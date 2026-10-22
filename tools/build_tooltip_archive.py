from prepare_tooltip_release import OUT,WHEEL,ESSENTIALS,SOURCES,FILES,metadata
from pathlib import Path
import hashlib,json,zipfile,requests

RELEASE='https://github.com/antonsuslyaev/espeech-whisper-native-runtime/releases/download/qt-webengine-6.10.3-r1/'
notes='''# Qt WebEngine 6.10.3 runtime subset, Windows x64

Unmodified files extracted from the official PySide6-Addons 6.10.3 wheel,
plus its ICU data file from the official PySide6-Essentials 6.10.3 wheel.
Not an official Qt release. No application, models or recordings are included.

Qt WebEngine and PySide6 are redistributed under LGPL-3.0; see LGPL-3.0-only.txt
and GPL-3.0-only.txt (LGPL incorporates the GPL terms). Chromium and its bundled
components retain their own licenses, including LGPL-2.1 and BSD/MIT licenses.
See LICENSE.Chromium and upstream-notices.zip for verbatim source notices,
copyrights, COPYING/LICENSE/NOTICE/PATENTS files and attribution metadata.
The original source archives below also contain these notices in context.
The commercial alternative notice retained in upstream sources does not grant
a commercial Qt license; this distribution uses the open-source LGPL option.

Sources, unchanged upstream archives (same release download directory):
https://github.com/antonsuslyaev/espeech-whisper-native-runtime/releases/tag/qt-webengine-6.10.3-r1
- qtwebengine-everywhere-src-6.10.3.tar.xz (including Chromium)
- pyside-setup-everywhere-src-6.10.3.tar.xz (including binding generator source)
See provenance.json for exact URLs, sizes and SHA-256 values.

Upstreams:
https://code.qt.io/cgit/qt/qtwebengine.git/tag/?h=v6.10.3
https://code.qt.io/cgit/pyside/pyside-setup.git/tag/?h=v6.10.3
https://www.chromium.org/chromium-projects/
https://pypi.org/project/PySide6-Addons/6.10.3/
Licensing: https://doc.qt.io/qt-6.10/qtwebengine-licensing.html

Requirements: matching Qt/PySide6 6.10.3 Windows x64 base libraries, Shiboken6,
Python compatible with the cp39-abi3 wheel, and the appropriate Microsoft C++
runtime. These dependencies are provided by the host application, not this ZIP.
Only WebEngine Core/Widgets, their Python bindings, the helper, release data
files and en-US/ru locales are selected. Quick/QML bindings, debug data and
other language packs are omitted. Selected files are not patched or rebuilt.

Replacement/rebuilding: these are separate dynamically loaded DLL/PYD files.
Recipients may replace them with ABI-compatible modified versions; no license
restriction on debugging such library modifications is imposed by this package.
Build instructions and scripts are in the supplied sources. Use matching Qt
6.10.3 dependencies and the official Windows build prerequisites:
https://doc.qt.io/qt-6.10/qtwebengine-platform-notes.html
https://doc.qt.io/qtforpython-6.10/building_from_source/index.html
The host must permit replacement and preserve these notices. Package hashes
identify the official download, not a prohibition on local library modification.
'''
for name in ['LICENSE.Chromium','LICENSES/LGPL-2.0-or-later.txt']:
 r=requests.get('https://raw.githubusercontent.com/qt/qtwebengine/v6.10.3/'+name,timeout=30);r.raise_for_status()
 (OUT/name.rsplit('/',1)[-1]).write_bytes(r.content)

provenance={'version':'6.10.3','chromium':'134.0.6998.208','wheels':[dict(filename=n,url=b+n,size=s,sha256=h) for n,b,s,h in (WHEEL,ESSENTIALS)],
 'sources':[dict(filename=n,url=b+n,size=s,sha256=h,release_url=RELEASE+n) for n,b,s,h in SOURCES],
 'changes':'Selection only; all selected wheel members unchanged.', 'notices':metadata(OUT/'upstream-notices.zip')}
(OUT/'NOTICE.md').write_text(notes,encoding='utf-8')
(OUT/'provenance.json').write_text(json.dumps(provenance,indent=2),encoding='utf-8')
assert metadata(OUT/WHEEL[0])==dict(size=WHEEL[2],sha256=WHEEL[3])
assert metadata(OUT/ESSENTIALS[0])==dict(size=ESSENTIALS[2],sha256=ESSENTIALS[3])
files={}
archive=OUT/'qt-webengine.zip'
prefix='native/qt-webengine/'
with zipfile.ZipFile(OUT/WHEEL[0]) as src, zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as dst:
 def add(name,body):
  entry=zipfile.ZipInfo(prefix+name,date_time=(2026,10,22,0,0,0))
  entry.compress_type=zipfile.ZIP_DEFLATED
  entry.external_attr=0o100644<<16
  dst.writestr(entry,body)
  files[prefix+name]=dict(size=len(body),sha256=hashlib.sha256(body).hexdigest())
 for name in FILES:
  payload=src.read('PySide6/'+name)
  local=Path('.venv/Lib/site-packages/PySide6')/name
  assert metadata(local)==dict(size=len(payload),sha256=hashlib.sha256(payload).hexdigest()),name
  add('PySide6/'+name,payload)
 with zipfile.ZipFile(OUT/ESSENTIALS[0]) as essentials:
  name='PySide6/resources/icudtl.dat'
  payload=essentials.read(name)
  assert metadata(Path('.venv/Lib/site-packages')/name)==dict(size=len(payload),sha256=hashlib.sha256(payload).hexdigest())
  add(name,payload)
 for name in ['NOTICE.md','provenance.json','LGPL-3.0-only.txt','GPL-3.0-only.txt','LGPL-2.0-or-later.txt','LICENSE.Chromium','upstream-notices.zip']:
  add('licenses/'+name,(OUT/name).read_bytes())
info=metadata(archive)
filename='qt-webengine-6.10.3-win64-'+info['sha256'][:16]+'.zip'
archive.rename(OUT/filename)
manifest=dict(version=1,qt_version='6.10.3',archives=[dict(filename=filename,label='Qt WebEngine — карточки',url=RELEASE+filename,**info,files=files)])
(OUT/'tooltip-downloads.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'SHA256SUMS.txt').write_text(''.join(h+'  '+n+'\n' for n,b,s,h in SOURCES)+info['sha256']+'  '+filename+'\n',encoding='ascii')
print(json.dumps(dict(filename=filename,**info,unpacked=sum(x['size'] for x in files.values()),files=len(files))),flush=True)
