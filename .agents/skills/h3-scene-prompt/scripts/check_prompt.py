#!/usr/bin/env python3
"""
驗證單段 H3 prompt。

    python check_prompt.py seg/S03a.txt --registry cast_registry.yaml --segment S03a

沒給 --registry 時只做不需要 registry 的通用檢查（索引連續性、區段順序、字元數等）。
離開碼 0 = 全過，1 = 有 FAIL。WARN 不影響離開碼。

只依賴 PyYAML；沒裝的話 registry 相關檢查會被跳過並提示。
"""

import argparse
import re
import sys
import unicodedata

MAX_CHARS = 7000
MAX_IMAGES = 9
SOFT_MAX_IMAGES = 4

SECTIONS_DETAILED = [
    "subject_definitions",
    "summary",
    "retention_analysis",
    "detailed_description",
    "overall_soundscape",
    "non_diegetic_music",
]
SECTIONS_INTEGRATED = [
    "subject_definitions",
    "retention_analysis",
    "integrated_multimodal_description",
    "overall_soundscape",
]

results = []


def ok(msg):
    results.append(("PASS", msg))


def warn(msg):
    results.append(("WARN", msg))


def fail(msg):
    results.append(("FAIL", msg))


def normalize(s):
    """比對 canonical description 用：壓平空白、統一標點，但保留字詞本身。"""
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def find_labels(text):
    """
    官方契約是 Subject / Picture 配對使用：
        <Subject 1> is ... ; ... follow <Picture 1>.
    <Picture N> = 第 N 個 ref_image 插槽（上傳順序），<Subject N> = 從該圖抽出的身份。
    回傳 (style, picture_indices, subject_indices)。
    """
    pics = sorted({int(n) for n in re.findall(r"<Picture\s+(\d+)>", text)})
    subs = sorted({int(n) for n in re.findall(r"<Subject\s+(\d+)>", text)})

    if pics and subs:
        style = "paired"
        ok("標籤形式: <Subject N> / <Picture N> 配對（官方契約）")
        orphan = [n for n in subs if n not in pics]
        if orphan:
            fail(f"<Subject {orphan}> 沒有對應的 <Picture N>，身份沒有綁到參考圖插槽")
        extra = [n for n in pics if n not in subs]
        if extra:
            warn(f"<Picture {extra}> 沒有對應的 <Subject N>；"
                 f"若該圖只作構圖錨點是合理的，若是角色圖則漏了身份綁定")
    elif pics:
        style = "picture-only"
        warn("只用了 <Picture N>，沒有 <Subject N>。node pack 的契約是兩者配對，"
             "身份鎖定建議改寫成 <Subject N> is ... follows <Picture N>")
    elif subs:
        style = "subject-only"
        fail("只有 <Subject N> 而沒有 <Picture N>，身份沒有綁到任何參考圖插槽")
    else:
        style = None
    return style, pics, subs


def check_sections(text):
    found = [(m.start(), m.group(1))
             for m in re.finditer(r"(?m)^([A-Za-z_]\w*):", text)]
    names = [n for _, n in found]
    known = set(SECTIONS_DETAILED) | set(SECTIONS_INTEGRATED)
    present = [n for n in names if n in known]

    if "integrated_multimodal_description" in present:
        expected, style = SECTIONS_INTEGRATED, "integrated"
    else:
        expected, style = SECTIONS_DETAILED, "detailed"

    missing = [s for s in expected if s not in present]
    if missing:
        fail(f"缺少區段（{style} 格式）: {', '.join(missing)}")
    else:
        ok(f"六區段齊全（{style} 格式）")

    ordered = [s for s in present if s in expected]
    if ordered != [s for s in expected if s in ordered]:
        fail(f"區段順序錯誤: 實際 {ordered}，應為 {expected}")
    elif not missing:
        ok("區段順序正確")
    return style


def check_declared(text, indices):
    """subject_definitions 裡宣告過的索引，必須涵蓋全文用到的索引。"""
    m = re.search(
        r"(?ms)^subject_definitions:\s*(.*?)(?=^[A-Za-z_]\w*:|\Z)", text)
    if not m:
        fail("找不到 subject_definitions 區段，無法檢查宣告")
        return set()
    block = m.group(1)
    declared = {int(n) for n in re.findall(r"<(?:Picture|Subject)\s+(\d+)>", block)}
    undeclared = set(indices) - declared
    if undeclared:
        fail(f"以下索引在內文使用但未在 subject_definitions 宣告: "
             f"{sorted(undeclared)}")
    else:
        ok("內文用到的索引都已宣告")
    unused = declared - set(indices)
    if unused:
        warn(f"宣告了但內文沒用到: {sorted(unused)}")
    return declared


