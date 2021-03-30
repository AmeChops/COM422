from Vehicle import Vehicle


class Lorry(Vehicle):
    def __init__(self, reg, weight):
        super().__init__(reg, weight)

    def calculate_fee(self):
        if self.weight <= 8000.00:
            return 10.00
        return 15.00
