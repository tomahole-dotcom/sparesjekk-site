#!/usr/bin/env python3
"""Read-only Axo/TUNE Affiliate API probe. Never prints API key."""
import json, os, sys, urllib.parse, urllib.request, urllib.error

key=os.environ.get("AXO_TUNE_API_KEY","").strip()
network=os.environ.get("AXO_TUNE_NETWORK_ID","axofinansno").strip()
if not key:
    raise SystemExit("AXO_TUNE_API_KEY missing")

base=f"https://{network}.api.hasoffers.com/Apiv3/json"

def call(target,method,params=None):
    q={"Target":target,"Method":method,"api_key":key}
    if params: q.update(params)
    url=base+"?"+urllib.parse.urlencode(q,doseq=True)
    req=urllib.request.Request(url,headers={"User-Agent":"Sparesjekk-Axo-ReadOnly-Probe/1.0"})
    try:
        with urllib.request.urlopen(req,timeout=25) as r:
            data=json.load(r)
    except urllib.error.HTTPError as e:
        body=e.read().decode("utf-8","replace")[:1000]
        return {"ok":False,"http":e.code,"error":body}
    resp=data.get("response",{})
    return {"ok":resp.get("status")==1,"http":resp.get("httpStatus"),"errors":resp.get("errors"),"errorMessage":resp.get("errorMessage"),"data":resp.get("data")}

acct=call("Affiliate_Affiliate","getAccountManager")
print("AUTH:", "OK" if acct["ok"] else "FAILED", "HTTP",acct.get("http"))
if not acct["ok"]:
    print("ERROR:",acct.get("errorMessage") or acct.get("errors") or acct.get("error"))
    sys.exit(2)

fields=["Offer.name","Goal.name","Stat.datetime","Stat.conversion_status","Stat.payout","Stat.approved_payout","Stat.currency","Stat.affiliate_info1","Stat.affiliate_info2","Stat.source","Stat.ad_id"]
params=[]
for x in fields: params.append(("fields[]",x))
params += [("filters[Stat.datetime][conditional]","GREATER_THAN_OR_EQUAL_TO"),("filters[Stat.datetime][values]","2026-09-01 00:00:00"),("sort[Stat.datetime]","desc"),("limit",10)]
conv=call("Affiliate_Report","getConversions",params)
print("CONVERSIONS_ACCESS:", "OK" if conv["ok"] else "FAILED", "HTTP",conv.get("http"))
if conv["ok"]:
    data=conv.get("data")
    rows=data if isinstance(data,list) else (list(data.values()) if isinstance(data,dict) else [])
    print("CONVERSION_ROWS_RETURNED:",len(rows))
    # Inspect only schema + explicitly requested commercial fields. Never emit PII/referrer/IP.
    def schema(v,prefix=""):
        out=[]
        if isinstance(v,dict):
            for k,val in v.items():
                path=f"{prefix}.{k}" if prefix else k
                out.append(path)
                if isinstance(val,(dict,list)): out.extend(schema(val,path))
        elif isinstance(v,list) and v:
            out.extend(schema(v[0],prefix+"[]"))
        return out
    if rows:
        print("ROW_SCHEMA:",json.dumps(sorted(set(schema(rows[0]))),ensure_ascii=False))
    safe=[]
    allowed_leaf={"name","datetime","conversion_status","payout","approved_payout","currency","affiliate_info1","affiliate_info2","source","ad_id"}
    for row in rows[:10]:
        if not isinstance(row,dict): continue
        z={}
        for k,val in row.items():
            if k in ("Offer","Goal","Stat") and isinstance(val,dict):
                z[k]={kk:vv for kk,vv in val.items() if kk in allowed_leaf}
            elif k in allowed_leaf:
                z[k]=val
        safe.append(z)
    print("COMMERCIAL_SAMPLE:",json.dumps(safe,ensure_ascii=False,default=str)[:6000])
