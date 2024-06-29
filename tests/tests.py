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

    def test_result_collection(self):
        bowling = bowling_engine.Bowling(game_result='X2/')
        result = bowling.results_collection()
        self.assertEqual(result, 35, 'Не верно рассчитываются очки!')

    def test_result_strike(self):
        bowling = bowling_engine.Bowling(game_result='X')
        result = bowling.results_collection()
        self.assertEqual(result, 20, 'Не верно рассчитываются очки за страйк!')

    def test_result_spare(self):
        bowling = bowling_engine.Bowling(game_result='2/')
        result = bowling.results_collection()
        self.assertEqual(result, 15, 'Не верно рассчитываются очки за спайр!')

    def test_result_miss(self):
        bowling = bowling_engine.Bowling(game_result='--')
        result = bowling.results_collection()
        self.assertEqual(result, 0, 'Не верно рассчитываются очки!')

    def test_result_hits(self):
        bowling = bowling_engine.Bowling(game_result='23')
        result = bowling.results_collection()
        self.assertEqual(result, 5, 'Не верно рассчитываются очки!')


if __name__ == '__main__':
    TestCase.main()
