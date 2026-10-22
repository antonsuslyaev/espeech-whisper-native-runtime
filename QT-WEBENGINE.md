# Qt WebEngine 6.10.3 runtime subset, Windows x64

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

## Repackaging the unchanged upstream binaries

From this repository root, create `.venv` with Python on Windows x64 and install
`PySide6==6.10.3` and `requests`. Then run these scripts using that interpreter:

```
python tools/prepare_tooltip_release.py wheel
python tools/prepare_tooltip_release.py essentials
python tools/prepare_tooltip_release.py sources
python tools/collect_tooltip_notices.py
python tools/build_tooltip_archive.py
```

They check upstream SHA-256 values, select explicit wheel members, collect
verbatim source notices and produce `tools/public-tooltip-release`. The local
PySide6 files are compared byte for byte with the official wheels. This process
repackages vendor binaries; it does not claim a bit-identical compiler rebuild.

For an external helper executable, Windows requires the matching base Qt DLLs
next to it. A host may use NTFS hardlinks to its existing Qt installation,
avoiding extra copies of the shared libraries. These base libraries are not
included in this archive; their distribution remains the host's responsibility.
