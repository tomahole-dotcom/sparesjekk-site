#!/usr/bin/env python3
import json, re, urllib.request
from html.parser import HTMLParser
from pathlib import Path
from datetime import date

SSB="https://data.ssb.no/api/v0/no/table/"
NB="https://www.norges-bank.no/tema/Statistikk/Styringsrente-daglig/Styringsgrente-manedlig/"
OUT=Path("data/rentegap-history.json")

def get_json(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)

def post_json(url, payload):
    req=urllib.request.Request(url,data=json.dumps(payload).encode(),headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def pick(meta, mode):
    q=[]
    for v in meta["variables"]:
        code=v["code"]; texts=v.get("valueTexts",[]); vals=v.get("values",[])
        label=v.get("text","").lower()
        if code.lower() in ("tid","time") or label=="måned":
            q.append({"code":code,"selection":{"filter":"all","values":["*"]}})
            continue
        if "utlånstype" in label:
            terms=["totale","pant","bolig"]
        elif "sektor" in label:
            terms=["hushold"]
        elif "binding" in label:
            terms=["totalt"]
        elif "statistikkvariabel" in label or "contents" in code.lower():
            terms=["renter"]
        else:
            terms=["totale"]
        chosen=None
        for val,txt in zip(vals,texts):
            low=txt.lower()
            if all(t in low for t in terms):
                chosen=val; break
        if not chosen:
            raise RuntimeError(f"Fant ikke {terms} for {v['text']}: {texts[:30]}")
        q.append({"code":code,"selection":{"filter":"item","values":[chosen]}})
    return q

def series(table, wanted):
    meta=get_json(SSB+table)
    payload={"query":pick(meta,wanted),"response":{"format":"json-stat2"}}
    d=post_json(SSB+table,payload)
    times=d["dimension"]["Tid"]["category"]["index"]
    if isinstance(times,dict):
        times=[x[0] for x in sorted(times.items(),key=lambda x:x[1])]
    vals=d["value"]
    return {t:float(v) for t,v in zip(times,vals) if v is not None}

class Table(HTMLParser):
    def __init__(self):
        super().__init__(); self.cell=False; self.row=[]; self.rows=[]
    def handle_starttag(self,tag,attrs):
        if tag=="tr": self.row=[]
        if tag in ("td","th"): self.cell=True
    def handle_endtag(self,tag):
        if tag in ("td","th"): self.cell=False
        if tag=="tr" and self.row: self.rows.append(self.row)
    def handle_data(self,data):
        if self.cell:
            s=" ".join(data.split())
            if s:
                if self.row: self.row[-1]+=" "+s
                else: self.row.append(s)
    def handle_startendtag(self,tag,attrs): pass

def policy_monthly():
    req=urllib.request.Request(NB,headers={"User-Agent":"Mozilla/5.0 (compatible; SparesjekkDataBot/1.0; +https://sparesjekk.no/)","Accept":"text/html,application/xhtml+xml"})\n    with urllib.request.urlopen(req,timeout=30) as r: html=r.read().decode("utf-8")
    p=Table(); p.feed(html)
    months={"januar":"01","februar":"02","mars":"03","april":"04","mai":"05","juni":"06","juli":"07","august":"08","september":"09","oktober":"10","november":"11","desember":"12"}
    out={}
    text=re.sub("<[^>]+>"," ",html)
    text=" ".join(text.split()).lower()
    for name,num in months.items():
        for m in re.finditer(rf"{name}\s+(20\d{{2}})\s+([0-9]+,[0-9]+)",text):
            out[f"{m.group(1)}M{num}"]=float(m.group(2).replace(",","."))
    return out

new=series("10748",[["totale","boliglån"],["hushold"]])
outstanding=series("10745",[["pant","bolig"],["hushold"]])
policy=policy_monthly()
periods=sorted(set(new)&set(outstanding)&set(policy))
rows=[]
for p in periods:
    rows.append({"period":p.replace("M","-"),"policy_rate_monthly_avg":policy[p],"new_mortgage_rate":new[p],"outstanding_mortgage_rate":outstanding[p],"new_gap_pp":round(new[p]-policy[p],2),"outstanding_gap_pp":round(outstanding[p]-policy[p],2)})
if len(rows)<100:
    raise RuntimeError(f"For kort historikk: {len(rows)} måneder")
doc={"name":"Sparesjekk Rentegap historikk","generated":date.today().isoformat(),"method":"Månedlig SSB-rente minus Norges Banks månedsgjennomsnitt for styringsrenten.","sources":{"ssb_new_mortgage":"10748","ssb_outstanding":"10745","norges_bank":"styringsrenten månedsgjennomsnitt"},"period_start":rows[0]["period"],"period_end":rows[-1]["period"],"observations":len(rows),"history":rows}
OUT.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"Skrev {len(rows)} måneder: {rows[0]['period']}–{rows[-1]['period']}")
