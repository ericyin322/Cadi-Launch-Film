import bpy
s=bpy.context.scene
result={'file':bpy.data.filepath,'scene':s.name,'camera':s.camera.name if s.camera else None,'frames':[s.frame_start,s.frame_end],'fps':s.render.fps,'rigs':[o.name for o in s.objects if o.type=='EMPTY'],'collections':[c.name for c in s.collection.children]}
