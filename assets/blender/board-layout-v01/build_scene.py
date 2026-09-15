import bpy, math, json
from pathlib import Path
from mathutils import Vector

OUT = Path('C:/Users/u/Documents/Codex/Cadi-Launch-Film/assets/blender/board-layout-v01')
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'source-preserved-v01.blend'))
bpy.ops.ed.undo_push(message='Build reference board in separate scene')
scene = bpy.data.scenes.new('Board_Layout_v01')
bpy.context.window.scene = scene
scene.unit_settings.system = 'METRIC'
scene.unit_settings.length_unit = 'MILLIMETERS'
scene['reference'] = 'codex-clipboard-a820c406-0334-4567-96e3-8e22db8aab5f.png'
scene['construction'] = 'Reference pixel tracing; all solid shapes 2 mm thick; no text objects or image textures.'
S=.00024
T=.002
collections={}
for key in ['01_Base','02_Main_Parts','03_Connectors','04_Surface_Details','05_Cameras']:
    c=bpy.data.collections.new(key); scene.collection.children.link(c); collections[key]=c
palette={'blue':'DDF0F9','grey':'B9B9B9','dark':'9C9F9E','edge':'BCCFD7','purple':'B5B1EC','violet':'B09ABE','green':'9BC8A4','olive':'94B489','cyan':'9DCCCF','lime':'BBCB42','pin':'858D8C','slot':'D4D7D6','led':'80BF45'}
mats={}
def linear(c): return c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4
for name,h in palette.items():
    m=bpy.data.materials.new(name); m.diffuse_color=tuple(linear(int(h[i:i+2],16)/255) for i in (0,2,4))+(1,); mats[name]=m
def poly(name,pts,color='grey',group='02_Main_Parts',z=T):
    p=[((x-677)*S,(305-y)*S) for x,y in pts]; n=len(p)
    verts=[(x,y,z) for x,y in p]+[(x,y,z+T) for x,y in p]
    faces=[tuple(reversed(range(n))),tuple(range(n,2*n))]
    faces += [(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)]
    mesh=bpy.data.meshes.new(name+'_Mesh'); mesh.from_pydata(verts,[],faces); mesh.update()
    ob=bpy.data.objects.new(name,mesh); collections[group].objects.link(ob); ob.data.materials.append(mats[color]); ob['thickness_mm']=2.0
    return ob
def rect(name,x,y,w,h,color='grey',group='02_Main_Parts',z=T):
    return poly(name,[(x,y),(x+w,y),(x+w,y+h),(x,y+h)],color,group,z)
def outline(name,x,y,w,h,color='edge',width=2,z=T):
    for j,(a,b,c,d) in enumerate([(x,y,w,width),(x,y+h-width,w,width),(x,y,width,h),(x+w-width,y,width,h)]): rect(name+'_'+str(j),a,b,c,d,color,'04_Surface_Details',z)
def line(name,pts,color='dark',width=1.4,z=T+.000015):
    for j,((x,y),(a,b)) in enumerate(zip(pts,pts[1:])):
        dx=a-x;dy=b-y;l=math.hypot(dx,dy)
        if l<.001: continue
        nx=-dy/l*width/2;ny=dx/l*width/2
        poly(name+'_'+str(j),[(x+nx,y+ny),(a+nx,b+ny),(a-nx,b-ny),(x-nx,y-ny)],color,'04_Surface_Details',z)
def arc(cx,cy,r,a,b,n=36): return [(cx+r*math.cos(math.radians(a+(b-a)*i/n)),cy+r*math.sin(math.radians(a+(b-a)*i/n))) for i in range(n+1)]

rect('Board',19,26,1317,574,'blue','01_Base',0)
outline('Board_Edge',19,26,1317,574,width=2,z=.00001)
rect('Upper_Long_Purple',178,26,999,47,'purple')
rect('Left_Purple',128,97,109,33,'purple')
rect('Power_Bank',272,93,320,86)
outline('Power_Bank_Clearance',248,86,367,102)
for i in range(8):
    x=282+i*40
    for j in range(2):
        outline('Power_Cell_%d_%d'%(i,j),x,103+j*45,27,27,'dark',1.1)
        rect('Power_Contact_%d_%d'%(i,j),x+6,101+j*45,13,2,'dark','04_Surface_Details',T+.000015)
