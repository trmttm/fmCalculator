from .AccountFactory import AccountFactory
from .Accounts import Accounts
from .Operators import Operators
from ...Entities import Configurations
from ...Entities import DataTable


class InteractorObjects:
    def __init__(self, data_table: DataTable, account_factory: AccountFactory, configurations: Configurations):
        self._data_table = data_table
        self._account_factory = account_factory
        self._configurations = configurations
        self._accounts = Accounts()
        self._operators = Operators()

    @property
    def data_table(self) -> DataTable:
        return self._data_table

    @property
    def account_factory(self) -> AccountFactory:
        return self._account_factory

    @property
    def configurations(self) -> Configurations:
        return self._configurations

    @property
    def accounts(self) -> Accounts:
        return self._accounts

    @property
    def operators(self) -> Operators:
        return self._operators
