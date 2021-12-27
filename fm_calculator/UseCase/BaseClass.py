from abc import ABC
from abc import abstractmethod

from .Objects import InteractorObjects


class UseCase(ABC):
    def __init__(self, interactor_objects: InteractorObjects):
        self._account_factory = interactor_objects.account_factory
        self._accounts = interactor_objects.accounts
        self._operators = interactor_objects.operators
        self._configurations = interactor_objects.configurations

    @property
    def accounts(self):
        return self._accounts

    @property
    def account_factory(self):
        return self._account_factory

    @property
    def operators(self):
        return self._operators

    @property
    def configurations(self):
        return self._configurations

    @abstractmethod
    def execute(self):
        pass
