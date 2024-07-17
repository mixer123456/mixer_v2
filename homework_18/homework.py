class Car:

    def __init__(self, *, producer: str, brand: str, fuel_consumption: float, year_of_issue: int = 2020):
        self.__year_of_issue = year_of_issue
        self.producer = producer.title()
        self.brand = brand.title()
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
        return f'This {self.__year_of_issue} car is from {self.producer} from {self.brand}'


car1 = Car(year_of_issue=2021, producer='ferdinand porsche', brand='porsche')
print(car1)
