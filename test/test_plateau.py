import pytest
from collections import namedtuple
from src.rover import Rover
from src.position import Position
from src.plateau import Plateau
from src.exception_plateau import PlateauInvalidDimmensionException
from src.position_interface import PositionInterface
from src.rover_interface import RoverInterface
from src.exception_position import PositionNotFoundException

ANY_VALUE_TEST_POSITION = 'test_position'


class TestInit():

    def test_init_valid(self):
        test_plateau = Plateau(5, 5)
        assert test_plateau.width == 5
        assert test_plateau.height == 5
        assert test_plateau.rovers == list()
        assert type(test_plateau.width) == int
        assert type(test_plateau.height) == int

    def test_init_dim_less_than_zero(self):
        with pytest.raises(PlateauInvalidDimmensionException):
            test_plateau = Plateau(-1, 5)


class Test_Add_Rover():

    def test_rovers_count(self):
        test_plateau = Plateau(5, 5)
        test_size_in = len(test_plateau.rovers)
        test_mission = list()
        test_rover = Rover(1, ANY_VALUE_TEST_POSITION, test_mission)
        test_plateau.add_rover(test_rover)
        test_size_out = len(test_plateau.rovers)
        assert test_size_in + 1 == test_size_out

    def test_rovers_no_reapeted(self):
        test_plateau = Plateau(5, 5)
        test_size_in = len(test_plateau.rovers)
        test_rover = Rover(1, ANY_VALUE_TEST_POSITION, list())
        test_plateau.add_rover(test_rover)
        """add again the same rover"""
        test_plateau.add_rover(test_rover)
        test_size_out = len(test_plateau.rovers)
        assert test_size_in + 1 == test_size_out


class Test_Is_In_Range():

    def test_range_ok(self):
        test_plateau = Plateau(5, 5)
        test_position = Position('3', '3', 'N')
        assert test_plateau.width >= test_position.x
        assert test_plateau.height >= test_position.y

    def test_out_of_range_(self):
        test_plateau = Plateau(5, 5)
        test_position = Position('9', '3', 'N')
        assert not test_plateau.width >= test_position.x or not test_plateau.height >= test_position.y


class Position_Mock_True(PositionInterface):
    def __eq__(self, position):
        return True


class Position_Mock_False(PositionInterface):
    def __eq__(self, position):
        return False


class Rover_Mock_Rover(RoverInterface):
    def __init__(self, id_number, position):
        self.id_number = id_number
        self.position = position


class Test_Is_Valid_Position():

    def test_valid_position(self, monkeypatch):
        test_plateau = Plateau(5, 5)
        test_position1 = Position_Mock_False()
        id_rover1 = 1
        test_rover1 = Rover_Mock_Rover(
            id_number=id_rover1, position=test_position1)
        id_rover2 = 2
        test_rover2 = Rover_Mock_Rover(
            id_number=id_rover2, position=test_position1)
        rovers = list()
        rovers.append(test_rover1)
        rovers.append(test_rover2)
        monkeypatch.setattr(
            "src.plateau.Plateau.is_in_range", lambda x, y: True)
        monkeypatch.setattr(test_plateau, 'rovers', rovers)
        assert test_plateau.is_valid_position(
            id_rover2, test_position1) == True

    def test_not_valid_position(self, monkeypatch):
        test_plateau = Plateau(5, 5)
        test_position1 = Position_Mock_True()
        id_rover1 = 1
        test_rover1 = Rover_Mock_Rover(
            id_number=id_rover1, position=test_position1)
        id_rover2 = 2
        test_rover2 = Rover_Mock_Rover(
            id_number=id_rover2, position=test_position1)
        rovers = list()
        rovers.append(test_rover1)
        rovers.append(test_rover2)
        monkeypatch.setattr(
            "src.plateau.Plateau.is_in_range", lambda x, y: True)
        monkeypatch.setattr(test_plateau, 'rovers', rovers)
        assert test_plateau.is_valid_position(
            id_rover2, test_position1) == False

    def test_not_in_range_position(self, monkeypatch):
        test_plateau = Plateau(5, 5)
        test_position1 = Position_Mock_True()
        id_rover1 = 1
        monkeypatch.setattr(
            "src.plateau.Plateau.is_in_range", lambda x, y: False)
        assert test_plateau.is_valid_position(
            id_rover1, test_position1) == False


class Test_Is_Busy_Position():

    def test_element_plateau_busy(self):
        test_plateau = Plateau(5, 5)
        test_position1 = Position('2', '2', 'W')
        test_rover1 = Rover(1, test_position1, list())
        test_plateau.add_rover(test_rover1)
        assert test_plateau.is_busy_position(test_position1) == True

    def test_element_plateau_not_busy(self):
        test_plateau = Plateau(5, 5)
        test_position1 = Position('2', '2', 'W')
        test_position2 = Position('1', '2', 'W')
        test_rover1 = Rover(1, test_position1, list())
        test_plateau.add_rover(test_rover1)
        assert not test_plateau.is_busy_position(test_position2) == True


class Rover_Mock_Rover_For_Run_Ok(RoverInterface):
    def __init__(self):      
        self.process_mission_called = False

    def process_mission(self, plateau):
        self.process_mission_called = True


class PositionNotFoundException_Mock(Exception):
    def __init__(self):
      super(PositionNotFoundException_Mock, self).__init__()

class Rover_Mock_Rover_For_Run_Fail(RoverInterface):

    def __init__(self):
        self.process_mission_called = False

    def process_mission(self, plateau):
        self.process_mission_called = True
        raise PositionNotFoundException_Mock()


class TestRun():

    def test_run_OK(self, monkeypatch):
        test_plateau = Plateau(5, 5)
        test_position1 = Position_Mock_False()
        id_rover1 = 1
        test_rover1 = Rover_Mock_Rover_For_Run_Ok()
        id_rover2 = 2
        test_rover2 = Rover_Mock_Rover_For_Run_Ok()
        rovers = list()
        rovers.append(test_rover1)
        rovers.append(test_rover2)
        monkeypatch.setattr(test_plateau, 'rovers', rovers)
        test_plateau.run()
        for rover in rovers:
            assert rover.process_mission_called == True

    def test_run_fail(self, monkeypatch):
        test_plateau = Plateau(5, 5)
        test_position1 = Position_Mock_False()
        id_rover1 = 1
        test_rover1 = Rover_Mock_Rover_For_Run_Ok()
        id_rover2 = 2
        test_rover2 = Rover_Mock_Rover_For_Run_Fail()
        rovers = list()
        rovers.append(test_rover1)
        rovers.append(test_rover2)
        monkeypatch.setattr(test_plateau, 'rovers', rovers)
        with pytest.raises(PositionNotFoundException_Mock ):
            test_plateau.run()
        for rover in rovers:
            assert rover.process_mission_called == True