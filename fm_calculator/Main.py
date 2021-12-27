from .Entities import Configurations
from .Entities import DataTable
from .UseCase import Calculate
from .UseCase import ChangeNumberOfPeriods
from .UseCase import InteractorObjects
from .UseCase.InstantiateAccounts import InstantiateAccounts
from .UseCase.Objects.AccountFactory import AccountFactory


def create_new_interactor_objects() -> InteractorObjects:
    data_table = DataTable()
    account_factory = AccountFactory(data_table)
    configurations = Configurations()
    interactor_objects = InteractorObjects(data_table, account_factory, configurations)
    return interactor_objects


def instantiate_accounts(interactor_objects, request_model):
    account_ids = request_model['account_ids']
    input_values = request_model['input_values']
    constants_to_values: dict = request_model['constants_to_values'] if 'constants_to_values' in request_model else {}
    nop: int = request_model['number_of_periods']

    use_case = InstantiateAccounts(interactor_objects, account_ids, input_values, nop, constants_to_values)
    use_case.execute()


def change_number_of_periods(interactor_objects, request_model):
    number_of_periods: int = request_model['number_of_periods']
    use_case_change_nop = ChangeNumberOfPeriods(interactor_objects, number_of_periods)
    use_case_change_nop.execute()


def calculate(interactor_objects, request_model):
    rpes: dict = request_model['rpes']
    calculation_order = request_model['calculation_order'] if 'calculation_order' in request_model else ()
    direct_links = request_model['direct_links'] if 'direct_links' in request_model else ()
    vertical_accounts = request_model['vertical_accounts'] if 'vertical_accounts' in request_model else ()

    use_case_calculate = Calculate(interactor_objects, rpes, calculation_order, direct_links, vertical_accounts)
    use_case_calculate.execute()
