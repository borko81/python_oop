from typing import ClassVar, List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    name: str
    customers: List[Customer]
    dvds: List[DVD]

    _DVD_CAPACITY: ClassVar[int] = 15
    _CUSTOMER_CAPACITY: ClassVar[int] = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []


    @classmethod
    def dvd_capacity(cls) -> int:
        return cls._DVD_CAPACITY

    @classmethod
    def customer_capacity(cls) -> int:
        return cls._CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) >= self._CUSTOMER_CAPACITY:
            return
        self.customers.append(customer)


    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) >= self._DVD_CAPACITY:
            return   # XXX
        self.dvds.append(dvd)


    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd      = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return 'DVD is already rented'
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = [c for c in self.customers if c.id == customer_id][0]

        if dvd_id not in map(lambda x: x.id, customer.rented_dvds):
            return f'{customer.name} does not have that DVD'

        dvd = [d for d in customer.rented_dvds if d.id == dvd_id][0]
        dvd.is_rented = False
        self.dvds.append(dvd)
        customer.rented_dvds.remove(dvd)

        return f'{customer.name} has successfully returned {dvd.name}'

    def __repr__(self):
        return '\n'.join([repr(x) for x in (self.customers + self.dvds)])