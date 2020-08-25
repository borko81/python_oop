#---------
class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False

# ---------------
import unittest

class TestCat(unittest.TestCase):

    def test_CatSizeIncreaseShoud_increasesizeBy1(self):
        """"Cat's size is increased after eating"""
        name = "Cat Name"
        fed = False
        sleepy = False
        size = 0
        cat = Cat(name)

        cat.eat()
        self.assertEqual(size + 1, cat.size)


    def test_CatFedAfterEating(self):
        """"Cat is fed after eating"""
        name = "Cat Name"
        cat = Cat(name)
        cat.eat()
        self.assertTrue(cat.fed)


    def test_CatCannotEatAfterFedShoud_raise_error(self):
        """"Cat cannot eat if already fed, raises an error"""
        name = "Cat Name"
        cat = Cat(name)
        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()

        self.assertIsNotNone(context.exception)


    def test_CatCannotFallasleepifNotFed_Should_RaiseError(self):
        """"Cat cannot fall asleep if not fed, raises an error"""
        name = "Cat Name"
        cat = Cat(name)
        with self.assertRaises(Exception) as context:
            cat.sleep()

        self.assertIsNotNone(context.exception)


    def test_CatIsNotSleepyAfterSleeping(self):
        """"Cat is not sleepy after sleeping"""
        name = "Cat Name"
        cat = Cat(name)
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
