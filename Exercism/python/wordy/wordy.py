import re
from operator import add, sub, mul, floordiv as div
OPS = {'plus': add, 'minus': sub, 'multiplied by': mul, 'divided by': div}


def answer(txt: str):
    try:
        if m := re.match(r'What is ((-?\d+) (%s) (-?\d+))' % '|'.join(OPS), txt):
            group, i, op, j = m.groups()
            res = str(OPS[op](*map(int, (i, j))))
            return answer(re.sub(group, res, txt, 1))
        return int(txt[8:-1])
    except Exception:
        raise ValueError('Can\'t handle operation.')
