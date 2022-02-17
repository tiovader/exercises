from itertools import zip_longest as zip_


def transpose(rows: str):
    rows = rows.replace(' ', '¶').splitlines()
    return '\n'.join((''.join(i).rstrip().replace('¶', ' ')
                      for i in zip_(*rows, fillvalue=' ')))
