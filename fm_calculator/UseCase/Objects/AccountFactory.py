from .Account import Account
from ...Entities.DataTable import DataTable


class AccountFactory:
    def __init__(self, data_table: DataTable):
        self._data_table = data_table

    def create_account(self, account_id, values: tuple = ()):
        self._data_table.add_new_account(account_id, values)
        return Account(account_id, self._data_table)
