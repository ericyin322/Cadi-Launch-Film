import bpy, math, json
from pathlib import Path
OUT=Path('C:/Users/u/Documents/Codex/Cadi-Launch-Film/assets/blender/cpu-motion-v01')
OUT.mkdir(exist_ok=True)
(OUT/'frames').mkdir(exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'cpu-motion-v01.blend'))
bpy.ops.ed.undo_push(message='CPU two second highlight and translation')
source=bpy.context.scene
scene=source.copy();scene.name='CPU_Motion_v01';bpy.context.window.scene=scene
# Isolate animated parts, so the original board scene remains intact.
animated=bpy.data.collections.new('06_CPU_Animation_v01');scene.collection.children.link(animated)
rig=bpy.data.objects.new('CPU_Motion_Rig_v01',None);animated.objects.link(rig)
rig.empty_display_type='PLAIN_AXES';rig.empty_display_size=.01
cpu=[]
for original in list(source.objects):
    if original.name.startswith('CPU_'):
        ob=original.copy();ob.data=original.data.copy();ob.name=original.name+'_Animated'
        animated.objects.link(ob);ob.parent=rig;cpu.append(ob)
# Shared source collections are excluded only from the new scene by copying
# their collection containers and linking static objects into replacements.
for original_collection in list(scene.collection.children):
    if original_collection==animated: continue
    replacement=bpy.data.collections.new(original_collection.name+'_Motion')
    scene.collection.children.link(replacement)
    for ob in original_collection.objects:
        if not ob.name.startswith('CPU_'): replacement.objects.link(ob)
    scene.collection.children.unlink(original_collection)
plate=next(o for o in cpu if o.name.startswith('CPU_Plate'))
mat=plate.data.materials[0].copy();mat.name='CPU_Highlight_v01';plate.data.materials[0]=mat
base=tuple(mat.diffuse_color)
def lin(x): return x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4
gold=tuple(lin(c) for c in (1,.82,.22))+(1,)
FPS=60;distance=205*.00024*.1
def ease(x):
    x=max(0,min(1,x));return x*x*(3-2*x)
samples=[]
for f in range(1,122):
    t=(f-1)/FPS
    amount=ease(t/.1) if t<.1 else (1 if t<.3 else (1-ease((t-.3)/.1) if t<.4 else 0))
    mat.diffuse_color=tuple(a+(b-a)*amount for a,b in zip(base,gold));mat.keyframe_insert(data_path='diffuse_color',frame=f)
    x=0 if t<.6 else (distance*ease((t-.6)/.4) if t<1 else (distance if t<1.6 else distance*(1-ease((t-1.6)/.4))))
    if f>=120: x=0
    rig.location=(x,0,0);rig.keyframe_insert(data_path='location',frame=f)
    samples.append({'frame':f,'time':t,'x_mm':x*1000,'highlight':amount})
scene.render.fps=FPS;scene.render.fps_base=1;scene.frame_start=1;scene.frame_end=120
scene.camera=bpy.data.objects['Top_Reference_View']
scene.render.engine='BLENDER_WORKBENCH'
scene.render.resolution_x=1624;scene.render.resolution_y=732;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.render.filepath=str(OUT/'frames/frame-')
for label,frame in [('Highlight',1),('Pause',25),('Move_Right',37),('Hold_Right',61),('Return_Left',97),('Restored',120)]: scene.timeline_markers.new(label,frame=frame)
manifest={'duration_seconds':2,'fps':FPS,'frames':120,'right_shift_mm':distance*1000,'camera':'Top_Reference_View','phases':[{'start':0,'end':.4,'action':'CPU 金黃色亮顯一次，再恢復原色'},{'start':.4,'end':.6,'action':'停頓'},{'start':.6,'end':1,'action':'平滑右移'},{'start':1,'end':1.6,'action':'停頓'},{'start':1.6,'end':2,'action':'平滑左移回原位'}],'animated_objects':[o.name for o in cpu],'samples':samples}
(OUT/'animation-manifest-v01.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
scene.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'cpu-motion-v01.blend'))
bpy.ops.render.render(animation=True)
scene.frame_set(1)
result={'blend':str(OUT/'cpu-motion-v01.blend'),'frames':120,'fps':60,'duration':2,'shift_mm':distance*1000,'animated_parts':len(cpu),'text_count':sum(o.type=='FONT' for o in scene.objects)}
