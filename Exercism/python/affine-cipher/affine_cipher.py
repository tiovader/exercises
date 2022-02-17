from math import gcd


def encode(_in: str, a: int, b: int, decode=False) -> str:
    if gcd(a, 26) > 1:
        raise ValueError(f'a({a}) and m(26) must be coprime.')

    text = filter(str.isalnum, _in.lower())
    secret = (lambda c: chr((a * (ord(c) % 97) + b) % 26 + 97),
              lambda c: chr((pow(a, -1, 26) * (ord(c) % 97 - b))
                            % 26 + 97))[decode]

    out = ''.join((i, secret(i))[i.isalpha()] for i in text)
    r = ((0, len(out), 5), (0, 0))[decode]

    return ' '.join(out[i: i + 5] for i in range(*r)) or out


def decode(*args): return encode(*args, decode=True)
