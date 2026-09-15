import bpy,json
from pathlib import Path
OUT=Path('C:/Users/u/Documents/Codex/Cadi-Launch-Film/assets/blender/cpu-motion-v02')
OUT.mkdir(exist_ok=True);(OUT/'frames').mkdir(exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'cpu-motion-v02.blend'))
bpy.ops.ed.undo_push(message='Increase CPU translation threefold')
s=bpy.context.scene;s.name='CPU_Motion_v02'
rig=bpy.data.objects['CPU_Motion_Rig_v01']
rig.animation_data_clear()
distance=.01476
def ease(x):
    x=max(0,min(1,x));return x*x*(3-2*x)
samples=[]
for f in range(1,122):
    t=(f-1)/60
    x=0 if t<.6 else (distance*ease((t-.6)/.4) if t<1 else (distance if t<1.6 else distance*(1-ease((t-1.6)/.4))))
    if f>=120:x=0
    rig.location=(x,0,0);rig.keyframe_insert(data_path='location',frame=f)
    samples.append({'frame':f,'time':t,'x_mm':x*1000})
manifest=json.loads((OUT.parent/'cpu-motion-v01/animation-manifest-v01.json').read_text(encoding='utf-8'))
manifest.update({'right_shift_mm':14.76,'revision':'v02','change':'右移幅度放大為 v01 的三倍，時序相同','samples':samples})
(OUT/'animation-manifest-v02.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
s.render.filepath=str(OUT/'frames/frame-');s.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'cpu-motion-v02.blend'))
bpy.ops.render.render(animation=True)
s.frame_set(1)
result={'file':str(OUT/'cpu-motion-v02.blend'),'right_shift_mm':14.76,'frames':120,'fps':60}
