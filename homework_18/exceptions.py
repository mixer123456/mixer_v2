class InvalidYearException(Exception):
    def __init__(self, message='Invalid year for car.'):
        self.message = message
        super().__init__(self.message)


class InvalidFuelConsumptionException(Exception):
    def __init__(self, message='Invalid fuel consumption'):
        self.message = message
        super().__init__(self.message)


class InvalidMileageException(Exception):
    def __init__(self, message='Invalid mileage'):
        self.message = message
        super().__init__(self.message)
