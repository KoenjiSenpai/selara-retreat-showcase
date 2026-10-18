"""Build six individually composed, reproducible, SVG illustration assets.
Every scene is drawn from different geometry (not a cropped/recolored master image).
Does not depend on a remote API. Requires Python 3.10+."""
from pathlib import Path
import math,random
A=Path(__file__).resolve().parents[1]/'public'/'assets'
A.mkdir(parents=True,exist_ok=True)

COL={'ink':'#143d32','pine':'#285c4b','sand':'#faedd6','gold':'#d6a46c','coral':'#c9856e','water':'#517f82','cream':'#fff6e6'}

def path(d,fill,opacity=1,stroke=None,sw=1): return f'<path d="{d}" fill="{fill}" opacity="{opacity}" '+(f'stroke="{stroke}" stroke-width="{sw}" ' if stroke else '')+'/>'
def rect(x,y,w,h,fill,rx=0,opacity=1):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" opacity="{opacity}"/>'
def circ(x,y,r,fill,op=1):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" opacity="{op}"/>'
def ellipse(x,y,rx,ry,color,op=1):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{color}" opacity="{op}"/>'

def leaf(x,y,s,ang,color):
 return f'<g transform="translate({x} {y}) rotate({ang}) scale({s})">'+path('M0 0 C38 -35 66 -40 101 -8 C64 11 37 19 0 0 Z',color)+path('M0 0 Q55 -2 95 -8','none',1,'#d6bd88',1.8)+'</g>'

def palm(x,y,s,lean=0,night=False):
 c='#152f2a' if night else '#285447';light='#244136' if night else '#39715a'
 p=f'<g transform="translate({x} {y}) scale({s})">'
 p+=path(f'M0 0 Q{lean*0.3+14} -170 {lean} -360 Q{lean+8} -370 {lean+19} -369 Q{lean+15} -220 24 0 Z',c)
 for a,sz in [(-166,.93),(-134,1.09),(-92,1.02),(-54,.97),(-19,.92),(14,.87),(53,.95),(84,1.06),(125,1.04),(158,.88)]:
  p+=leaf(lean,-365,sz,a,light if a%2 else c)
 p+='</g>'
 return p

def surf_sky(sunset=False, night=False,forest=False):
 if night:
  sky=['#122b36','#274557','#867c7d'];sea=['#304b5c','#2c5c61']
 elif sunset:
  sky=['#4b6571','#d2a28f','#f7c796'];sea=['#477f84','#2d5960']
 elif forest:
  sky=['#b9cfbc','#e0d9bb','#e9dfca'];sea=['#417875','#234f45']
 else:
  sky=['#779e9d','#b4c5ae','#f7d9ad'];sea=['#538f91','#346a75']
 return sky,sea