rect('Upper_Cooling_Left',677,92,194,68)
rect('Upper_Cooling_Right',894,82,242,87)
outline('Cooling_Left_Clearance',667,74,214,103)
outline('Cooling_Right_Clearance',883,74,266,104)
rect('CPU_Plate',339,216,205,101)
outline('CPU_Clearance',329,205,226,123)
outline('CPU_Center_Outline',401,253,68,27,'dark',1.3)
poly('Wireless_Green',[(204,201),(237,201)]+arc(243,201,6,180,0,16)+[(284,201),(284,297),(204,297)],'olive')
rect('Wireless_Connector',204,298,80,26)
outline('Wireless_Clearance',197,192,94,143)
for x in [208,275]: rect('Wireless_Contact_'+str(x),x,301,6,7,'dark','04_Surface_Details',T+.00002)

def fan(name,x,y,w,cy):
    r=w/2;cx=x+r
    poly(name,[(x,y),(x+w,y),(x+w,cy)]+arc(cx,cy,r,0,180,80)+[(x,y)])
    line(name+'_Clearance',[(x-8,y-8),(x+w+8,y-8),(x+w+8,cy)]+arc(cx,cy,r+9,0,180,80)+[(x-8,y-8)],'edge',2,z=T)
    # Three slim closed curved blade outlines, matching the visible fan symbols.
    for k in range(3):
        a=-75+k*120
        pts=arc(cx,cy,r*.64,a,a+74,26)+arc(cx,cy,r*.40,a+60,a+2,24)
        pts.append(pts[0]); line(name+'_Blade_'+str(k),pts,'dark',1.8)
fan('Fan_Left',688,191,170,276)
fan('Fan_Right',894,192,242,314)

def ram(name,x):
    pts=[(x,384),(x+258,384),(x+258,414),(x+252,414),(x+252,430),(x+258,430),(x+258,457),(x+252,457),(x+252,471),(x+258,471),(x+258,480),(x,480),(x,468),(x+6,468),(x+6,451),(x,451),(x,432),(x+6,432),(x+6,414),(x,414)]
    poly(name,pts,'green')
    rect(name+'_Socket',x-7,484,271,20,'dark','03_Connectors')
    rect(name+'_Slot',x-4,489,264,6,'pin','04_Surface_Details',T+.00002)
    for i in range(52): rect(name+'_Pin_%02d'%i,x+i*4.85,480,2.4,7,'slot','03_Connectors')
    for side in [-7,258]:
        for j in range(5):
            rect(name+'_Latch_%d_%d'%(side,j),x+side,418+j*17,7,11,'dark','03_Connectors')
            rect(name+'_Latch_Insert_%d_%d'%(side,j),x+side+2,419+j*17,3,5,'slot','04_Surface_Details',T+.00002)
    outline(name+'_Clearance',x-25,375,308,142)
ram('Memory_Left',104)
ram('Memory_Right',426)
rect('SSD_Connector',800,492,28,81,'dark','03_Connectors')
rect('SSD_Connector_Core',806,499,18,66,'grey','04_Surface_Details',T+.00002)
poly('SSD',[(830,491),(1115,491),(1115,526)]+arc(1115,533,7,-90,-270,20)+[(1115,574),(830,574)],'lime')
outline('SSD_Clearance',783,486,350,95)
poly('WWAN',[(1168,333),(1211,333)]+arc(1221,333,10,180,0,20)+[(1274,333),(1274,504),(1168,504)],'cyan')
rect('WWAN_Connector',1183,505,76,24,'grey','03_Connectors')
outline('WWAN_Clearance',1158,316,126,234)
outline('WWAN_Internal',1170,351,101,94,'edge',1.5)
line('WWAN_Lower_Pattern',[(1183,460),(1183,470),(1251,470),(1251,460)],'dark',1.3)
for i in range(17): rect('WWAN_Pins_'+str(i),1193+i*3,471,1.7,3,'dark','04_Surface_Details',T+.00002)
for i in range(3): rect('WWAN_Traces_'+str(i),1199+i*7,491-i*4,39,1,'dark','04_Surface_Details',T+.00002)
rect('Bottom_Gray_Left',257,528,73,40)
rect('Bottom_Gray_Center',352,529,144,48)
outline('Bottom_Gray_Left_Clearance',252,523,84,49)
outline('Bottom_Gray_Center_Clearance',344,524,160,56)
rect('Bottom_Purple',634,554,109,32,'purple')
rect('Bottom_Small_Purple_A',244,584,30,16,'purple')
rect('Bottom_Small_Purple_B',299,584,31,16,'purple')
outline('Bottom_Header_Clearance',520,560,86,33)
rect('Bottom_Header',533,564,61,14,'grey','03_Connectors')
for i in range(10): rect('Header_Pin_'+str(i),535+i*6,576,2,11,'dark','03_Connectors')
rect('Left_Violet_A',85,142,42,50,'violet')
rect('Left_Violet_B',84,215,42,49,'violet')
outline('Left_Violet_Clearance_A',79,138,52,60)
outline('Left_Violet_Clearance_B',79,210,52,59)

