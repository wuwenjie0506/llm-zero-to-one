# LLM Zero to One

从零开始学习大语言模型（LLM）的学习笔记与配套代码。

> 起点：《Attention Is All You Need》(2017)

## 学习路线

```
数学/框架地基 → Transformer 核心 → GPT 生成式模型 → 预训练/Scaling
→ 对齐(SFT/RLHF) → 推理与工程优化 → 应用与前沿(RAG/Agent/多模态)
```

## 目录（进度）

| # | 主题 | 状态 |
|---|---|---|
| 01 | Self-Attention（自注意力） | ✅ 已记录 |
| 02 | Multi-Head Attention + Positional Encoding | ⏳ 计划中 |
| 03 | 完整 Transformer Block | ⏳ 计划中 |
| 04 | GPT 与自回归生成 | ⏳ 计划中 |
| 05 | Tokenizer（BPE）与训练数据 | ⏳ 计划中 |
| 06 | 预训练与 Scaling Laws | ⏳ 计划中 |
| 07 | 对齐：SFT / RLHF / DPO | ⏳ 计划中 |
| 08 | 推理优化：KV Cache / 量化 | ⏳ 计划中 |
| 09 | 应用：RAG / Agent | ⏳ 计划中 |

## 必读论文清单

1. *Attention Is All You Need*（2017）
2. *GPT-1 / GPT-2 / GPT-3*
3. *Scaling Laws*（Kaplan）+ *Chinchilla*
4. *InstructGPT*（RLHF）+ *DPO*
5. *LLaMA*（RoPE 旋转位置编码）
6. *FlashAttention*、*LoRA*

## 推荐资源

- Andrej Karpathy《Let's build GPT: from scratch》/ `nanoGPT`
- Jay Alammar《The Illustrated Transformer》
- 3Blue1Brown 神经网络 / 注意力可视化
- Hugging Face Course

## 目录结构

```
.
├── README.md
├── lessons/          # 学习笔记（markdown）
│   └── 01-self-attention.md
└── code/             # 配套代码
    └── self_attention.py
```
