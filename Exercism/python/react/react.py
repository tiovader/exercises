from typing import Union


CELLS: list[Union['InputCell', 'ComputeCell']] = []


class InputCell:
    def __init__(self, initial_value: int):
        self._value = initial_value
        CELLS.append(self)

    @property
    def value(self): return self._value
    def _update(self): return self._value

    @value.setter
    def value(self, value):
        self._value, new_value = value, self._value != value
        [cell._update() for cell in CELLS if new_value]


class ComputeCell:
    def __init__(self, inputs: list[InputCell], compute_function):
        self._function = lambda: compute_function([i.value for i in inputs])
        self._callbacks = []
        self._value = self._function()
        CELLS.append(self)

    @property
    def value(self): return self._value
    def add_callback(self, callback): self._callbacks.append(callback)

    def _update(self):
        self._value, new_value = self._function(), self._value != self._function()
        [c(self._value) for c in self._callbacks if new_value]

    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)
