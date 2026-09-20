import yaml,json,copy
from pathlib import Path
r=Path('.');p=r/'segments/SEG-09';reg=yaml.safe_load((r/'cast_registry.yaml').read_text(encoding='utf-8'));a=copy.deepcopy(reg['assets']['cadi']);a['canonical']=a['canonical'].split(' Its height is approximately')[0];a['priority']=1
creo='Creo Robot, a massive industrial humanoid with broad rounded off-white shoulder armor, heavy elongated forearms, large articulated dark-metal hands, short sturdy legs, exposed gunmetal joints, green joint rings, a small rectangular head with a dark face panel and a single vertical warm-white optic, and a black-and-green cube emblem on the shoulder.'
assets={'cadi':a,'creo_robot':{'priority':2,'file':'assets/characters/creo-robot-concept/creo-robot-concept-v01.png','canonical':creo,'role':'identity'},'catch_anchor':{'priority':3,'file':'segments/SEG-09/references-v01/picture-03-fan-catch-v01.png','role':'pose_and_scale'},'layout_anchor':{'priority':4,'file':'segments/SEG-09/references-v01/picture-04-carry-layout-wide-v01.png','role':'spatial_layout_and_carrying'},'arrival_anchor':{'priority':5,'file':'segments/SEG-09/references-v01/picture-05-cadi-fan-placed-v01.png','role':'final_composition'}}
common=f'''subject_definitions:
<Subject 1> is {a['canonical']} Its design, proportions, and colors follow <Picture 1>.
<Subject 2> is {creo} Its appearance follows <Picture 2>; the lead carrier and four fellow carriers share this identity.
<Picture 3> is the lead carrier's giant-fan catch pose and relative-scale anchor.
<Picture 4> is the elevated wide spatial anchor for five carriers, their cargo, the rectangular placement plane and its component locations.
<Picture 5> is the spatial anchor for Cadi beside the installed right-hand fan and the fan's final footprint.

summary:
[reference generation] {{summary}}

retention_analysis:
<Subject 1> / <Picture 1>: fully_preserved - {a['retention']}
<Subject 2> / <Picture 2>: fully_preserved - preserve the shoulder silhouette, small head, vertical optic, green accents, articulated hands and heavy mechanical proportions on all five carriers.
<Picture 3>: partially_preserved - use the supported fan orientation, size relationship and hand contact as the physical reference for the lead carrier and its cargo.
<Picture 4>: partially_preserved - preserve the relative footprint and arrangement of components, five work routes and wide viewing direction. Current component positions follow the timed transport and placement states.
<Picture 5>: partially_preserved - preserve Cadi-to-fan scale and the installed fan footprint. Its settled relationship is reached at the end of the placement sequence.
Character identity comes from <Picture 1> and <Picture 2>. References <Picture 3>, <Picture 4> and <Picture 5> supply spatial relationships and poses. Surfaces are physically detailed metal, with realistic contact shadows and reflections.

detailed_description:
{reg['project']['visual_style']}
Inside a monumental engineering dock: white-gray structural metal, exposed service pipes, green structural accents, warm industrial lights and soft cyan fill reflecting across the floor. Deep side aisles frame a large rectangular placement platform. Use photographic industrial materials and coherent real lighting throughout.
{{timeline}}

Negative constraints: no subtitles, no extra fingers or limbs, no deformed limbs, no shaky camera, no looping; no rubbery, gelatinous, solid jelly texture; no solid glass surface on the plasma head.

overall_soundscape:
N/A. Silent throughout.

non_diegetic_music:
N/A.
'''
A='''[Shot 1] Close view of Cadi <Picture 1> hovering near the dock entrance, looking toward the lead Creo Robot <Picture 2>. Cadi's red plasma head continuously burns and sheds delicate orange-gold tongues and warm luminous embers.
[0s-2s] Cadi raises one hand, presses the middle finger against the thumb, then releases a crisp finger snap. Hold the final gesture briefly; his flame responds with a soft upward flicker.
[Shot 2] At 00:02.000, cut to a low-angle medium close-up of the lead Creo Robot, keeping its full head, shoulders, forearms and hands inside frame.
[2s-4s] The robot spreads its elbows, contracts its chest and drives both clenched hands down and inward beside its lower chest. Shoulder armor and forearm pistons tighten into a powerful downward chest-flex pose. The camera makes a restrained forward push.
[4s-5s] Hold the strength pose for a readable beat. The robot lifts its gaze toward the falling cargo and opens its hands, preparing to receive weight.
[Shot 3] At 00:05.000, cut wider and lower to include the robot, its feet and clear space overhead.
[5s-7s] One enormous laptop cooling fan falls vertically into view and accelerates downward. The lead carrier tracks its descent and raises both hands beneath the housing. At the end of this beat, establish the supported pose and scale from <Picture 3>; palms meet the underside and the fan's downward travel stops.
[7s-9s] The robot's knees bend, torso compresses and elbows yield briefly under the load; then the legs extend and shoulders brace, recovering to a stable carry. Maintain continuous hand-to-housing contact. The fan remains a single rigid assembly with a fixed outline and consistent size.
[Shot 4] At 00:09.000, cut to a moving three-quarter tracking view aimed deeper into the dock.
[9s-11s] The lead carrier turns and strides briskly into the dock with the same fan. Cadi flies ahead along the central approach, his red flame trailing with the airflow. Reveal the four fellow Creo Robots carrying a left memory module, a CPU plate, an SSD and an upper cooling component, respectively.
[11s-13s] Track behind and slightly above Cadi, opening the view toward the work arrangement of <Picture 4>. All five carriers are already moving toward separate mapped placement locations. Each transported component exists as one continuous piece of cargo; its receiving footprint on the platform stays empty until that piece is lowered into contact. The lead fan's footprint follows the position indicated by <Picture 5>. End with Cadi and the carriers still moving forward, camera rising gently.'''
B='''[Shot 1] A continuous rising tracking shot inside the same dock. Cadi <Picture 1> is already flying ahead; the five Creo Robots <Picture 2> are already striding toward their mapped placement locations. Preserve their forward momentum and stable cargo support from the previous motion.
[0s-2s] Follow Cadi deeper into the work bay, then begin a smooth upward crane. Reveal all five carriers in the spatial arrangement of <Picture 4>. The lead robot carries the same right-hand fan supported as in <Picture 3>. The other four carry the left memory module, CPU plate, SSD and upper cooling component. Their receiving footprints remain clear. Preserve the platform's orientation and the relative component positions.
[2s-4s] Continue rising while the carriers reach their respective receiving locations and align each component horizontally over its own footprint. Both hands remain under each load. Preserve a single continuous instance of every transported component, with coherent rigid geometry and steady scale. The other installed components stay fixed on the platform.
[4s-5s] In one closely coordinated placement wave, the left memory module contacts its receiving position first, the CPU plate follows, then the lead right-hand fan, the SSD and the upper cooling component. Complete all five placements within this one-second interval. Show a controlled final vertical descent, physical contact, subtle weight transfer and a short settling hold. Each piece now occupies its own correct position in the complete layout.
[5s-7s] With all five components resting securely, the robots unload their hands, open their grip, withdraw their forearms and step backward. Their hands separate visibly from the stationary components. The lead fan remains exactly at the right-hand footprint shown in <Picture 5>. The four fellow carriers continue to the platform's outer aisles, leaving the completed layout clearly visible.
[7s-9s] Reach a high, wide overhead view that holds the entire rectangular placement and both dock aisles inside frame. Cadi hovers above the layout as his non-solid flame flickers upward. Show the complete arrangement: the long rear strip, both fan housings, paired memory modules, CPU plate, SSD, cooling elements and surrounding connectors, all fixed in the reference positions established by <Picture 4>. All five carriers have empty hands and stand clear of the installed pieces.
[9s-11s] The camera follows Cadi in a smooth descending arc toward the installed right-hand fan. Preserve the same side of the platform and continuous orientation. Cadi's red-orange flame streams upward against the descent; the installed fan and every neighboring component remain motionless.
[11s-13s] Ease into the final composition of <Picture 5>: Cadi hovering beside the fully placed fan, warm-white eyes directed toward its housing, with a small approving gesture. The fan is already seated and stable throughout this arrival. Settle the camera and hold the composition while the flame tongues continue to flicker and dissipate. The completed placement is maintained through the end.'''
for tag,timeline,summary in [('a',A,'A 13-second sequence: Cadi snaps, the lead Creo Robot flexes, catches a falling giant fan, recovers its balance and carries it into the dock as four coworkers transport their own components.'),('b',B,'A 13-second continuation: five Creo carriers finish transporting and placing their components almost together, then withdraw; the camera follows Cadi upward over the complete layout and down beside the installed fan.')]:
 text=common.replace('{summary}',summary).replace('{timeline}',timeline);(p/f'seg09-{tag}-minimax-h3-prompt-v01.txt').write_text(text,encoding='utf-8');print(tag,len(text))
local={'project':copy.deepcopy(reg['project']),'assets':assets,'segments':[{'id':'seg09-'+tag,'scene':9,'seed':7901,'duration_seconds':13,'cast':list(assets),'prompt':f'segments/SEG-09/seg09-{tag}-minimax-h3-prompt-v01.txt'} for tag in ['a','b']]}
local['project']['frames_per_segment']='依實際節點13秒設定';(p/'cast-registry-v01.yaml').write_text(yaml.safe_dump(local,allow_unicode=True,sort_keys=False),encoding='utf-8')
manifest={'mode':'Ref2VA','source':'assets/blender/seg09-creo-dock-v06/creo-dock-animation-v06.blend','segments':{'a':13,'b':13},'seed':7901,'images':[{'picture':i,'slot':'ref_image_'+str(i-1),'asset':k,'file':v['file'],'role':v['role']} for i,(k,v) in enumerate(assets.items(),1)],'picture4_note':'v06第396幀動作狀態，另以拉遠機位重渲染以完整呈現布局；非原影片逐幀擷取。'}
(p/'reference-manifest-v01.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