def check_timeline(text, style):
    body_key = ("integrated_multimodal_description" if style == "integrated"
                else "detailed_description")
    m = re.search(rf"(?ms)^{body_key}:\s*(.*?)(?=^[A-Za-z_]\w*:|\Z)", text)
    if not m:
        fail(f"找不到 {body_key} 區段")
        return
    body = m.group(1)
    stamps = re.findall(r"(?:^|\s)(\d+):(\d{2})(?=\s)", body)
    ranges = re.findall(r"\[(\d+)s\s*-\s*(\d+)s\]", body)
    beats = len(stamps) + len(ranges)
    total = beats + 1 if stamps else beats
    if beats == 0:
        fail("內文沒有任何時間碼；15 秒必須切成 5-6 個 beat，否則後半段會停滯或循環")
    elif total < 4:
        warn(f"只有約 {total} 個 beat；15 秒建議 5-6 個，動作密度不足會導致後段停滯")
    else:
        ok(f"時間碼 beat 數 ≈ {total}")

    if stamps:
        secs = [int(a) * 60 + int(b) for a, b in stamps]
        if secs != sorted(secs):
            fail(f"時間碼非遞增: {['%d:%02d' % (s // 60, s % 60) for s in secs]}")
        if secs and secs[-1] > 15:
            warn(f"最後一個時間碼 {secs[-1]}s 超過單段長度 15.083s")

    for bad, good in [(r"\bnine-second\b", "fifteen-second"),
                      (r"\bten-second\b", "fifteen-second"),
                      (r"\btwenty-second\b", "fifteen-second"),
                      (r"\bthirty-second\b", "fifteen-second")]:
        if re.search(bad, body, re.I):
            word = bad.replace("\\b", "")
            fail(f"內文寫了 {word} 但單段實為 15.083 秒；"
                 f"秒數不符會讓模型壓縮或拉長節奏，改成 {good}")


def check_negatives(text, style):
    body_key = ("integrated_multimodal_description" if style == "integrated"
                else "detailed_description")
    m = re.search(rf"(?ms)^{body_key}:\s*(.*?)(?=^[A-Za-z_]\w*:|\Z)", text)
    body = m.group(1) if m else ""
    if not re.search(r"\bno (readable text|subtitles)\b", body, re.I):
        fail("負面表列缺失或不完整（找不到 no readable text / no subtitles）")
    else:
        ok("負面表列存在")


# ---------------------------------------------------------------------------
# 召喚檢查：H3 的文字條件沒有否定運算子，提示詞裡出現的物件名詞一律會被畫出來。
# 「排除宣告」「保留槽」不但無效，而且是強力的正向條件；Ref2VA 連上傳參考圖本身
# 都是召喚。不出場的東西唯一正確的處理方式是：完全不提、不上傳、不編索引。
# ---------------------------------------------------------------------------

EXCLUSION_PATTERNS = [
    (r"\bis the excluded\b", "排除宣告"),
    (r"\bexcluded (?:mascot|subject|character|asset)\b", "排除宣告"),
    (r"\bnot an on-screen\b", "排除宣告"),
    (r"\breserved (?:project )?declaration\b", "保留槽宣告"),
    (r"\bis (?:a )?reserved\b", "保留槽宣告"),
    (r"\bunused and absent\b", "排除宣告"),
    (r"\babsent from every\b", "排除宣告"),
    (r"\bno (?:second|third|fourth|fifth|sixth) image is (?:supplied|used|provided)\b",
     "保留槽宣告"),
    (r"\bmandatory reserved\b", "保留槽宣告"),
    (r"\b(?:unconnected|unbound) and absent\b", "保留槽宣告"),
]

# 負面表列允許的字詞：畫面瑕疵與鏡頭屬性，沒有對應的可繪製實體。
NEGATIVE_ALLOW = {
    "subtitle", "subtitles", "text", "caption", "captions", "watermark",
    "watermarks", "logo", "logos", "letter", "letters", "lettering",
    "typography", "font", "fonts", "panel", "panels", "border", "borders",
    "number", "numbers", "monochrome", "grayscale", "greyscale",
    "black-and-white", "live-action", "photoreal", "photorealistic",
    "finger", "fingers", "limb", "limbs", "deformed", "deformity",
    "duplicate", "duplicated", "extra", "distortion", "artifact", "artifacts",
    "blur", "blurring", "morph", "morphing", "flicker", "flickering",
    "jitter", "shaky", "shake", "handheld", "slow", "speed", "time-lapse",
    "timelapse", "loop", "looping", "freeze", "frozen", "reverse",
    "backward", "mirror", "mirrored", "mirroring", "penetration", "clipping",
    "jelly", "gelatinous", "rubbery", "cut", "cuts", "transition",
    "transitions", "zoom", "dolly", "pan", "split", "collage", "montage",
    "motion", "render", "rendering", "seam", "banding", "noise", "aliasing",
    "glitch", "camera", "shot", "frame", "output", "switch", "spoken",
    "dialogue", "lyrics", "invented", "scripted",
}


