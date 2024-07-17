class Car:

    def __init__(self, *, brand: str, model: str, fuel_consumption: float, year: int = 2020):
        self.__year_of_issue = year
        self.brand = brand.title()
        self.model = model.title()
        self.__fuel_consumption = fuel_consumption

        self.__mileage = 0


    @property
    def year_of_issue(self) -> int:
        return self.__year_of_issue

    @year_of_issue.setter
    def year_of_issue(self, value):
        self.__year_of_issue = value

    @property
    def mileage(self) -> int:
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        self.__mileage = value

    @property
    def fuel_consumption(self) -> float:
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        self.__fuel_consumption = value

    def __str__(self) -> str:
        if self.__fuel_consumption:
            return f'{self.__year_of_issue} car from {self.brand} {self.model} model with fuel consumption {self.__fuel_consumption}'
        else:
            return f'{self.__year_of_issue} car from {self.brand} {self.model} model and it is electric car'


car1 = Car(year=2021, brand='porsche', model='cayman', fuel_consumption=22.1)
print(car1)
car2 = Car(year=2023, brand='tesla', model='model x', fuel_consumption=0)
print(car2)
car3 = Car(year=2020, brand='mercedes', model='AMG', fuel_consumption=30.0)
print(car3)

