from Bridge import Bridge
from Motorbike import Motorbike
from Lorry import Lorry


def test_create_bridge_max_vehicles():
    tollbridge = Bridge()
    assert tollbridge.max_vehicles == 20


def test_create_bridge_max_weight():
    tollbridge = Bridge()
    assert tollbridge.max_weight == 30000


def test_add_to_bridge():
    tollbridge = Bridge()
    mb = Motorbike("abc", 182)
    assert tollbridge.add_vehicle(mb) is True


def test_bridge_total_weight():
    tollbridge = Bridge()
    mb = Motorbike("abc", 182)
    lorry = Lorry("abc", 5000)
    tollbridge.add_vehicle(mb)
    tollbridge.add_vehicle(lorry)
    assert tollbridge.calculate_total_weight() == 5182


def test_add_to_full_bridge():
    tollbridge = Bridge(1, 10000)
    mb = Motorbike("abc", 182)
    tollbridge.add_vehicle(mb)
    lorry = Lorry("abc", 5000)
    assert tollbridge.add_vehicle(lorry) is False


def test_add_to_bridge_weight():
    tollbridge = Bridge(2, 5182)
    mb = Motorbike("abc", 182)
    tollbridge.add_vehicle(mb)
    lorry = Lorry("abc", 5000)
    assert tollbridge.add_vehicle(lorry) is True