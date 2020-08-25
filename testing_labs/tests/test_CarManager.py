import unittest

from OOP.testing.labs.tests.CarManager import Car


class TestCar(unittest.TestCase):

    def __get_exception_from_init(self, make, model, fuel_consumption, fuel_capacity):
        with self.assertRaises(Exception) as ex:
            Car(make, model, fuel_consumption, fuel_capacity)
        return ex.exception


    def test_carInitWithCorectValues(self):
        make = "Test make"
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 60

        car = Car(make, model, fuel_consumption, fuel_capacity)
        expected = [make, model, fuel_consumption, fuel_capacity, 0]
        actual = [car.make, car.model, car.fuel_consumption, car.fuel_capacity, car.fuel_amount]

        self.assertListEqual(expected, actual)

    def test_carWithInvalidMake_shouldRaise(self):
        make = None
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carWithEmptyMake_shouldRaise(self):
        make = ""
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carWithInvalidModel_shouldRaise(self):
        make = "Test Car"
        model = None
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carWithEmptyModel_shouldRaise(self):
        make = "Test Car"
        model = ''
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carWithlessNegativeFuelConsumption_shouldRaise(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = -1
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carWithlessZeroFuelConsumption_shouldRaise(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = 0
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carWithlessNegativeCapasity_shouldRaise(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = -1

        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carWithlessZeroCapasity_shouldRaise(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 0

        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_catNegativeFuelAmmount_ShouldRaise(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        with self.assertRaises(Exception) as x:
            car.fuel_amount = -1

        self.assertIsNotNone(x.exception)

    def test_carRefuelWithZero_ShouldRaiseException(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        with self.assertRaises(Exception) as x:
            car.refuel(0)

        self.assertIsNotNone(x.exception)

    def test_carRefuelWithNegative_ShouldRaiseException(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        with self.assertRaises(Exception) as x:
            car.refuel(-1)

        self.assertIsNotNone(x.exception)

    def test_carRefuelWithPositiveAndEnoughttoCapasity_ShouldReturn(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        car.refuel(6)

        self.assertEqual(6, car.fuel_amount)


    def test_carRefuelWithPositiveAndBiggerFromCapasity_ShouldReturn(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        car.refuel(car.fuel_capacity * 2)

        self.assertEqual(car.fuel_capacity, car.fuel_amount)

    def test_driveWhenNotEnoughtFuelRaiseException(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        with self.assertRaises(Exception) as x:
            car.drive(100)

        self.assertIsNotNone(x.exception)

    def test_driveWhithEnoughtFuelRaiseException(self):
        make = "Test Car"
        model = 'Test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        car.refuel(car.fuel_capacity)
        distance = 100
        car.drive(distance)

        expected = car.fuel_capacity - car.fuel_consumption * distance / 100
        actual = car.fuel_amount

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()