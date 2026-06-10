---
language:
- en
- hi
- te
- ta
- kn
- mr
- bn
- gu
- pa
license: apache-2.0
library_name: mlx
tags:
- agriculture
- indian-farming
- fine-tuned
- lora
- qwen3
- mlx
- crops
- farming
- india
base_model: Qwen/Qwen3-4B
datasets:
- KissanAI/india-climate-qa-synth-v1
pipeline_tag: text-generation
---

<div align="center">

<img src="https://cdn-avatars.huggingface.co/v1/production/uploads/67a527986b39b58ea8528fb0/i_tvZOmu3un4ABR8Z0Fyp.png" alt="IlaAI Logo" width="120"/>

# IlaAI-v1 🌱
### Earth · Crop · Intelligence

**An open-source Agricultural AI for Bharat's Farmers**

[![HuggingFace](https://img.shields.io/badge/HuggingFace-Ila--AI-yellow?logo=huggingface)](https://huggingface.co/Ila-AI)
[![GitHub](https://img.shields.io/badge/GitHub-IlaAI-green?logo=github)](https://github.com/IlaAI)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE)
[![Base Model](https://img.shields.io/badge/Base-Qwen3--4B-purple)]()
[![Val Loss](https://img.shields.io/badge/Val%20Loss-0.695-brightgreen)]()
</div>

---

## 🌾 About IlaAI

**IlaAI** (इला — Sanskrit for *"the earth that gives"*) is an open-source LLM fine-tuned specifically for Indian agriculture. Built on **Qwen3-4B** and trained on **96,000+ Indian agriculture Q&A pairs**, IlaAI helps farmers and developers get accurate, practical farming advice.

> "For the hands that feed a billion 🌾"

---

## ✨ Capabilities

- 🌾 iagnosis** — symptoms, causes, treatments
- 💊 **Pesticide & Fertilizer Advice** — what to use, how much, when
- 🌦️ **Weather-based Advisory** — sowing, irrigation, harvest timing
- t Schemes** — eligibility, documents, how to apply
- 📈 **Market Price Guidance** — mandi prices, sell/hold advice
- 🐛 **Pest Management** — detection and treatment
- 🌱 **Soil Health** — soil types, nutrients, improvement tips

---

## 🚀 Quick Start

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load("Ila-AI/IlaAI-v1")

messages = [
    {"rolontent": "You are IlaAI, an expert agricultural assistant for Indian farmers. Answer clearly and helpfully."},
    {"role": "user", "content": "My wheat crop has yellow spots on leaves. What should I do?"}
]

text = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=False
)

sampler = make_sampler(temp=0.7, top_p=0.9)
response = generate(model, tokenizer, prompt=text, max_tokens=300, sampler=sampler, verbose=True)
```

---

## 📊 Training Details

| Detail | Value |
|--------|-------|
| Base Model | Qwen3-4B (4-bit quantized) |
| Framework | MLX LoRA |
| Hardware | Apple M4 Mac Mini (24GB) |
| Dataset | KissanAI/india-climate-qa-synth-v1 |
| Training rows | 92,060 |
| Validation rows | 4,845 |
| Training iters | 5,000 |
| LoRA rank | 8 |
| Final Val Loss | **0.695** |
| Peak Memory | 3.894 GB |

---

## ⚠️ Limitations

- **Best performance in E** — Hindi and other Indian languages are supported but quality varies
- **Text only** — does not process images (vision model coming in v2)
- **v1 release** — multilingual improvement planned for v2

---

## 🗺️ Roadmap

### ✅ Phase 1 — Foundation (Current)
- [x] Organization setup (GitHub + HuggingFace)
- [x] Dataset curation (96K rows)
- [x] IlaAI-v1 — English agriculture advisory
- [x] Published on HuggingFace

### 🔄 Phase 2 — Multilingual (Coming Soon)
- [ ] Add Hindi, Telugu, Tamil, Kannada, Marathi, Bengali, Gujarati, Punjabi datasets
- [ ] Fine-tune IlaAI-v2 on 22+ Indian languages
- [ ] Improve response quality across all languages
- [ ] Release IlaAI-v2 on HuggingFace

### 👁️ Phase 3 — Vision (Coming Soon)
- [ ] Fine-tune vision model on Indian crop disease images
- [ ] Support all major Indian crops — Rice, Wheat, Cotton, Sugarcane, Pulses
- [ ] Release IlaAI-Vision on HuggingFace
- [ ] Combine text + vision into one unified model

### 📱 Phase 4 — Mobile App (Coming Soon)
- [ ] IlaAI Android app — free, forever
- [ ] IlaAI iOS app — free, forever
- [ ] On-device inference (no internet needed)
- [ ] Voice input in Indian languages
- [ ] Available on Play Store & App Store

### 🌐 Phase 5 — Community (Coming Soon)
- [ ] Open dataset contributions from farmers
- [ ] Regional crop data by state
- [ ] API for developers to build on IlaAI
- [ ] WhatsApp bot integration

---

## 📜 License

Apache 2.0 — free to use, fine-tune, and build upon.

---

## 🙏 Acknowledgements

- [Kface.co/KissanAI) for open-sourcing Dhenu models and datasets
- [Qwen Team](https://huggingface.co/Qwen) for Qwen3 base models
- [Apple MLX Team](https://github.com/ml-explore/mlx) for MLX framework
- Every Indian farmer who inspired this project 🌾

---

<div align="center">
  <b>For the hands that feed a billion 🌾</b><br/>
  <a href="https://huggingface.co/Ila-AI">HuggingFace</a> · <a href="https://github.com/IlaAI">GitHub</a>
</div>
