from .BaseClass import UseCase
from .Objects import InteractorObjects


class ChangeNumberOfPeriods(UseCase):
    def __init__(self, interactor_objects: InteractorObjects, number_of_periods: int):
        UseCase.__init__(self, interactor_objects)
        self._number_of_periods = number_of_periods

    def execute(self):
        self.configurations.set_number_of_periods(self._number_of_periods)
