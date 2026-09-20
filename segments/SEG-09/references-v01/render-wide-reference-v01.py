import bpy
from pathlib import Path
r=Path('C:/Users/u/Documents/Codex/Cadi-Launch-Film');s=bpy.data.scenes['SEG09_Creo_Dock_v06'];bpy.context.window.scene=s;s.frame_set(396)
c=s.camera.copy();c.data=s.camera.data.copy();c.animation_data_clear();s.collection.objects.link(c)
for con in list(c.constraints):c.constraints.remove(con)
from mathutils import Vector
c.location=(0,0,100);c.rotation_euler=(Vector((0,27,1))-c.location).to_track_quat('-Z','Y').to_euler();c.data.lens=28
s.timeline_markers.clear();s.camera=c;s.render.resolution_x=1600;s.render.resolution_y=900;s.render.filepath=str(r/'segments/SEG-09/references-v01/picture-04-carry-layout-wide-v01.png');bpy.ops.render.render(write_still=True,scene=s.name)
