RES = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
       'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}


def color_code(color: str) -> int: return RES[color.lower()]
def colors() -> list[str]: return list(RES.keys()).copy()
