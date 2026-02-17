from src.ioc_utils import normalize_defang, extract_urls

def test_normalize_defang():
    assert normalize_defang("hxxps://a[.]b/x") == "https://a.b/x"

def test_extract_urls():
    urls = extract_urls("See hxxp://example[.]com/test")
    assert urls == ["http://example.com/test"]