def port(name,x,y,w,h):
    pts=[(x+5,y),(x+12,y),(x+12,y+3),(x+w-8,y+3),(x+w-8,y),(x+w-3,y),(x+w-3,y+6),(x+w,y+6),(x+w,y+h-6),(x+w-4,y+h-6),(x+w-4,y+h),(x+8,y+h),(x+8,y+h-4),(x,y+h-4),(x,y+7),(x+5,y+7)]
    poly(name,pts,'grey','03_Connectors')
    for j in range(4):
        rect(name+'_PinA'+str(j),x+8+j*(w-16)/4,y-3,3,5,'dark','03_Connectors')
        rect(name+'_PinB'+str(j),x+8+j*(w-16)/4,y+h-1,3,5,'dark','03_Connectors')
    outline(name+'_Clearance',x-5,y-8,w+10,h+16)
port('Left_Top_Port',33,63,48,50)
port('Left_Small_Port_A',30,163,31,23)
port('Left_Small_Port_B',30,221,31,25)
port('Left_Audio_Port',25,329,46,27)
port('Left_Square_Port',87,330,39,32)
outline('Left_Square_Port_Inner',92,334,26,21,'slot',2)
rect('Right_Slim_Port',1199,129,36,58)
outline('Right_Slim_Port_Clearance',1196,123,43,71)
port('Right_Top_Port',1273,120,45,49)
port('Right_Middle_Port',1275,212,43,43)
rect('Right_Green_Indicator_A',1278,220,22,6,'led','04_Surface_Details',T+.00002)
rect('Right_Green_Indicator_B',1278,241,19,6,'led','04_Surface_Details',T+.00002)
port('Right_Lower_Port',1289,293,31,27)
for i,(x,y) in enumerate([(44,574),(1299,574),(651,361),(884,448)]): rect('Small_Mount_'+str(i),x,y,13,10,'dark','03_Connectors')

def camera(name,location,target,scale):
    d=bpy.data.cameras.new(name);ob=bpy.data.objects.new(name,d);collections['05_Cameras'].objects.link(ob)
    ob.location=location;ob.rotation_euler=(Vector(target)-ob.location).to_track_quat('-Z','Y').to_euler();d.type='ORTHO';d.ortho_scale=scale;d.clip_start=.001;d.clip_end=100;return ob
top=camera('Top_Reference_View',(0,0,1),(0,0,0),1353*S)
angle=camera('Angled_Thickness_View',(0,-.44,.65),(0,0,0),.354)
scene.camera=top;scene.render.engine='BLENDER_WORKBENCH';scene.render.resolution_x=1624;scene.render.resolution_y=732;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
sh=scene.display.shading;sh.light='FLAT';sh.color_type='MATERIAL';sh.show_shadows=False;sh.show_cavity=False;sh.show_specular_highlight=False;sh.show_object_outline=False;sh.background_type='WORLD';scene.world=bpy.data.worlds.new('White_World');scene.world.color=(1,1,1)
scene.view_settings.view_transform='Standard'
scene.render.filepath=str(OUT/'board-top-v01.png');bpy.ops.render.render(write_still=True)
scene.camera=angle;sh.light='STUDIO';sh.show_shadows=True;sh.show_cavity=True;sh.cavity_type='BOTH'
scene.render.resolution_y=940;scene.render.filepath=str(OUT/'board-angle-v01.png');bpy.ops.render.render(write_still=True)
scene.camera=top;sh.light='FLAT';sh.show_shadows=False;sh.show_cavity=False;scene.render.resolution_y=732
for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type=='VIEW_3D':
            area.spaces.active.shading.color_type='MATERIAL'
            area.spaces.active.region_3d.view_perspective='CAMERA'
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'board-layout-v01.blend'))
result={'file':str(OUT/'board-layout-v01.blend'),'scene':scene.name,'objects':len(scene.objects),'text_objects':sum(o.type=='FONT' for o in scene.objects),'solid_thickness_mm':2,'renders':['board-top-v01.png','board-angle-v01.png']}
(OUT/'verification-v01.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
