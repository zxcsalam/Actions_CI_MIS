import re

def normalize_defang(text: str) -> str:
    """Учебная нормализация defang."""
    return (
        text.replace("hxxps://", "https://")
            .replace("hxxp://", "http://")
            .replace("[.]", ".")
    )

_URL_RE = re.compile(r"\bhttps?://[^\s'\"<>]+")


def extract_urls(text: str) -> list[str]:
    text = normalize_defang(text)
    return _URL_RE.findall(text)
