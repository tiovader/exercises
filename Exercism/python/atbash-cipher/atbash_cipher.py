import re
from string import ascii_lowercase
from functools import partial
SECRET = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def encode(text: str, decode=False) -> str:
    def wrap(): return ' '.join(re.findall(r'.{,5}', text)).strip()
    text = re.sub(r'[^a-z0-9]', '', text.lower().translate(SECRET))

    return text if decode else wrap()


decode = partial(encode, decode=True)
