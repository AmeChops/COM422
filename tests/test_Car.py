from Car import Car


def test_create_car_reg():
    car = Car("abc", 1590)
    assert car.reg == "abc"


def test_create_car_weight():
    car = Car("abc", 1590)
    assert car.weight == 1590


def test_create_car_fee():
    car = Car("abc", 1590)
    fee = car.calculate_fee()
    assert fee == 10.00


def test_create_car_fee_overweight_by_less_than_100():
    car = Car("abc", 1650)
    fee = car.calculate_fee()
    assert fee == 10.00


def test_create_car_fee_overweight_by_100():
    car = Car("abc", 1690)
    fee = car.calculate_fee()
    assert fee == 10.10
