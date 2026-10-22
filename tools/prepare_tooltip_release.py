import hashlib, json, shutil, sys, tarfile, zipfile
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'public-tooltip-release'
OUT.mkdir(exist_ok=True)
SOURCES = [
 ('qtwebengine-everywhere-src-6.10.3.tar.xz', 'https://download.qt.io/official_releases/qt/6.10/6.10.3/submodules/', 881406300, '07c95f81d64391b3dd5b0edce7fc7eb2e8d39844e4904f82ae53f5533f4cf043'),
 ('pyside-setup-everywhere-src-6.10.3.tar.xz', 'https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-6.10.3-src/', 17900952, '2c7462fe0cecb5b8ac0a3d92014b8d0b88bd4d9f8646709dab5286d9416f45bc'),
]
WHEEL = ('pyside6_addons-6.10.3-cp39-abi3-win_amd64.whl', 'https://files.pythonhosted.org/packages/2c/5d/28dc9b8c926c86530c42cab4ed4f1bc43f025da8b7d8a39d3e18f8a937f3/', 164743124, 'b465b38d1ec3476a9197441fe6a62a1fac97c45a8094f11c2d7e318aee1e3fb3')
ESSENTIALS = ('pyside6_essentials-6.10.3-cp39-abi3-win_amd64.whl', 'https://files.pythonhosted.org/packages/bf/11/7cfcfc74213b8e33aecef6fa05dcedf45e65385155f07486a514a9777b0d/', 74610897, '051a70e2df79cf1c012a208ad82a98e8de23ca7fe3b0f3344d07152d15705b59')
FILES = ['Qt6WebEngineCore.dll', 'Qt6WebEngineWidgets.dll', 'QtWebEngineCore.pyd', 'QtWebEngineWidgets.pyd', 'QtWebEngineProcess.exe',
 'resources/qtwebengine_resources.pak', 'resources/qtwebengine_resources_100p.pak', 'resources/qtwebengine_resources_200p.pak', 'resources/qtwebengine_devtools_resources.pak', 'resources/v8_context_snapshot.bin',
 'translations/qtwebengine_locales/en-US.pak', 'translations/qtwebengine_locales/ru.pak']

def metadata(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  while b:=f.read(2*1024**2): h.update(b)
 return dict(size=path.stat().st_size, sha256=h.hexdigest())

def download(row):
 name,base,size,sha=row
 p=OUT/name
 if p.exists() and metadata(p)==dict(size=size,sha256=sha):return p
 if shutil.disk_usage(OUT).free-size < 10*1024**3:raise RuntimeError('10 GiB reserve')
 with requests.get(base+name,stream=True,timeout=(20,60)) as r:
  r.raise_for_status()
  with p.open('wb') as f:
   for b in r.iter_content(2*1024**2):
    if shutil.disk_usage(OUT).free-len(b)<10*1024**3:raise RuntimeError('10 GiB reserve')
    f.write(b)
 if metadata(p)!=dict(size=size,sha256=sha):raise RuntimeError('Checksum mismatch: '+name)
 print('Verified',name,size,flush=True)
 return p

if __name__=='__main__':
 if sys.argv[1]=='wheel':download(WHEEL)
 elif sys.argv[1]=='essentials':download(ESSENTIALS)
 elif sys.argv[1]=='sources':
  for row in SOURCES:download(row)
