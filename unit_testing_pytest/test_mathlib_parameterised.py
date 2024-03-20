from source.mathlib import calc_square
import pytest


@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (1, 1),
                             (2, 4),
                             (5, 25),
                             (7, 49),
                             (21, 441)
                         ],
                         ids=[
                             "test_square_1", "test_square_2", "test_square_5", "test_square_7", "test_square_21"
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = calc_square(test_input)
    assert result == expected_output
