class Configurations:
    __number_of_periods__ = 'nop'

    def __init__(self):
        self._data = {
            self.__number_of_periods__: 0
        }

    @property
    def number_of_periods(self) -> int:
        return self._data[self.__number_of_periods__]

    def set_number_of_periods(self, number_of_periods: int):
        self._data[self.__number_of_periods__] = number_of_periods
