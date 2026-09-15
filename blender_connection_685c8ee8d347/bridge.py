"""Run inside Blender to accept local file-based Codex requests."""

import json
import os
import time
import traceback
from pathlib import Path

import bpy

# Set this to the project's private bridge directory before running.
BRIDGE_ROOT = Path('C:\\Users\\u\\Documents\\Codex\\Cadi-Launch-Film\\blender_connection_685c8ee8d347')
if BRIDGE_ROOT is None:
    raise RuntimeError("Run prepare_connection.py first, then open the generated bridge.py in Blender.")
REQUEST = BRIDGE_ROOT / "request.json"
RESPONSE = BRIDGE_ROOT / "response.json"
CONNECTED = BRIDGE_ROOT / "connected.json"


def poll():
    if not REQUEST.exists():
        return 0.25

    request = None
    try:
        request = json.loads(REQUEST.read_text(encoding="utf-8"))
        REQUEST.unlink()
        scope = {"bpy": bpy, "result": None}
        exec(compile(request["code"], "<codex-blender-request>", "exec"), scope)
        payload = {"id": request.get("id"), "ok": True, "result": scope.get("result")}
    except Exception:
        payload = {
            "id": request.get("id") if isinstance(request, dict) else None,
            "ok": False,
            "error": traceback.format_exc(),
        }

    temp = BRIDGE_ROOT / "response.tmp"
    temp.write_text(json.dumps(payload, ensure_ascii=False, default=str), encoding="utf-8")
    temp.replace(RESPONSE)
    return 0.25


BRIDGE_ROOT.mkdir(parents=True, exist_ok=True)
old = bpy.app.driver_namespace.get("_codex_local_file_bridge")
if old and bpy.app.timers.is_registered(old):
    bpy.app.timers.unregister(old)
bpy.app.driver_namespace["_codex_local_file_bridge"] = poll
bpy.app.timers.register(poll, first_interval=0.1, persistent=True)
CONNECTED.write_text(
    json.dumps(
        {"version": bpy.app.version_string, "file": bpy.data.filepath, "timestamp": time.time(), "pid": os.getpid(), "executable": bpy.app.binary_path},
        ensure_ascii=False,
    ),
    encoding="utf-8",
)
