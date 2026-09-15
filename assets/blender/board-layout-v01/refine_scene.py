import bpy, math, json
from pathlib import Path
OUT=Path('C:/Users/u/Documents/Codex/Cadi-Launch-Film/assets/blender/board-layout-v01')
scene=bpy.context.scene
for ob in list(scene.objects):
    if '_Blade_' in ob.name: bpy.data.objects.remove(ob,do_unlink=True)
    elif ob.name.startswith(('CPU_Center_Outline','Power_Cell_','WWAN_Internal','Left_Square_Port_Inner')): ob.location.z+=.000025
patterns=[[(737,279),(743,254),(764,235),(785,229),(797,232),(777,245),(759,263),(752,281)],[(799,245),(810,238),(823,248),(833,267),(835,289),(829,301),(823,281),(815,262)],[(748,296),(770,303),(790,303),(808,296),(815,310),(797,321),(775,323),(759,314),(746,301)]]
def smooth(p):
    out=[]
    for i in range(len(p)):
        a,b,c,d=[p[j%len(p)] for j in [i-1,i,i+1,i+2]]
        for k in range(7):
            t=k/7
            out.append(tuple(.5*((2*b[q])+(-a[q]+c[q])*t+(2*a[q]-5*b[q]+4*c[q]-d[q])*t*t+(-a[q]+3*b[q]-3*c[q]+d[q])*t*t*t) for q in [0,1]))
    return out+[out[0]]
group=next(c for c in scene.collection.children if c.name.startswith('04_Surface_Details'))
for name,cx,cy,scale in [('Fan_Left',773,276,1),('Fan_Right',1015,314,242/170)]:
    for k,p in enumerate(patterns):
        pts=[(cx+(x-773)*scale,cy+(y-276)*scale) for x,y in smooth(p)]
        verts=[];faces=[]
        for (x,y),(a,b) in zip(pts,pts[1:]):
            l=math.hypot(a-x,b-y);nx=-(b-y)/l*.75;ny=(a-x)/l*.75
            corners=[(x+nx,y+ny),(a+nx,b+ny),(a-nx,b-ny),(x-nx,y-ny)]
            start=len(verts)
            verts.extend([((u-677)*.00024,(305-v)*.00024,z) for z in [.002025,.004025] for u,v in corners])
            faces.extend([tuple(start+j for j in f) for f in [(3,2,1,0),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]])
        mesh=bpy.data.meshes.new(name+'_BladeTrace');mesh.from_pydata(verts,[],faces);mesh.update()
        ob=bpy.data.objects.new(name+'_Blade_'+str(k),mesh);group.objects.link(ob);mesh.materials.append(bpy.data.materials['dark']);ob['thickness_mm']=2.0
scene.camera=bpy.data.objects['Top_Reference_View'];scene.render.filepath=str(OUT/'board-top-v02.png');bpy.ops.render.render(write_still=True)
scene.camera=bpy.data.objects['Angled_Thickness_View'];scene.render.resolution_y=940
sh=scene.display.shading;sh.light='STUDIO';sh.show_shadows=True;sh.show_cavity=True
scene.render.filepath=str(OUT/'board-angle-v02.png');bpy.ops.render.render(write_still=True)
scene.camera=bpy.data.objects['Top_Reference_View'];scene.render.resolution_y=732;sh.light='FLAT';sh.show_shadows=False;sh.show_cavity=False
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'board-layout-v02.blend'))
meshes=[o for o in scene.objects if o.type=='MESH']
result={'file':str(OUT/'board-layout-v02.blend'),'scene':scene.name,'mesh_count':len(meshes),'text_count':sum(o.type=='FONT' for o in scene.objects),'thickness_range_mm':[min(o.dimensions.z for o in meshes)*1000,max(o.dimensions.z for o in meshes)*1000],'blender_version':bpy.app.version_string}
(OUT/'verification-v02.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
