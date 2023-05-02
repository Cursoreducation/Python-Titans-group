from functions import *
from unittest.mock import patch


def test_suma():
    assert suma(5, 4) == 9
    assert suma(6, 2) == 8

def test_dif():
    assert diff(5, 2) == 3
    assert diff(4, 5) == -1


@patch("functions.rand", return_value=4)
def test_suma_with_rand(mock_rand):
    assert suma_with_rand(5, 4) == 13
    assert mock_rand.called
