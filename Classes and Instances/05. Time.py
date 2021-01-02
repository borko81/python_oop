class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f'{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}'

    def next_second(self):
        change_second = self.seconds + 1
        if change_second > Time.max_seconds:
            self.seconds = '00'
            change_minutes = self.minutes + 1
            if change_minutes > Time.max_minutes:
                self.minutes = '00'
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = '00'
            else:
                self.minutes += 1
        else:
            self.seconds = change_second


        return self.get_time()