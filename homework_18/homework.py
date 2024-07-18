import datetime

import exceptions


class Car:

    def __init__(self, *, brand: str, model: str, fuel_consumption: float, year: int = 2020):
        if year < 1900 or year > datetime.datetime.now().year:
            raise exceptions.InvalidYearException()

        if fuel_consumption < 0:
            raise exceptions.InvalidFuelConsumptionException()

        self.__year_of_issue = year
        self.__brand = brand.title()
        self.__model = model.title()
        self.__fuel_consumption = fuel_consumption
        self.__mileage = 0


    @property
    def year_of_issue(self) -> int:
        return self.__year_of_issue

    @property
    def mileage(self) -> int:
        return self.__mileage

    @mileage.setter
    def mileage(self, value: int):
        if value < 0:
            raise exceptions.InvalidMileageException()

        self.__mileage = value

    @property
    def fuel_consumption(self) -> float:
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if value < 0:
            raise exceptions.InvalidFuelConsumptionException()

        self.__fuel_consumption = value

    def __str__(self) -> str:
        if self.__fuel_consumption:
            return f'{self.__brand} {self.__model} with fuel consumption {self.__fuel_consumption} {self.__year_of_issue} year'
        else:
            return f'Electric car {self.__brand} {self.__model} {self.__year_of_issue} year'


car1 = Car(year=2029, brand='porsche', model='cayman', fuel_consumption=22.1)
car1.mileage = -500
car2 = Car(year=2023, brand='tesla', model='model x', fuel_consumption=0)
car3 = Car(year=2020, brand='mercedes', model='AMG', fuel_consumption=30.0)

print(car1)
print(car2)
print(car3)

datetime.datetime.now()