def _negative_block(body):
    """只取負面表列那一段；內文敘述裡的 no/without 是劇情，不在這裡判。"""
    m = re.search(r"(?is)\bnegative constraints?\s*:(.*?)(?:\n\s*\n|\Z)", body)
    if m:
        return m.group(1)
    paras = [x for x in re.split(r"\n\s*\n", body) if re.match(r"\s*No\b", x)]
    return paras[-1] if paras else ""


def _negative_items(body):
    """抓負面表列裡的每一條 no 項目。"""
    block = _negative_block(body)
    return [(m.group(0).strip(), m.group(1).strip().lower())
            for m in re.finditer(r"(?i)\bno\s+([^.,;:\n]{2,60})", block)]


def check_summoning(text, style, reg=None, cast=None):
    body_key = ("integrated_multimodal_description" if style == "integrated"
                else "detailed_description")
    m = re.search(rf"(?ms)^{body_key}:\s*(.*?)(?=^[A-Za-z_]\w*:|\Z)", text)
    body = m.group(1) if m else ""

    hits = 0

    # (a) 排除／保留宣告句型：全文都不該出現（重疊的命中合併成一條）
    spans = []
    for pat, label in EXCLUSION_PATTERNS:
        for mm in re.finditer(pat, text, re.I):
            spans.append((mm.start(), mm.end(), label))
    spans.sort()
    merged = []
    for start, end, label in spans:
        if merged and start <= merged[-1][1] + 60:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end, label])
    for start, end, label in merged:
        line = text[max(0, start - 30):end + 30].replace("\n", " ")
        fail(f"{label}會把物件召喚進畫面，必須整段刪除: \"...{line.strip()}...\"")
        hits += 1

    # (b) 否定句裡出現參考標籤：等於一邊說不要、一邊餵完整描述
    for mm in re.finditer(
            r"(?i)\b(?:no|not|never|without)\b[^.;\n]{0,60}?"
            r"<(?:Picture|Subject)\s+\d+>", text):
        line = mm.group(0).replace("\n", " ")
        fail(f"否定句裡帶了參考標籤，模型只會讀到標籤指向的物件: \"{line.strip()}\"")
        hits += 1

    # (c) registry 比對：不在 cast 卻在提示詞裡被提名的資產
    if reg and cast is not None:
        assets = reg.get("assets", {})
        for key, asset in assets.items():
            if key in cast:
                continue
            tokens = [key.replace("_", " ")] + list(asset.get("summon_tokens") or [])
            for tok in tokens:
                tok = str(tok).strip().lower()
                if not tok:
                    continue
                if re.search(r"(?<![\w-])" + re.escape(tok) + r"(?![\w-])",
                             text, re.I):
                    fail(f"資產 {key} 不在 {'/'.join(sorted(cast))} 的 cast 裡，"
                         f"但提示詞出現 \"{tok}\"；不出場就一個字都不能提")
                    hits += 1
                    break

    # (d) 負面表列裡的物件名詞：WARN，請改寫成正向狀態描述
    allowed_extra = []
    if reg and cast:
        for key in cast:
            for neg in (reg.get("assets", {}).get(key, {})
                        .get("extra_negatives") or []):
                allowed_extra.append(normalize(neg))
    for whole, item in _negative_items(body):
        if "<picture" in item or "<subject" in item:
            continue  # 已由 (b) 以 FAIL 報過
        words = set(re.findall(r"[a-z][a-z-]+", item))
        if words & NEGATIVE_ALLOW:
            continue
        norm_item = normalize(item)
        if any(e and (e in norm_item or norm_item in e) for e in allowed_extra):
            continue  # registry 針對出場角色指定的材質負面詞
        warn(f"負面表列 \"{whole}\" 在點名物件而非畫面瑕疵；"
             f"物件名詞會被召喚，請刪掉或改寫成正向狀態"
             f"（例如 \"the laptop stays closed\"）")

    if hits == 0:
        ok("沒有排除宣告、保留槽或否定標籤（不出場的物件不會被召喚）")


def check_length(text):
    n = len(text)
    if n > MAX_CHARS:
        fail(f"prompt {n} 字元，超過上限 {MAX_CHARS}")
    else:
        ok(f"長度 {n} 字元（上限 {MAX_CHARS}）")