def start(kind,night=False,sunset=False,forest=False):
 sky,sea=surf_sky(sunset,night,forest)
 s=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800" role="img" aria-label="Original illustrated Selara concept scene">',
 f'<defs><linearGradient id="sky" x2=".25" y2="1"><stop stop-color="{sky[0]}"/><stop offset=".55" stop-color="{sky[1]}"/><stop offset="1" stop-color="{sky[2]}"/></linearGradient>',
 f'<linearGradient id="sea" x2="0" y2="1"><stop stop-color="{sea[0]}"/><stop offset="1" stop-color="{sea[1]}"/></linearGradient>',
 '<linearGradient id="wood" x2="0" y2="1"><stop stop-color="#8e7357"/><stop offset="1" stop-color="#4b392e"/></linearGradient>',
 '<linearGradient id="wall" x2="0" y2="1"><stop stop-color="#f4e8cb"/><stop offset="1" stop-color="#d7c7a7"/></linearGradient>',
 '<linearGradient id="leaf" x2="0" y2="1"><stop stop-color="#507967"/><stop offset="1" stop-color="#193d32"/></linearGradient>',
 '<linearGradient id="pool" x2="0" y2="1"><stop stop-color="#75aaa5"/><stop offset="1" stop-color="#316b6b"/></linearGradient>',
 '<linearGradient id="shadow" x2="0" y2="1"><stop stop-color="#000" stop-opacity=".04"/><stop offset="1" stop-color="#142e2b" stop-opacity=".46"/></linearGradient>',
 '<filter id="haze"><feGaussianBlur stdDeviation="19"/></filter><filter id="soft"><feGaussianBlur stdDeviation="4"/></filter>',
 '</defs>',rect(0,0,1200,800,'url(#sky)'),
 # backdrop translucent rays
 path('M775 0 L1050 0 L700 575 L610 570Z','#fff7d7',.12),
 circ(900 if not forest else 275,215 if not night else 115,81 if not night else 42,'#fae8c4',.9 if not night else .7),
 path('M0 470 Q150 348 294 439 T600 405 T880 438 T1200 384 L1200 610 L0 610Z','#496f69',.26),
 path('M0 535 Q190 454 345 505 T710 483 T1200 488 L1200 650 L0 650Z','#3b6764',.3),
 rect(0,535,1200,265,'url(#sea)')]
 if night:
  r=random.Random(17)
  for i in range(80):
   x=r.randint(30,1180);y=r.randint(20,395);s.append(circ(x,y,r.choice([1,1.5,2,2.8]),'#fff5dc',r.uniform(.3,.75)))
 for i in range(28):
  y=559+i*8;x=80+(i*43)%600
  s.append(path(f'M{x} {y} q70 -5 155 0','none',.15,'#fae3bd',2))
 return s

def ending(s):
 s.append(rect(0,0,1200,800,'url(#shadow)',0,.14))
 # thin editorial keyline with vignetting
 s.append('<rect x="18" y="18" width="1164" height="764" rx="3" fill="none" stroke="#fff7e6" stroke-width="2" opacity=".22"/>')
 s.append('</svg>')
 return '\n'.join(s)

def plants(s,seed,edge='both',low=760,colors=('#244e3b','#355f4b','#42705a')):
 r=random.Random(seed)
 for i in range(28):
  x=r.randint(-10,220) if i%2==0 else r.randint(980,1220)
  if edge=='left':x=r.randint(-10,280)
  if edge=='right':x=r.randint(930,1220)
  y=r.randint(low-210,low+80);a=r.choice([-75,-35,0,40,75]);sc=r.uniform(.35,.9)
  s.append(leaf(x,y,sc,a,r.choice(colors)))

def villa(s,ox=370,oy=267,scale=1,wide=False,lantern=True):
 s.append(f'<g transform="translate({ox} {oy}) scale({scale})">')
 # shadow behind
 s.append(ellipse(312,440,460,60,'#19382e',.22))
 s.append(path('M24 167 L614 167 L628 452 L20 452 Z','url(#wall)'))
 s.append(path('M-32 176 L302 -10 L672 176 L634 201 L303 45 L9 208Z','#4f3f32'))
 s.append(path('M-4 177 L308 17 L659 183','none',1,'#b28b64',14))
 s.append(rect(80,213,470,205,'#244239',4))
 s.append(rect(106,229,418,177,'#af7d55',0,.24))
 for x in [130,255,383,520]:
  s.append(rect(x,190,13,234,'#523d2a'))
 s.append(path('M80 224 H550 M80 311 H550','none',1,'#c6aa80',4))
 for x in [176,300,422]:
  s.append(rect(x,249,58,92,'#f2c88f',0,.45))
 s.append(path('M-40 430 L665 430 L750 505 L-140 505 Z','#ccb896'))
 s.append(path('M-95 472 L708 472','none',1,'#f4e5c8',8))
 if lantern:
  for x in (10,606):
   s.append(rect(x,398,18,32,'#e9bf75',3,.7));s.append(circ(x+9,414,24,'#ffbe67',.12))
 s.append('</g>')

def create_shore():
 s=start('shore',sunset=True)
 s+=[path('M0 660 Q230 622 415 684 T800 654 T1200 662 L1200 800 H0Z','#d1b58a'),path('M0 729 Q320 684 600 728 T1200 707','none',.7,'#fff3d7',8)]
 villa(s,412,194,.93)
 s.append(path('M300 585 L967 577 L1096 800 L117 800Z','#d8cab0'))
 s.append(path('M337 609 L943 604 L1030 788 L225 788Z','url(#pool)'))
 for i in range(14):
  y=618+i*12;s.append(path(f'M{329-i*7} {y} q210 -10 450 0','none',.24,'#f6f3db',2))
 s.append(palm(124,712,.83,50))
 plants(s,10,low=780)
 return ending(s)

