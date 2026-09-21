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
params += [("sort[Stat.datetime]","desc"),("limit",10)]
conv=call("Affiliate_Report","getConversions",params)
print("CONVERSIONS_ACCESS:", "OK" if conv["ok"] else "FAILED", "HTTP",conv.get("http"))
if conv["ok"]:
    data=conv.get("data")
    rows=data if isinstance(data,list) else (list(data.values()) if isinstance(data,dict) else [])
    print("CONVERSION_ROWS_RETURNED:",len(rows))
    # Only non-sensitive commercial metadata; never emit IP/user-agent/referrer.
    safe=[]
    for row in rows[:10]:
        if not isinstance(row,dict): continue
        safe.append({k:v for k,v in row.items() if k in fields or k in ("Offer","Goal","Stat")})
    print("CONVERSION_SAMPLE:",json.dumps(safe,ensure_ascii=False,default=str)[:6000])
else:
    print("CONVERSION_ERROR:",conv.get("errorMessage") or conv.get("errors") or conv.get("error"))
