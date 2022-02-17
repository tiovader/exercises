import re
PATTERN = r"^(1)?(([2-9]\d{2})[2-9]\d{6})$"


class PhoneNumber:

    def __init__(self, number: str) -> None:
        if not (num:=re.match(PATTERN, re.sub(r'[^\d]', '', number))):
            raise ValueError("incorrect number of digits")

        self.number = num.group(2)
        self.area_code = num.group(3)

    def pretty(self):
        return f'({self.area_code})-{self.number[3:6]}-{self.number[6:]}'

