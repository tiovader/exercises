from typing import Iterable

def flatten(iterable):
    def unpack(iterable):
        for item in filter(lambda x: x is not None, iterable):
            if isinstance(item, Iterable):
                yield from unpack(item)
            else:
                yield item
                
    return list(unpack(iterable))
