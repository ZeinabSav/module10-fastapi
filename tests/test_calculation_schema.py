import pytest
from pydantic import ValidationError

from schemas.calculation import CalculationCreate


def test_valid_calculation():
    calc = CalculationCreate(
        a=10,
        b=2,
        type="Divide"
    )

    assert calc.a == 10
    assert calc.b == 2


def test_invalid_type():
    with pytest.raises(ValidationError):
        CalculationCreate(
            a=10,
            b=5,
            type="Power"
        )


def test_divide_by_zero():
    with pytest.raises(ValidationError):
        CalculationCreate(
            a=10,
            b=0,
            type="Divide"
        )