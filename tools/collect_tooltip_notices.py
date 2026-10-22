from prepare_tooltip_release import OUT,SOURCES,metadata
import json,tarfile,zipfile
from pathlib import PurePosixPath

out=OUT/'upstream-notices.zip'
rows={}
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for name,base,size,sha in SOURCES:
  assert metadata(OUT/name)==dict(size=size,sha256=sha)
  count=0
  with tarfile.open(OUT/name,'r|xz') as t:
   for member in t:
    p=PurePosixPath(member.name)
    leaf=p.name.upper()
    selected=('LICENSES' in p.parts or leaf.startswith(('LICENSE','LICENCE','COPYING','NOTICE','COPYRIGHT','PATENTS')) or leaf in ('README.CHROMIUM','QT_ATTRIBUTION.JSON'))
    if not selected or not member.isfile():continue
    if p.is_absolute() or '..' in p.parts or member.size>20*1024**2:raise RuntimeError(member.name)
    payload=t.extractfile(member).read()
    z.writestr('licenses/upstream/'+member.name,payload)
    count+=1
  rows[name]=count
  print(name,count,flush=True)
print(metadata(out),flush=True)
(OUT/'notices-audit.json').write_text(json.dumps(rows,indent=2))
