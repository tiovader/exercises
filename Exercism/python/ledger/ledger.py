import re


class Date:
    def __init__(self, year: int, month: int, day: int, locale=None) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.locale = locale

    def setlocale(self, locale: str) -> 'Date':
        self.locale = locale
        return self

    def __lt__(self, other: 'Date') -> bool:
        return tuple(self._date().values()) < tuple(other._date().values())

    def __repr__(self) -> str:
        str_ = {'en_US': '{month:02d}/{day:02d}/{year:04d}',
                'nl_NL': '{day:02d}-{month:02d}-{year:04d}'} \
            .get(self.locale, '{day:02d}/{month:02d}/{year:04d}')
        return str_.format(**self._date())

    def __format__(self, format_str: str) -> str:
        return str(self).format(format_str)

    def _date(self) -> dict[str, int]:
        return {'year': self.year, 'month': self.month, 'day': self.day}


class CurrencyFormatter:
    def format(value: float, currency: str, locale: str) -> str:
        formatter = {'en_US': CurrencyFormatter._en_US,
                     'nl_NL': CurrencyFormatter._nl_NL}[locale]

        symbol = {"USD": "$", "EUR": "€"}[currency]
        return formatter(f"{value:,.2f}", symbol)

    def _en_US(text: str, symbol: str) -> str:
        if text.count('-'):
            return re.sub(r'-(.+)', r'({}\1)'.format(symbol), text)
        return f' {symbol}{text} '

    def _nl_NL(text: str, symbol: str) -> str:
        text = text.translate(str.maketrans(",.", ".,"))
        return f" {symbol} {text} "


class LedgerEntry:

    def __init__(self, date: str, description: str, change: float) -> None:
        self.date = Date(*map(int, date.split('-')))
        self.description = description
        self.change = change/100

    def _values(self) -> tuple[Date, str, float]:
        return (self.date, self.description, self.change)

    def __lt__(self, other: 'LedgerEntry') -> bool:
        a, b, c = self._values()
        d, e, f = other._values()
        return a < d or b < e or c < f


create_entry = LedgerEntry


def format_entries(currency: str, locale: str, entries: list[LedgerEntry]) -> str:
    return '\n'.join(row for row in table(currency, locale, entries))


def table(currency: str, locale: str, entries: list[LedgerEntry]) -> str:
    def aux(entry: LedgerEntry):
        date = entry.date.setlocale(locale)
        a = entry.description
        description = (a, f"{a[:22]}...")[len(a) > 25]
        change = CurrencyFormatter.format(entry.change, currency, locale)
        return '{:<10} | {:<25} | {:>13}'.format(date, description, change)

    header = '{: <10} | {: <25} | {: <13}'
    format_ = {'en_US': ('Date', 'Description', 'Change'),
               'nl_NL': ('Datum', 'Omschrijving', 'Verandering')}[locale]
    yield header.format(*format_)
    yield from (aux(entry) for entry in sorted(entries))
