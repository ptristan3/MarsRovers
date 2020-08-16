import pytest
from unittest.mock import patch
from collections import namedtuple
from src.rover import Rover
from src.position import Position
from src.plateau import Plateau
from src.exception_plateau import PlateauInvalidDimmensionException
from src.position_interface import PositionInterface
from src.rover_interface import Rover_Interface
from src.exception_command import CommandInvalidException
from src.exception_position import PositionNotFoundException, PositionInvalidException, PositionBusyException
from src.parser_input import parse_input_model_file


class ManagerFilesMok():

    def __init__(self):
        pass

    def readline(self):
        return '5 5'

    def readlines(self):
        return ['1 2 N', 'xxxx', '1 2 N', 'xxxx']


class TestParserInput():

    def test_all_its_ok(self, monkeypatch):
        monkeypatch.setattr('builtins.open', lambda x: ManagerFilesMok())
        with patch('src.parser_input.produce') as produce_mock:
            produce_mock.return_value = list()
            with patch('src.parser_input.Plateau') as MockPlateau:
                instancePlateau = MockPlateau.return_value
                instancePlateau.is_busy_position.return_value = False
                with patch('src.parser_input.Rover') as MockRover:
                    instanceRover = MockPlateau.return_value
                    parse_input_model_file('mockPath')
                    assert instancePlateau.is_busy_position.call_count == 2
                    assert instancePlateau.add_rover.call_count == 2
                    produce_mock.assert_called_with('xxxx')

    def test_bad_plateau(self, monkeypatch):
        monkeypatch.setattr('builtins.open', lambda x: ManagerFilesMok())
        with patch('src.parser_input.Plateau') as MockPlateau:
            instancePlateau = MockPlateau.return_value
            MockPlateau.side_effect = PlateauInvalidDimmensionException(
                -1, 1)
            with patch('src.parser_input.logging') as mock_logging:
                parse_input_model_file('mockPath')
                mock_logging.info.assert_called_with(
                    'Into parser of input. Exception: %s', 'Position -1 is not valid')

    def test_bad_position(self, monkeypatch):
        monkeypatch.setattr('builtins.open', lambda x: ManagerFilesMok())
        with patch('src.parser_input.produce') as produce_mock:
            produce_mock.return_value = list()
            with patch('src.parser_input.Plateau') as MockPlateau:
                with patch('src.parser_input.Rover') as MockRover:
                    MockRover.side_effect = PositionInvalidException(
                        -1, 1, 'P')
                    with patch('src.parser_input.logging') as mock_logging:
                        parse_input_model_file('mockPath')
                        mock_logging.info.assert_called_with(
                            'Into parser of input. Exception: %s', 'Position -1 1 P is not valid')
                        produce_mock.assert_called_with('xxxx')

    def test_bad_command(self, monkeypatch):
        monkeypatch.setattr('builtins.open', lambda x: ManagerFilesMok())
        with patch('src.parser_input.produce') as produce_mock:
            produce_mock.side_effect = CommandInvalidException('X')
            with patch('src.parser_input.Plateau'):
                with patch('src.parser_input.logging') as mock_logging:
                    parse_input_model_file('mockPath')
                    mock_logging.info.assert_called_with(
                        'Into parser of input. Exception: %s', 'Command X is not valid')
                    produce_mock.assert_called_with('xxxx')
