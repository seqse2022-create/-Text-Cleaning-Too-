# 文本清洗小工具

一个 Python 文本清洗工具，提供两个功能：

1. **清洗网页文本**：去掉 HTML 标签、多余空白
2. **提取中文句子**：从混杂文本中提取以中文标点结尾的句子

## 环境

- Python 3.8+
- 无第三方依赖

## 功能一：清洗网页文本

去掉 HTML 标签、多余空白、空行。

```python
from cleaner import 清洗网页文本

原始 = "<div><h1>  Python 正则  </h1><p>  多练习  </p></div>"
print(清洗网页文本(原始))
# 输出：
# Python 正则
# 多练习
```

## 功能二：提取中文句子

从混杂文本中提取以中文标点（。！？）结尾的句子。

```python
from cleaner import 提取中文句子

文本 = "Hello world. 今天天气不错。Python is great. 我喜欢编程。"
print(提取中文句子(文本))
# 输出：['今天天气不错。', '我喜欢编程。']
```

## 运行测试

```bash
python test_cleaner.py
```

预期输出：

```
所有测试通过
```

## 项目结构

```
文本清洗小工具/
├── cleaner.py          # 核心代码
├── test_cleaner.py     # 测试代码
├── README.md           # 项目说明
└── 原始网页.txt        # 测试数据
```

## 作者

GitHub: [cu]