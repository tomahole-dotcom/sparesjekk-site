#!/usr/bin/env python3
from pathlib import Path
import subprocess
R=Path(__file__).resolve().parents[1]
out=R/"rendered"; out.mkdir(exist_ok=True)
W,H=1080,1920
# Four clean scene cards, rendered as SVG -> PNG -> short clips. No external assets.
scenes=[
("0,25 prosentpoeng","Hva betyr det i kroner?","0","3"),
("1 mill. ≈ 2 500 kr","2 mill. ≈ 5 000 kr\n4 mill. ≈ 10 000 kr","3","7"),
("Rentemøte 24. september","Styringsrente før møtet: 4,25 %","7","10"),
("Regn på ditt eget lån","sparesjekk.no","10","12"),
]
clips=[]
for i,(title,body,start,end) in enumerate(scenes,1):
    body_lines=body.split("\n")
    tspans="".join(f'<tspan x="540" dy="{0 if j==0 else 82}">{x}</tspan>' for j,x in enumerate(body_lines))
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">
<rect width="1080" height="1920" fill="#071b3b"/>
<circle cx="880" cy="210" r="260" fill="#0d4f9a" opacity=".55"/>
<circle cx="120" cy="1650" r="330" fill="#123f75" opacity=".55"/>
<text x="90" y="150" fill="#8fc7ff" font-family="Arial" font-size="44" font-weight="700">SPARESJEKK.NO</text>
<text x="540" y="690" text-anchor="middle" fill="white" font-family="Arial" font-size="86" font-weight="700">{title}</text>
<text x="540" y="890" text-anchor="middle" fill="#dcecff" font-family="Arial" font-size="55">{tspans}</text>
<rect x="180" y="1390" width="720" height="150" rx="75" fill="#ffffff"/>
<text x="540" y="1485" text-anchor="middle" fill="#071b3b" font-family="Arial" font-size="48" font-weight="700">Sjekk hva det betyr for deg</text>
<text x="540" y="1770" text-anchor="middle" fill="#9db7d8" font-family="Arial" font-size="30">Offisielle tall • ingen spådom om rentebeslutningen</text>
</svg>'''
    sf=out/f"scene-{i}.svg"; png=out/f"scene-{i}.png"; mp4=out/f"scene-{i}.mp4"
    sf.write_text(svg,encoding="utf-8")
    subprocess.run(["rsvg-convert","-w","1080","-h","1920",str(sf),"-o",str(png)],check=True)
    dur=str(int(end)-int(start))
    subprocess.run(["ffmpeg","-y","-loop","1","-i",str(png),"-t",dur,"-r","30",
                    "-vf","zoompan=z='min(zoom+0.0008,1.06)':d=1:s=1080x1920:fps=30,format=yuv420p",
                    "-c:v","libx264","-movflags","+faststart",str(mp4)],check=True)
    clips.append(mp4)
lst=out/"concat.txt"; lst.write_text("\n".join("file '"+p.name+"'" for p in clips),encoding="utf-8")
final=out/"rentemote-short-v2.mp4"
subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst.name,"-c","copy",final.name],cwd=out,check=True)
subprocess.run(["ffprobe","-v","error","-show_entries","stream=width,height,duration","-of","default=nw=1",final.name],cwd=out,check=True)
print(final)
