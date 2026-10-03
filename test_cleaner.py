from cleaner import clean_webpage_text, extract_chinese_sentences


def test_cleaning_webpage_text():
    original = "<div><h1>  Python  </h1><p>  正则  </p></div>"
    result = clean_webpage_text(original)
    assert "Python" in result
    assert "正则" in result
    assert "<" not in result
    assert ">" not in result


def test__extract_chinese_sentences():
    text = "Hello world. 今天天气不错。Python is great. 我喜欢编程。"
    result = extract_chinese_sentences(text)
    assert result == ["今天天气不错。", "我喜欢编程。"]


if __name__ == "__main__":
    test_cleaning_webpage_text()
    test__extract_chinese_sentences()
    print("所有测试通过")