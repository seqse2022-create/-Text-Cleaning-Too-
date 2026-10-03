"""
文本清洗小工具

提供两个功能：
1. 清洗网页文本：去掉 HTML 标签、多余空白
2. 提取中文句子：从混杂文本中提取以中文标点结尾的句子
"""

import re


def clean_webpage_text(原始文本: str) -> str:
    """
    清洗网页文本。

    步骤：
    1. 去掉 HTML 标签
    2. 多个连续空格 → 一个空格
    3. 去掉行首行尾空白
    4. 去掉空行
    5. 去掉整体首尾空白

    参数：
        原始文本：带 HTML 标签的文本

    返回：
        清洗后的纯文本
    """
    text = re.sub(r"<[^>]+>", "", 原始文本)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"^[ \t]+|[ \t]+$", "", text, flags=re.M)
    text = re.sub(r"\n+", "\n", text)
    text = text.strip()
    return text


def extract_chinese_sentences(文本: str) -> list[str]:
    """
    提取中文句子。

    要求：
    - 以中文标点（。！？）结尾
    - 句子主体为中文

    参数：
        文本：中英文混杂的文本

    返回：
        中文句子列表
    """
    return re.findall(r"[\u4e00-\u9fa5]+[。！？]", 文本)


if __name__ == "__main__":
    # 测试 1：清洗网页文本
    original = "<div><h1>  Python 正则  </h1><p>  多练习  </p></div>"
    print("清洗前:", original)
    print("清洗后:", clean_webpage_text(original))

    # 测试 2：提取中文句子
    mixed = "Hello world. 今天天气不错。Python is great. 我喜欢编程。"
    print("中文句子:", extract_chinese_sentences(mixed))