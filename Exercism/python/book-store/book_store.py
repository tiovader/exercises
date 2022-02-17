DISCOUNT = (None, 0, 5, 10, 20, 25)
PRICE = 800


def total(basket: list[int], price: int = PRICE,
          discount: tuple[int] = DISCOUNT) -> float:

    def get_price(amount: int) -> float:
        return price * amount * (1 - discount[amount]/100)

    lst = []
    while basket:
        lst += [len(group := set(basket))]
        [basket.remove(i) for i in group]

    while 3 in lst and 5 in lst:
        [lst.remove(i) for i in (3, 5)]
        lst.extend((4, 4))

    return sum(map(get_price, lst))
