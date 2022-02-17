import re
BRACKETS = '{}\n[]\n()'.splitlines()
pattern = re.compile(r'[^{}[\]()]')


def is_paired(text: str) -> bool:
    text = pattern.sub('', text)

    while (p := next((b for b in BRACKETS if b in text), False)):
        text = text.replace(p, '')
    return not text
