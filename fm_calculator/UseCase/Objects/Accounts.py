from .Account import Account


class Accounts:
    def __init__(self):
        self._data = {}

    def get_account(self, account_id) -> Account:
        return self._data[account_id]

    def add_account(self, account_id, account):
        self._data[account_id] = account

    @property
    def all_account_ids(self) -> tuple:
        return tuple(self._data.keys())

    def __contains__(self, item) -> bool:
        return item in self._data
