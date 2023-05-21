from typing import Any
from typing import Dict

import Interactor.display_list_of_actions

from . import SortRPE
from .BaseClass import UseCase
from .Objects import InteractorObjects


class Calculate(UseCase):
    def __init__(self, interactor_objects: InteractorObjects, rpes: dict, order_of_calculation=(), direct_links=(),
                 vertical_accounts: Dict[Any, tuple] = None):
        UseCase.__init__(self, interactor_objects)
        self._rpes = rpes
        self._order_of_calculation = order_of_calculation
        self._direct_links = direct_links
        self._vertical_accounts = vertical_accounts

    def execute(self):
        sorted_rpes = SortRPE.get_sorted_rpes(self._rpes, self._order_of_calculation, self._direct_links)
        execute(self, sorted_rpes, self._vertical_accounts)


def execute(interactor_objects: Calculate, sorted_rpes: dict, vertical_accounts: Dict[Any, tuple]):
    accounts = interactor_objects.accounts
    operators = interactor_objects.operators
    number_of_periods = interactor_objects.configurations.number_of_periods

    for period in range(number_of_periods):
        for owner_id, expression in sorted_rpes.items():
            if owner_id in vertical_accounts.keys():
                owner_account = accounts.get_account(owner_id)
                vertical_dependencies = vertical_accounts[owner_id]

                vertical_sum_value = 0
                for p in range(period + 1):
                    ##
                    stack = []
                    for n, element in enumerate(expression):
                        if element in accounts:
                            operand = accounts.get_account(element)
                            stack.append(operand)
                        elif element in operators:
                            if operators.takes_two_argument(element):
                                op2 = stack.pop()
                                op1 = stack.pop()
                                args = (period, op1, op2)

                                shift_a, shift_b = 0, 0
                                try:
                                    if op2.id in vertical_dependencies:
                                        shift_b = p - period
                                except AttributeError:
                                    pass
                                try:
                                    if op1.id in vertical_dependencies:
                                        shift_a = p - period
                                except AttributeError:
                                    pass
                                value = Interactor.display_list_of_actions.execute(,
                                stack.append(value)
                            elif operators.takes_one_argument(element):
                                op = stack.pop()
                                args = (period, op)
                                value = Interactor.display_list_of_actions.execute(,
                                stack.append(value)
                            else:
                                try:
                                    two_forward = expression[n + 2]
                                except IndexError:
                                    two_forward = None
                                op2 = stack.pop()
                                op1 = stack.pop()
                                if two_forward == element:
                                    # Handling operator that takes more than 2 arguments: Average(a, b, c)
                                    if type(op1) == tuple:
                                        stack.append(op1 + (op2,))
                                    else:
                                        stack.append((op1, op2))
                                else:
                                    # Calculate
                                    args = op1 + (op2,)
                                    value = Interactor.display_list_of_actions.execute(period,, element,
                                    stack.append(value)
                        else:
                            stack.append(element)  # float
                    if len(stack) != 1:
                        value = "invalid"
                    else:
                        # Multiply by 1 in case rpe = (Account) (direct link)
                        args = (stack.pop(), 1)
                        value = Interactor.display_list_of_actions.execute(period,, '*',
                    vertical_sum_value += value
                owner_account.set_value(period, vertical_sum_value)
            else:
                calculate_normal_accounts(accounts, expression, operators, owner_id, period)


def calculate_normal_accounts(accounts, expression, operators, owner_id, period):
    owner_account = accounts.get_account(owner_id)
    value = calculate_value(accounts, expression, operators, period)
    owner_account.set_value(period, value)


def calculate_value(accounts, expression, operators, period) -> float:
    stack = []
    for n, element in enumerate(expression):
        if element in accounts:
            operand = accounts.get_account(element)
            stack.append(operand)
        elif element in operators:
            if operators.takes_two_argument(element):
                op2 = stack.pop()
                op1 = stack.pop()
                args = (period, op1, op2)
                value = Interactor.display_list_of_actions.execute(,
                stack.append(value)
            elif operators.takes_one_argument(element):
                op = stack.pop()
                args = (period, op)
                value = Interactor.display_list_of_actions.execute(,
                stack.append(value)
            else:
                try:
                    two_forward = expression[n + 2]
                except IndexError:
                    two_forward = None
                op2 = stack.pop()
                op1 = stack.pop()
                if two_forward == element:
                    # Handling operator that takes more than 2 arguments: Average(a, b, c)
                    if type(op1) == tuple:
                        stack.append(op1 + (op2,))
                    else:
                        stack.append((op1, op2))
                else:
                    # Calculate
                    args = op1 + (op2,)
                    value = Interactor.display_list_of_actions.execute(period,, element,
                    stack.append(value)
        else:
            stack.append(element)  # float
    if len(stack) != 1:
        value = "invalid"
    else:
        # Multiply by 1 in case rpe = (Account) (direct link)
        args = (stack.pop(), 1)
        value = Interactor.display_list_of_actions.execute(period,, '*',
    return value
