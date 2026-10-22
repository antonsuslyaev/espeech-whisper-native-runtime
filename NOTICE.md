# Third-party notices and modifications

Prepared 2026-10-22. These packages are converted model assets, not original upstream releases.

## ESpeech RL-V2

Upstream: ESpeech / Den4ikAI, https://huggingface.co/ESpeech/ESpeech-TTS-1_RL-V2/tree/f582b6e5897fe8a5835059405a8439d13bdf7684

The pinned model card grants Apache-2.0. Retain licenses/Apache-2.0.txt and the source model card. No additional NOTICE file is present in that upstream model repository at the pinned revision.

Changes: select EMA inference tensors, discard training/optimizer state, convert matrices to F16 and retain small tensors as F32, rename tensors into the native F5 GGUF layout, embed vocabulary and the Vocos model below. No voice-specific fine-tuning, reference waveforms or conditioning embeddings are included.

Source checkpoint SHA-256: 2422df03cd4e939411edae06ab063b89340f70a6dee8cdeab812c4add1bdaa6c
Converted GGUF SHA-256: b141e530aae7bda98f80ae1f56d0aae8c8be568ea103c3e181de6c974f125043

## Vocos

Copyright (c) 2023 Charactr Inc. MIT; see licenses/Vocos-MIT.txt.
https://huggingface.co/charactr/vocos-mel-24khz/tree/0feb3fdd929bcd6649e0e7c5a688cf7dd012ef21
Changes: integrated into the synthesis GGUF, with tensor renaming and precision conversion. Source checkpoint SHA-256: 97ec976ad1fd67a33ab2682d29c0ac7df85234fae875aefcc5fb215681a91b2a

## Whisper Small

OpenAI, https://huggingface.co/openai/whisper-small/tree/973afd24965f72e36ca33b3055d56a652f456b4d
The pinned Hugging Face model card declares Apache-2.0. Preserve that license and card. OpenAI's Whisper repository also grants MIT; its copyright and MIT notice are included in licenses/Whisper-MIT.txt.
Changes: FP32 tensors converted to FP16 and repacked into whisper.cpp's binary format, retaining the multilingual vocabulary. No fine-tuning.
Source safetensors SHA-256: 1d7734884874f1a1513ed9aa760a4f8e97aaa02fd6d93a3a85d27b2ae9ca596b
Converted binary SHA-256: 95b243cd2f8032a6a69ef43a1186ae2cafc333eb50e0ac38db1c787ea0e83784

## RUAccent v1

Copyright 2026 Denis Petrov. MIT; see licenses/RUAccent-MIT.txt.
https://huggingface.co/ruaccent/accentuator/tree/b78ae5ea1e62beaf138bed1865cd8c3b0b5ca855
The pinned model card explicitly applies MIT to the entire v1 system.
Changes: selected the turbo3.1 inference subset; stored its embedding table in FP16 and inserted conversion back to FP32 after lookup. Remaining model/tokenizer/dictionary files are unchanged upstream files. No custom vocabulary or user dictionary was added.

Native project links and pinned versions appear in README.md. Each project retains its own license; no executable code from those projects is distributed in these model archives.


## ESpeech attention/FFN Q8_0 derivative

The conversion descriptions above record the original models-v1 assets. The current synthesis derivative additionally quantizes 132 attention/FFN matrices to Q8_0. See [ESPEECH-Q8-NOTICE.txt](ESPEECH-Q8-NOTICE.txt) for exact hashes, modifications, sources and retained Apache-2.0/MIT obligations. Original release assets are unchanged.
