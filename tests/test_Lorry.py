import pytest
from Lorry import Lorry


def test_create_lorry():
    lorry = Lorry("zzz", 7500.00)
    assert lorry.reg == "zzz"


def test_create_lorry_weight():
    lorry = Lorry("zzz", 7500.00)
    assert lorry.weight == 7500.00


def test_create_little_lorry_fee():
    lorry = Lorry("zzz", 7500.00)
    fee = lorry.calculate_fee()
    assert fee == 10.00


def test_create_large_lorry_fee():
    lorry = Lorry("zzz", 8500.00)
    fee = lorry.calculate_fee()
    assert fee == 15.00