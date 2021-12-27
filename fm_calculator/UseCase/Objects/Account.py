from ...Entities.DataTable import DataTable


class Account:
    def __init__(self, account_id, data_table: DataTable):
        self._account_id = account_id
        self._data_table = data_table

    @property
    def values(self) -> tuple:
        return self._data_table.get_values(self._account_id)

    def get_value(self, period: int) -> float:
        return self._data_table.get_value(self._account_id, period)

    def set_values(self, values: tuple):
        self._data_table.set_values(self._account_id, values)

    def set_value(self, period: int, value: float):
        self._data_table.set_value(self._account_id, period, value)

    @property
    def id(self):
        return self._account_id

    def __repr__(self):
        return f'Account:{self._account_id}'
