import unittest

class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return (f'{self.name} has saved {self.money} money.')


class WorkerTests(unittest.TestCase):
    def test_worker(self):
        """Test if the worker is initialized with correct name, salary and energy"""
        name = "Worker Name"
        salary = 100
        energy = 5
        worker = Worker(name, salary, energy)
        self.assertEqual(name, worker.name)
        self.assertEqual(salary, worker.salary)
        self.assertEqual(energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_rest(self):
        """Test if the worker's energy is incremented after the rest method is called"""
        name = "Worker Name"
        salary = 100
        energy = 5
        worker = Worker(name, salary, energy)
        worker.rest()
        self.assertEqual(energy + 1, worker.energy)

    def test_rest_with_zero_enery(self):
        """Test if an error is raised if the worker tries to work with negative energy or equal to 0"""
        name = "Worker Name"
        salary = 100
        energy = 0
        worker = Worker(name, salary, energy)
        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertIsNotNone(context.exception)

    def test_get_money(self):
        """Test if the worker's money is increased by his salary correctly after the work method is called"""
        name = "Worker Name"
        salary = 100
        energy = 5
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(salary, worker.money)

    def test_get_worker_enery_decrease(self):
        """Test if the worker's energy is decreased after the work method is called"""
        name = "Worker Name"
        salary = 100
        energy = 5
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(energy - 1, worker.energy)

    def test_get_info(self):
        """Test if the get_info method returns the proper string with correct values"""
        name = "Worker Name"
        salary = 100
        energy = 0
        worker = Worker(name, salary, energy)
        expexted = f'{name} has saved 0 money.'
        actual = worker.get_info()
        self.assertEqual(expexted, actual)


if __name__ == '__main__':
    unittest.main()
