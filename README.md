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

### 3Blue1Brown（神经网络 / 注意力可视化）

- 官网：[3blue1brown.com](https://www.3blue1brown.com/)
- 神经网络专题：[3blue1brown.com/topics/neural-networks](https://www.3blue1brown.com/topics/neural-networks)
- B 站官方号（国内可看）：[space.bilibili.com/88461692](https://space.bilibili.com/88461692)
- 神经网络 4 集：
  - [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk)
  - [Gradient descent, how neural networks learn](https://www.youtube.com/watch?v=IHZwWFHWa-w)
  - [What is backpropagation really doing?](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
  - [Backpropagation calculus](https://www.youtube.com/watch?v=tIeHLnjs5U8)
- GPT / 注意力可视化 3 集：
  - [But what is a GPT? Visual intro to transformers](https://www.youtube.com/watch?v=wjZofJX0v4M)
  - [Attention in transformers, visually explained](https://www.youtube.com/watch?v=eMlx5fFNoYc)
  - [How might LLMs store facts](https://www.youtube.com/watch?v=9-Jl0dxWQs8)

### 其他

- Andrej Karpathy《Let's build GPT: from scratch》/ [nanoGPT](https://github.com/karpathy/nanoGPT)
- Jay Alammar《[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)》
- [Hugging Face Course](https://huggingface.co/learn)

## 目录结构

```
.
├── README.md
├── lessons/          # 学习笔记（markdown）
│   └── 01-self-attention.md
└── code/             # 配套代码
    └── self_attention.py
```
