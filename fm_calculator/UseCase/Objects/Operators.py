class Operators:
    __takes_one_argument__ = ('abs',)
    __takes_two_arguments__ = ('+', '-', '*', 'x', '/', '**', '^', '=', '<', '<=', '>', '>=', 'max', 'min', 'shift',
                               'iferror')
    __takes_arbitrary_number_of_arguments__ = ('sum', 'average')

    def __init__(self):
        self._data = {
            '+': add__,
            '-': sub__,
            '*': mul__,
            'x': mul__,
            '/': truediv__,
            '**': pow__,
            '^': pow__,
            '=': eq__,
            '<': lt__,
            '<=': le__,
            '>': gt__,
            '>=': ge__,
            'shift': __shift__,

            'max': __max__,
            'min': __min__,
            'sum': __sum__,
            'average': __average__,
            'abs': abs__,
            'iferror': iferror__,
        }

    def takes_one_argument(self, operator_id) -> bool:
        return operator_id in self.__takes_one_argument__

    def takes_two_argument(self, operator_id) -> bool:
        return operator_id in self.__takes_two_arguments__

    def execute(self, operator_id, *args, **kwargs):
        return self._data[operator_id](*args, **kwargs)

    def __contains__(self, item) -> bool:
        return item in self._data


def add__(period: int, a, b, shift_a=0, shift_b=0):
    return get_value(a, period + shift_a) + get_value(b, period + shift_b)


def sub__(period: int, a, b, shift_a=0, shift_b=0):
    return get_value(a, period + shift_a) - get_value(b, period + shift_b)


def mul__(period: int, a, b, shift_a=0, shift_b=0):
    return get_value(a, period + shift_a) * get_value(b, period + shift_b)


def truediv__(period: int, a, b, shift_a=0, shift_b=0):
    try:
        return get_value(a, period + shift_a) / get_value(b, period + shift_b)
    except ZeroDivisionError:
        return 0


def pow__(period: int, a, b, shift_a=0, shift_b=0):
    return get_value(a, period + shift_a) ** get_value(b, period + shift_b)


def eq__(period: int, a, b, shift_a=0, shift_b=0):
    return get_value(a, period + shift_a) == get_value(b, period + shift_b)


def lt__(period: int, a, b, shift_a=0, shift_b=0):
    return get_value(a, period + shift_a) < get_value(b, period + shift_b)


def le__(period: int, a, b, shift_a=0, shift_b=0):
    return get_value(a, period + shift_a) <= get_value(b, period + shift_b)


def gt__(period: int, a, b, shift_a=0, shift_b=0):
    return get_value(a, period + shift_a) > get_value(b, period + shift_b)


def ge__(period: int, a, b, shift_a=0, shift_b=0):
    return get_value(a, period + shift_a) >= get_value(b, period + shift_b)


def __sum__(period: int, *args):
    return sum(tuple(get_value(arg, period) for arg in args))


def __average__(period: int, *args):
    return 0 if len(args) == 0 else __sum__(period, *args) / len(args)


def __shift__(period: int, *args):
    element, shift = args
    return get_value(element, period + shift)


def __max__(period: int, *args):
    return max(tuple(get_value(arg, period) * 1 for arg in args))


def __min__(period: int, *args):
    return min(tuple(get_value(arg, period) * 1 for arg in args))


def abs__(period: int, a):
    return abs(get_value(a, period))


def iferror__(period: int, a, b, shift_a=0, shift_b=0):
    try:
        value = float(get_value(a, period + shift_a))
    except ZeroDivisionError:
        value = get_value(b, period + shift_b)
    return value


def get_value(element, period: int):
    try:
        return element.get_value(period)
    except KeyError:
        return 0
    except AttributeError:
        return element
