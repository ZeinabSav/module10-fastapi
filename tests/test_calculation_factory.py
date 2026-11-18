from calculation_factory import CalculationFactory


def test_add():
    op = CalculationFactory.get_operation("Add")
    assert op.calculate(5, 3) == 8


def test_sub():
    op = CalculationFactory.get_operation("Sub")
    assert op.calculate(10, 4) == 6


def test_multiply():
    op = CalculationFactory.get_operation("Multiply")
    assert op.calculate(3, 4) == 12


def test_divide():
    op = CalculationFactory.get_operation("Divide")
    assert op.calculate(10, 2) == 5