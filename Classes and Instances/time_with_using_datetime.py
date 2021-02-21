import datetime
import unittest

class Time:

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    def next_second(self):
        t = datetime.datetime(1,1,1, int(self.hours), int(self.minutes), int(self.seconds))
        t += datetime.timedelta(seconds=1)
        self.hours, self.minutes, self.seconds = str(t.time()).split(':')
        return self.get_time()


class CheckTime(unittest.TestCase):

    def setUp(self):
        self.t = Time(1, 20, 30)

    def test_correct_set(self):
        self.assertEqual(self.t.hours, 1)
        self.assertEqual(self.t.minutes, 20)
        self.assertEqual(self.t.seconds, 30)

    def test_return_time(self):
        self.assertEqual(self.t.get_time(), '01:20:30')

    def test_increase_time(self):
        self.assertAlmostEqual(self.t.next_second(), '01:20:31')



if __name__ == '__main__':
    unittest.main()