def create_grove():
 s=start('grove',forest=True)
 s.append(path('M0 536 Q320 420 680 560 T1200 510 L1200 800 H0Z','#396e57'))
 s.append(path('M0 602 Q220 565 450 665 T975 618 T1200 621 L1200 800 H0Z','#2d5848'))
 villa(s,276,264,.78)
 s.append(path('M355 682 Q500 631 635 705 T1040 680 L1200 800 H240Z','#bb9a70'))
 s.append(palm(80,793,1.17,94));s.append(palm(1080,785,.98,-42));plants(s,22,low=820)
 s.append(ellipse(645,670,190,15,'#d9bf95',.12))
 return ending(s)

def create_horizon():
 s=start('horizon',sunset=True)
 s.append(path('M0 680 Q180 619 330 665 T730 645 T1200 645 L1200 800 H0Z','#c6ae8c'))
 villa(s,165,162,1.27)
 s.append(path('M145 684 L1060 684 L1190 790 L15 790 Z','#a28c74'))
 s.append(path('M151 692 L1020 692 L1140 778 L32 778Z','url(#pool)'))
 s.append(palm(1095,780,.66,-24));plants(s,35,'right',low=760)
 return ending(s)

def create_sail():
 s=start('sail',sunset=True)
 s.append(path('M0 640 Q278 555 502 632 T1200 609 L1200 800 H0Z','#366669',.56))
 # distant boat and mast main
 s.append(path('M385 630 L915 630 L851 700 L469 700Z','#2d4039'))
 s.append(path('M618 255 L618 629','none',1,'#f8e5c1',10))
 s.append(path('M603 277 L603 610 L349 610Z','#f9e9ce',.85))
 s.append(path('M638 301 L638 599 L871 597Z','#ead0aa',.82))
 s.append(path('M448 706 Q683 724 828 700','none',.6,'#f5bd7a',7))
 s.append(palm(95,815,.7,60));plants(s,88,'right')
 return ending(s)

def create_forest():
 s=start('forest',forest=True)
 s.append(path('M0 480 Q240 360 450 476 T850 420 T1200 476 L1200 800 H0Z','#356c56',.8))
 s.append(path('M0 570 Q240 480 510 570 T1200 510 L1200 800 H0Z','#235541'))
 s.append(path('M530 550 L684 550 L845 800 L325 800 Z','#ad946c'))
 s.append(path('M548 576 L655 576 L750 800 L406 800Z','#ddbf8b'))
 for x,y,sc,lean in [(90,820,1.35,85),(240,800,.9,50),(1020,815,1.2,-100),(1120,780,.9,-60)]:s.append(palm(x,y,sc,lean))
 plants(s,57,low=780)
 return ending(s)

def create_dining():
 s=start('dining',night=True)
 s.append(path('M0 610 Q300 573 550 615 T1200 600 L1200 800H0Z','#9e8b6e'))
 s.append(path('M-20 222 Q520 292 1220 194','none',.9,'#c69c72',3))
 for x,y in [(90,240),(245,257),(401,257),(559,257),(720,248),(885,229),(1040,207)]:
  s.append(path(f'M{x} {y} v22','none',1,'#bda57f',2));s.append(circ(x,y+25,8,'#ffcc83'));s.append(circ(x,y+25,20,'#ffcc83',.12))
 # dining pavilion / tables
 s.append(rect(175,468,890,37,'#634a39'))
 for x in (225,960):s.append(rect(x,506,18,210,'#5b493a'))
 s.append(path('M390 518 L810 518 L870 595 L330 595 Z','#cab191'))
 for x in (413,810):s.append(rect(x,592,14,110,'#614f3c'))
 for x in (480,710):
  s.append(rect(x,480,55,42,'#e7d3b3',9));s.append(rect(x+10,469,36,17,'#f5d7a8',7));s.append(circ(x+27,463,18,'#f9b96b',.2))
 s.append(circ(608,502,16,'#f5c68e'))
 s.append(palm(88,795,.75,34,True));s.append(palm(1110,780,.7,-32,True));plants(s,64,low=810,colors=('#1c493f','#215a4c','#315f50'))
 return ending(s)

