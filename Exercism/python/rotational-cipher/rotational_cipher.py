from string import ascii_lowercase as lower, ascii_uppercase as upper


def rotate(text, key):
    def encrypt(c):
        n = 97 if c in lower else 65 if c in upper else None
        return c if not n else chr((ord(c) % n + key) % 26 + n)

    return ''.join(encrypt(c) for c in text)
