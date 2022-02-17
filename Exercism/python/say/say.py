from inflect import engine  # $ pip install inflect
# learning libraries VS implementing by myself
# which approach to follow while learning python


def say(num:int) -> str:
    if not 1e12 > num >= 0:
        raise ValueError('invalid number input.')

    return ' '.join(engine().number_to_words(num, wantlist=True, andword=''))
