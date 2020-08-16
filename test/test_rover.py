from test import test_position
import pytest
from src.rover import Rover
from src.command_factory import produce
from src.position import Position
from src.exception_position import PositionInvalidException

ANY_VALUE_TEST_ROVER_MISSION = 'test_rover_mission'
ANY_VALUE_TEST_POSITION = 'test_position'
ANY_VALUE_TEST_ROVER_MISSION2 = 'test_rover_mission_2'
ANY_VALUE_TEST_POSITION2 = 'test_position2'


class TestInit():
    """ def test_init_valid(self, monkeypatch):
        def mocked_produce(commands):
          assert True == True
        monkeypatch.setattr('src.command_factory.produce',
                                mocked_produce)
    """

    def test_init_valid(self):
        test_rover_mission = ANY_VALUE_TEST_ROVER_MISSION
        test_position = ANY_VALUE_TEST_POSITION
        test_rover = Rover(1, test_position, test_rover_mission)
        assert test_rover.position == ANY_VALUE_TEST_POSITION
        assert test_rover.mission == ANY_VALUE_TEST_ROVER_MISSION


class TestEq():
    def test_Operator_EqTrue(self):
        test_rover_mission = ANY_VALUE_TEST_ROVER_MISSION
        test_position = ANY_VALUE_TEST_POSITION
        test_rover_mission_2 = ANY_VALUE_TEST_ROVER_MISSION2
        test_position_2 = ANY_VALUE_TEST_POSITION2
        test_rover1 = Rover(1, test_position, test_rover_mission)
        test_rover2 = Rover(1, test_position_2, test_rover_mission_2)
        assert test_rover1 == test_rover2

    def test_Operator_EqFalse(self):
        test_rover_mission = ANY_VALUE_TEST_ROVER_MISSION
        test_position = ANY_VALUE_TEST_POSITION
        test_rover1 = Rover(1, test_position, test_rover_mission)
        test_rover2 = Rover(2, test_position, test_rover_mission)
        assert not test_rover1 == test_rover2
