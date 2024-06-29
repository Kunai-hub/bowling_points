# -*- coding: utf-8 -*-
from unittest import TestCase
import bowling_engine


class BowlingTest(TestCase):
    """
    Тесты для модуля bowling_engine
    """

    def test_attribute_error_1(self):
        with self.assertRaises(AttributeError):
            bowling = bowling_engine.Bowling(game_result='')
            bowling.results_collection()

    def test_attribute_error_2(self):
        with self.assertRaises(AttributeError):
            bowling = bowling_engine.Bowling(game_result='5865')
            bowling.results_collection()

    def test_max_frame_error(self):
        with self.assertRaises(bowling_engine.MaxFrameError):
            bowling = bowling_engine.Bowling(game_result='XXXXXXXXXXXXXXX')
            bowling.results_collection()

    def test_symbols_error(self):
        with self.assertRaises(bowling_engine.InputValueError):
            bowling = bowling_engine.Bowling(game_result='1s')
            bowling.results_collection()

    def test_spare_error(self):
        with self.assertRaises(bowling_engine.SpareError):
            bowling = bowling_engine.Bowling(game_result='/1')
            bowling.results_collection()

    def test_strike_error(self):
        with self.assertRaises(bowling_engine.StrikeError):
            bowling = bowling_engine.Bowling(game_result='2X')
            bowling.results_collection()