def check_placeholders(text):
    leftovers = re.findall(r"<<<.*?>>>", text, re.S)
    if leftovers:
        fail(f"還有 {len(leftovers)} 處樣板佔位沒填（<<<...>>>）")
    if "使用說明" in text or "=====" in text:
        fail("樣板頂部的使用說明沒刪掉")


def check_registry(text, reg, seg_id, indices):
    segs = {s["id"]: s for s in reg.get("segments", [])}
    if seg_id not in segs:
        fail(f"registry 裡找不到分段 {seg_id}")
        return
    seg = segs[seg_id]
    assets = reg["assets"]
    cast = seg.get("cast", [])

    unknown = [c for c in cast if c not in assets]
    if unknown:
        fail(f"{seg_id} 的 cast 含 registry 未定義的資產: {unknown}")
        return

    order = sorted(cast, key=lambda k: assets[k]["priority"])
    expected = {i + 1: k for i, k in enumerate(order)}

    if sorted(expected) != indices:
        fail(f"索引與 cast 不符: registry 期望 {sorted(expected)} "
             f"({', '.join(f'{i}={k}' for i, k in expected.items())})，"
             f"prompt 實際用了 {indices}")
    else:
        ok("索引數量與 cast 一致: " +
           ", ".join(f"<{'Picture'} {i}>={k}" for i, k in expected.items()))

    # canonical description 是否被逐字複製
    norm_text = normalize(text)
    for i, key in expected.items():
        canon = normalize(assets[key].get("canonical", ""))
        if not canon:
            continue
        if canon in norm_text:
            ok(f"<Picture {i}> ({key}) canonical description 逐字一致")
        else:
            fail(f"<Picture {i}> ({key}) 的 canonical description 被改寫過。"
                 f"必須從 registry 逐字複製，否則跨段會漂移")

    # 角色專屬負面詞
    for key in cast:
        for neg in assets[key].get("extra_negatives", []) or []:
            if normalize(neg) not in norm_text:
                fail(f"{key} 出場但負面表列缺少 \"{neg}\"")

    n = len(cast)
    if n > MAX_IMAGES:
        fail(f"{n} 張參考圖，超過上限 {MAX_IMAGES}")
    elif n > SOFT_MAX_IMAGES:
        warn(f"{n} 張參考圖，超過建議值 {SOFT_MAX_IMAGES}，身份鎖定會變鬆")

    print(f"\n上傳順序（ref_order，必須照這個順序掛圖）:")
    for i, key in expected.items():
        print(f"  ref_image_{i-1}  {assets[key]['file']:<28}"
              f"-> <Picture {i}> / <Subject {i}> = {key}")
    print(f"  seed = {seg.get('seed', '未設定')}, "
          f"frames = {reg['project'].get('frames_per_segment', 362)}")
    return cast


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt")
    ap.add_argument("--registry")
    ap.add_argument("--segment")
    args = ap.parse_args()

    text = open(args.prompt, encoding="utf-8").read()

    check_placeholders(text)
    style = check_sections(text)
    label_style, indices, sub_indices = find_labels(text)

    if not indices:
        warn("沒有任何 <Picture N> / <Subject N> 標籤；這是 T2VA 而非 Ref2VA prompt？")
    else:
        if indices != list(range(1, len(indices) + 1)):
            fail(f"<Picture> 索引不連續: {indices}，必須是 1..N 無跳號，否則會和 ref_image 插槽錯位")
        else:
            ok(f"<Picture> 索引連續: 1..{len(indices)} (= ref_image_0..{len(indices)-1})")
        check_declared(text, indices)

    check_timeline(text, style)
    check_negatives(text, style)
    check_length(text)

    reg = None
    cast = None
    if args.registry:
        if not args.segment:
            fail("給了 --registry 就必須同時給 --segment")
        else:
            try:
                import yaml
            except ImportError:
                warn("未安裝 PyYAML，跳過 registry 比對（pip install pyyaml）")
            else:
                reg = yaml.safe_load(open(args.registry, encoding="utf-8"))
                cast = check_registry(text, reg, args.segment, indices)

    check_summoning(text, style, reg, set(cast) if cast else None)

    print()
    for level, msg in results:
        mark = {"PASS": "  ok  ", "WARN": " warn ", "FAIL": " FAIL "}[level]
        print(f"[{mark}] {msg}")

    n_fail = sum(1 for l, _ in results if l == "FAIL")
    n_warn = sum(1 for l, _ in results if l == "WARN")
    print(f"\n{len(results) - n_fail - n_warn} passed, {n_warn} warnings, {n_fail} failed")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
