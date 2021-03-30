from Vehicle import Vehicle


class Motorbike(Vehicle):
    def __init__(self, reg, weight):
        super().__init__(reg, weight)

    def calculate_fee(self):
        return 3.00
