from unit_testing_pytest.source import mathlib


def test_calc_total():
    result = mathlib.calc_total(4, 5)
    assert result == 9


def test_calc_multiply():
    result = mathlib.calc_multipy(3, 4)
    assert result == 12