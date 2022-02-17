def append(list1, list2): return [*list1, *list2]
def concat(lists): return foldl(append, lists, [])
def filter(function, list): return [item for item in list if function(item)]
def length(list): return foldl(lambda x, y: x+1, list, 0)
def map(function, list): return [function(item) for item in list]
def foldr(*args): return foldl(*args, right=True)
def reverse(list): return [list[i] for i in range(length(list) -1, -1, -1)]


def foldl(function, list, accumulate=0, *, right=False):
    def helper(*args): return reverse(args) if right else args

    for item in helper(*list):
        accumulate = function(*helper(accumulate, item))

    return accumulate
