from typing import Any
from typing import Dict

from .BaseClass import UseCase
from .Objects import InteractorObjects


class InstantiateAccounts(UseCase):
    def __init__(self, interactor_objects: InteractorObjects, account_ids: tuple, input_values: Dict[Any, tuple],
                 number_of_periods: int, constants_to_values: dict = None):
        UseCase.__init__(self, interactor_objects)
        self._account_ids = account_ids
        self._number_of_periods = number_of_periods
        self._input_values = input_values
        self._constants_to_values = constants_to_values if (constants_to_values is not None) else {}

    def execute(self):
        account_factory = self.account_factory
        accounts = self.accounts
        account_ids = self._account_ids
        input_values = self._input_values
        for account_id in account_ids:
            values = input_values[account_id] if account_id in input_values else tuple()
            new_account = account_factory.create_account(account_id, values)
            accounts.add_account(account_id, new_account)

        for constant_id, value in self._constants_to_values.items():
            values = tuple(value for _ in range(self._number_of_periods))
            new_account = account_factory.create_account(constant_id, values)
            accounts.add_account(constant_id, new_account)