SCENES={'shore-villa':create_shore,'grove-suite':create_grove,'horizon-residence':create_horizon,'sunset-sail':create_sail,'forest-walk':create_forest,'starlit-dining':create_dining}
for key,func in SCENES.items():
 p=A/f'{key}.svg';p.write_text(func(),encoding='utf-8'); print(f'{p.name}: {p.stat().st_size:,} bytes')

def create_morning():
 """Independently composed top-down still-life, not a recolor of the coastal scenes."""
 s=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800" role="img" aria-label="Original illustrated island breakfast still life">',
 '<defs><linearGradient id="table" x2="1" y2="1"><stop stop-color="#d9bb8f"/><stop offset="1" stop-color="#ac8a6c"/></linearGradient>',
 '<linearGradient id="paper" x2=".2" y2="1"><stop stop-color="#fff8e5"/><stop offset="1" stop-color="#e9d9b9"/></linearGradient></defs>',rect(0,0,1200,800,'url(#table)')]
 for i in range(16):
  y=i*53;s.append(path(f'M0 {y} Q600 {y-12} 1200 {y+5}','none',.1,'#513a2b',2))
 s.append(ellipse(700,378,325,310,'#705942',.22))
 s.append(circ(678,352,274,'#ead7b0'));s.append(circ(678,352,249,'#f9efdd'));s.append(circ(678,352,232,'#e4d6ba',.75))
 for a in range(0,360,36):
  x=678+174*math.cos(math.radians(a));y=352+174*math.sin(math.radians(a));s.append(circ(round(x),round(y),13,'#efe4ce'))
 for (x,y) in [(590,282),(710,287),(640,412),(780,390),(523,378)]:
  s.append(ellipse(x,y,69,43,'#d58654'));s.append(ellipse(x+6,y+4,54,29,'#efa963'))
  for dx in [-24,0,24]:s.append(circ(x+dx,y+3,3,'#fff0b6',.8))
 s.append(circ(805,478,44,'#4a7659'));s.append(circ(805,478,36,'#acd1a1'));s.append(circ(805,478,24,'#f0d69c'))
 # coffee
 s.append(ellipse(259,244,98,108,'#755643',.28));s.append(circ(251,230,97,'#f1e9da'));s.append(circ(251,230,73,'#a98c6b'));s.append(circ(251,230,62,'#5e4838'));s.append(ellipse(251,222,42,20,'#bf9a70',.3))
 s.append(path('M333 195 C420 163 430 296 333 279','none',1,'#f9ead2',18))
 # napkin and journal
 s.append('<g transform="rotate(-10 260 607)">'+rect(70,487,368,274,'#f9efdf',5)+rect(92,506,333,230,'url(#paper)',3))
 for y in range(550,724,31):s.append(path(f'M127 {y} h255','none',.42,'#aa9f86',2))
 s.append('</g>')
 s.append(path('M475 522 Q500 560 512 648','none',1,'#385546',8))
 s.append(leaf(473,525,.7,-27,'#3d7656'));s.append(leaf(487,555,.7,21,'#456e53'))
 # mini woven flower
 for i in range(7):
  ang=i*360/7;cx=1020+52*math.cos(math.radians(ang));cy=170+52*math.sin(math.radians(ang));s.append(ellipse(round(cx),round(cy),28,44,'#fbdfaf',.9))
 s.append(circ(1020,170,38,'#d99b63'))
 s.append('<rect x="18" y="18" width="1164" height="764" fill="none" stroke="#fff4de" stroke-width="3" opacity=".35"/>')
 s.append('</svg>')
 return '\n'.join(s)

p=A/'slow-mornings.svg';p.write_text(create_morning(),encoding='utf-8');print(f'{p.name}: {p.stat().st_size:,} bytes')
