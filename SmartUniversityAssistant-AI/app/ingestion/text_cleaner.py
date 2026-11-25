
import re


def clean_text(text: str) -> str:
    """
    Clean extracted document text while preserving its meaning.
    """

    if not text:
        return ""

    # Normalize Windows and Unix line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove null characters
    text = text.replace("\x00", "")

    # Remove excessive spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove spaces around line breaks
    text = re.sub(r" *\n *", "\n", text)

    # Reduce excessive consecutive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
