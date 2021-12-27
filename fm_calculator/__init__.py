from typing import Any
from typing import Dict

from interface_fm_calculator import CalculatorABC

from . import Main


class Calculator(CalculatorABC):

    def create_data_table(self, request_model) -> Dict[Any, Dict[int, float]]:
        interactor_objects = Main.create_new_interactor_objects()
        Main.instantiate_accounts(interactor_objects, request_model)
        Main.change_number_of_periods(interactor_objects, request_model)
        Main.calculate(interactor_objects, request_model)
        return interactor_objects.data_table.data
