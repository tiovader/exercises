OCR = {' _ | ||_|   ': '0', '     |  |   ': '1', ' _  _||_    ': '2',
       ' _  _| _|   ': '3', '   |_|  |   ': '4', ' _ |_  _|   ': '5',
       ' _ |_ |_|   ': '6', ' _   |  |   ': '7', ' _ |_||_|   ': '8',
       ' _ |_| _|   ': '9'
       }
CONCAT = ''.join
def formatter(ocr, default='?'): return OCR.get(ocr, default)


def __get_num(raw_num):
    columns = tuple(zip(*raw_num))
    yield from \
        (formatter(''.join(CONCAT(line) for line in zip(*columns[i:i+3])))
         for i in range(0, len(columns), 3))


def convert(grid: list[str]) -> str:
    if not (len(grid) % 4 == 0 and all(len(i) % 3 == 0 for i in grid)):
        raise ValueError('Invalid row lenght for input.')
    nums = (grid[n:n+4] for n in range(0, len(grid), 4))

    return ','.join((CONCAT(__get_num(i)) for i in nums))
