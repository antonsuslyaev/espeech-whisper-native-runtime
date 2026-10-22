# ESpeech Whisper Native Runtime

Versioned model packages for local Russian speech synthesis, recognition and stress marking on native inference backends. Independent packaging project; not an official release of any upstream project.

This repository distributes **model assets and an optional Qt WebEngine runtime component**, with per-component licenses and source information. It does not include an application, speech engine executables, a Python environment, CUDA binaries, voice references or recordings. A compatible speech implementation and a user-supplied reference recording are required for synthesis.

## Published packages

| Package | Contents | Upstream license |
| --- | --- | --- |
| ESpeech + Vocos | ESpeech RL-V2 EMA weights converted to GGUF; F16 matrices and F32 small tensors; embedded Vocos vocoder and vocabulary | ESpeech Apache-2.0; Vocos MIT |
| Whisper Small | Multilingual Small in whisper.cpp format; current Q8_0 weights, previous FP16 release retained | HF release Apache-2.0; OpenAI also publishes Whisper under MIT |
| RUAccent | v1 dictionaries, tokenizers and ONNX models; turbo3.1 with FP16 embedding storage | MIT |

The archive and member hashes in [models.json](models.json) pin the exact files. [SHA256SUMS.txt](SHA256SUMS.txt) lists archive hashes. Each archive carries its license notices. Model precision/conversion changes are described in [NOTICE.md](NOTICE.md). A format conversion does not change an upstream license.

## Optional Qt WebEngine component

[Qt WebEngine 6.10.3 for Windows x64](https://github.com/antonsuslyaev/espeech-whisper-native-runtime/releases/tag/qt-webengine-6.10.3-r1) provides an independent HTML/CSS renderer: WebEngine Core/Widgets DLLs, PySide6 bindings, helper executable, resources and en-US/ru locales. The selected files are unmodified members of the official PySide6-Addons wheel, plus ICU data from PySide6-Essentials. Matching base Qt/PySide6 and Python are supplied by the host application.

Download: **99.4 MiB**, unpacked: **223.5 MiB**. Corresponding Qt WebEngine (including Chromium) and PySide source archives are downloadable from the same release, without authentication. They are not downloaded by the runtime installer.

See [component notice and replacement/build instructions](QT-WEBENGINE.md), [provenance](qt-webengine-provenance.json), [file manifest](tooltip-downloads.json) and [archive checksums](QT-SHA256SUMS.txt). Qt/PySide use the LGPL-3.0 option; Chromium retains its component licenses. Full upstream notice files accompany the runtime in `licenses/upstream-notices.zip`, and remain in context in the source archives.

## Model sources

- [ESpeech / ESpeech-TTS-1_RL-V2](https://huggingface.co/ESpeech/ESpeech-TTS-1_RL-V2), revision `f582b6e5897fe8a5835059405a8439d13bdf7684`.
- [Charactr / Vocos mel 24 kHz](https://huggingface.co/charactr/vocos-mel-24khz), revision `0feb3fdd929bcd6649e0e7c5a688cf7dd012ef21`; [Vocos implementation](https://github.com/gemelo-ai/vocos).
- [OpenAI / Whisper Small](https://huggingface.co/openai/whisper-small), revision `973afd24965f72e36ca33b3055d56a652f456b4d`; [Whisper implementation](https://github.com/openai/whisper).
- [RUAccent model system v1](https://huggingface.co/ruaccent/accentuator), revision `b78ae5ea1e62beaf138bed1865cd8c3b0b5ca855`; [RUAccent implementation](https://github.com/Den4ikAI/ruaccent).

## Native implementations used for preparation and validation

- [CrispASR](https://github.com/CrispStrobe/CrispASR), commit `46506786de68ef670faa7355c8fb76b2e24a93ab`: F5/Vocos conversion and native inference basis (MIT).
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp), commit `231638a0717b7822784297e5980965ffcec05810`: native Small inference (MIT).
- [ggml](https://github.com/ggml-org/ggml), commit `e2ae679a563014f46c546ce6c6448e8601e4dea6`: shared tensor backend (MIT).
- [F5-TTS](https://github.com/SWivid/F5-TTS): original architecture/reference implementation (MIT code). Its separately licensed base checkpoints are **not** distributed here; the synthesis checkpoint is the ESpeech release above.

The executable implementations are not included in these archives. NVIDIA libraries are obtained separately from [NVIDIA's official redistribution service](https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.8.1.json) and remain subject to NVIDIA's terms.

## License scope

See [licenses](licenses) for full notices and pinned model cards. The licenses apply per component, not as one blanket license for the repository. Redistribution is based on the upstream authors' stated grants; no trademark rights or endorsement are implied. Reference recordings are not supplied and must be obtained with appropriate rights.

## Whisper Small Q8_0

The current recognition package is [Whisper Small Q8_0](https://github.com/antonsuslyaev/espeech-whisper-native-runtime/releases/tag/whisper-small-q8-v1). Its archive, member hashes and source notices are in [whisper-small-q8.json](whisper-small-q8.json) and [WHISPER-Q8-NOTICE.txt](WHISPER-Q8-NOTICE.txt). Weights are quantized; intermediate arithmetic remains backend-dependent. The previous FP16 release is immutable and remains available.
