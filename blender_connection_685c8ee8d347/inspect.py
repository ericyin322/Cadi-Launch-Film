import bpy
result = {
    "version": bpy.app.version_string,
    "pid": __import__("os").getpid(),
    "file": bpy.data.filepath,
    "active_scene": bpy.context.scene.name,
    "scenes": [{
        "name": s.name,
        "objects": [{"name": o.name, "type": o.type} for o in s.objects],
        "camera": s.camera.name if s.camera else None,
        "collections": [c.name for c in s.collection.children],
        "frames": [s.frame_start, s.frame_end],
        "fps": s.render.fps / s.render.fps_base,
        "units": s.unit_settings.system,
    } for s in bpy.data.scenes],
}
