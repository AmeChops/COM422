
class Bridge:
    def __init__(self, max_vehicles=20, max_weight=30000):
        self.max_vehicles = max_vehicles
        self.max_weight = max_weight
        self.vehicles = []

    def calculate_total_weight(self):
        total_weight = 0
        for vehicle in self.vehicles:
            total_weight += vehicle.weight
        return total_weight

    def add_vehicle(self, vehicle):
        total_weight = self.calculate_total_weight()

        if len(self.vehicles) < self.max_vehicles:
            if vehicle.weight + total_weight <= self.max_weight:
                self.vehicles.append(vehicle)
                return True
        return False