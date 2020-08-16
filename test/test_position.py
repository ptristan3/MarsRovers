import pytest
from src.position import Position
from src.exception_position import PositionInvalidException


class TestInit():
    def test_init_valid(self):
        test_position = Position('1', '1', 'N')
        assert test_position.x == 1
        assert test_position.y == 1
        assert test_position.cardinal == 'N'
        assert type(test_position.x) == int
        assert type(test_position.y) == int
        assert type(test_position.cardinal) == str

    def test_init_less_than_zero(self):
        with pytest.raises(PositionInvalidException):
            test_position = Position('-1', '1', 'N')

    def test_init_invalid_cardinal(self):
        with pytest.raises(PositionInvalidException):
            test_osition = Position('1', '1', 'A')


class TestEq():
    def test_Operator_EqTrue(self):
        test_position1 = Position('1', '1', 'N')
        test_position2 = Position('1', '1', 'N')
        assert test_position1 == test_position2

    def test_Operator_EqFalse(self):
        test_position1 = Position('1', '1', 'N')
        test_position2 = Position('1', '2', 'N')
        assert not test_position1 == test_position2