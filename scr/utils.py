import re
import os


class EnviromentVariables:
    def __init__(self):
        self.__vars = dict(self.__get_variables())

    def __get_variables(self):
        curdir = os.path.dirname(os.path.abspath(__file__))
        with open(f'{curdir}/.config') as file:
            content = file.read()

        yield from (re.search(r'(.+)=(.+)', line).groups()
                    for line in content.splitlines())
    def keys(self):
        return self.__vars.keys()
    def __getattribute__(self, __name: str):
        try:
            return super().__getattribute__(__name)
        except:
            return self.__vars[__name]

    def __getitem__(self, __name):
        return self.__vars[__name]
