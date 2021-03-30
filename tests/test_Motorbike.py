import pytest
from Motorbike import Motorbike


def test_create_motorbike_reg():
    mb = Motorbike("abc", 182)
    assert mb.reg == "abc"


def test_create_motorbike_weight():
    mb = Motorbike("abc", 182)
    assert mb.weight == 182


def test_create_motorbike_fee():
    mb = Motorbike("abc", 182)
    fee = mb.calculate_fee()
    assert fee == 3.00
