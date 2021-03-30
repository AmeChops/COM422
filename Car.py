from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, reg, weight):
        super().__init__(reg, weight)

    def calculate_fee(self):
        fee = 10.00

        if self.weight > 1590:
            overweight = self.weight - 1590
            times_exceeded = overweight / 100
            return fee + (int(times_exceeded) * 0.10)

        return fee
