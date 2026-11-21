"""
Lesson 01 — Self-Attention（自注意力）
《Attention Is All You Need》(2017) 核心组件之一。

依赖：torch  （pip install torch）
"""
import torch
import torch.nn.functional as F


def self_attention(X, Wq, Wk, Wv):
    """单头自注意力。

    Args:
        X  : [n, d_model]  输入序列（n 个 token，每个 d_model 维）
        Wq : [d_model, d_k] Query 权重
        Wk : [d_model, d_k] Key 权重
        Wv : [d_model, d_v] Value 权重

    Returns:
        out  : [n, d_v] 注意力输出
        attn : [n, n]   注意力权重矩阵（每行和为 1，可用来可视化）
    """
    Q = X @ Wq
    K = X @ Wk
    V = X @ Wv
    d_k = K.size(-1)

    scores = Q @ K.transpose(-2, -1) / (d_k ** 0.5)   # 缩放点积
    attn = F.softmax(scores, dim=-1)                   # 每行归一化
    out = attn @ V                                     # 加权求和
    return out, attn


if __name__ == "__main__":
    # 2 个 token，d_model = 4，用单位阵权重以便看清机制
    X = torch.tensor([[1.0, 0.0, 1.0, 0.0],
                      [0.0, 1.0, 0.0, 1.0]])
    I = torch.eye(4)

    out, attn = self_attention(X, I, I, I)

    print("注意力权重 attn =\n", attn)
    print("输出 out =\n", out)
