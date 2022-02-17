from operator import add, sub
import threading


class BankAccount:

    def __init__(self):
        self.__is_active__ = False
        self.__balance__ = 0
        self.lock = threading.Lock()

    def open(self): self.__active__(True)
    def deposit(self, amount): self.__op__(amount, add)
    def withdraw(self, amount): self.__op__(amount, sub)
    def close(self): self.__active__(False)

    def get_balance(self):
        if not self.__is_active__:
            raise ValueError('The current accout is not active.')
        return self.__balance__

    def __op__(self, amount, op):
        with self.lock:
            if amount < 0:
                raise ValueError(
                    "It's not possible to handle negative values!")
            elif op(self.__balance__, amount) < 0:
                raise ValueError("Insufficient funds for this operation.")
            elif not self.__is_active__:
                raise ValueError('The current accout is not active.')

            self.__balance__ = op(self.__balance__, amount)

    def __active__(self, bool):
        if self.__is_active__ is bool:
            raise ValueError("It's not possible to handle this operation!")
        self.__is_active__ = bool

        if not self.__is_active__:
            self.__init__()
