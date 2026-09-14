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
            fail(f"內文寫了 {bad.strip('\\b')} 但單段實為 15.083 秒；"
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
                check_registry(text, reg, args.segment, indices)

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
