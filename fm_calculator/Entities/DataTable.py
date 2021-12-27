from typing import Any
from typing import Dict


class DataTable:
    def __init__(self):
        self._data: Dict[Any, Dict[int, float]] = {}

    def get_values(self, account_id) -> tuple:
        return tuple(self._data[account_id].values()) if account_id in self._data else ()

    def get_value(self, account_id, period: int) -> float:
        return self._data[account_id][period]

    def add_new_account(self, account_id, values: tuple = ()):
        nop = len(values)
        self._data[account_id] = dict(zip(range(nop), values))

    def set_values(self, account_id, values: tuple):
        nop = len(values)
        self._data[account_id] = dict(zip(range(nop), values))

    def set_value(self, account_id, period: int, value: float):
        self._data[account_id][period] = value

    @property
    def data(self) -> Dict[Any, Dict[int, float]]:
        return self._data

    def __repr__(self):
        return str(self._data)
