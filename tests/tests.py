# -*- coding: utf-8 -*-
import unittest
import bowling_engine


class BowlingTest(unittest.TestCase):
    """
    Тесты для модуля bowling_engine
    """

    def test_attribute_error_1(self):
        """
        Тест на выброс исключения входных данных

        :return: None
        """
        with self.assertRaises(AttributeError):
            bowling = bowling_engine.Bowling(game_result='')
            bowling.results_collection()

    def test_attribute_error_2(self):
        """
        Тест на выброс исключения входных данных

        :return: None
        """
        with self.assertRaises(AttributeError):
            bowling = bowling_engine.Bowling(game_result='5865')
            bowling.results_collection()

    def test_max_frame_error(self):
        """
        Тест на выброс исключения максимального количества фреймов

        :return: None
        """
        with self.assertRaises(bowling_engine.MaxFrameError):
            bowling = bowling_engine.Bowling(game_result='XXXXXXXXXXXXXXX')
            bowling.results_collection()

    def test_symbols_error(self):
        """
        Тест на выброс исключения неизвестного символа

        :return: None
        """
        with self.assertRaises(bowling_engine.InputValueError):
            bowling = bowling_engine.Bowling(game_result='1s')
            bowling.results_collection()

    def test_spare_error(self):
        """
        Тест на выброс исключения спайра

        :return: None
        """
        with self.assertRaises(bowling_engine.SpareError):
            bowling = bowling_engine.Bowling(game_result='/1')
            bowling.results_collection()

    def test_strike_error(self):
        """
        Тест на выброс исключения страйка

        :return: None
        """
        with self.assertRaises(bowling_engine.StrikeError):
            bowling = bowling_engine.Bowling(game_result='2X')
            bowling.results_collection()

    def test_result_collection(self):
        """
        Тест на правильный расчет

        :return: None
        """
        bowling = bowling_engine.Bowling(game_result='X2/')
        result = bowling.results_collection()
        self.assertEqual(result, 35, 'Не верно рассчитываются очки!')

    def test_result_strike(self):
        """
        Тест на страйк

        :return: None
        """
        bowling = bowling_engine.Bowling(game_result='X')
        result = bowling.results_collection()
        self.assertEqual(result, 20, 'Не верно рассчитываются очки за страйк!')

    def test_result_spare(self):
        """
        Тест на спайр

        :return: None
        """
        bowling = bowling_engine.Bowling(game_result='2/')
        result = bowling.results_collection()
        self.assertEqual(result, 15, 'Не верно рассчитываются очки за спайр!')

    def test_result_miss(self):
        """
        Тест на два промаха

        :return: None
        """
        bowling = bowling_engine.Bowling(game_result='--')
        result = bowling.results_collection()
        self.assertEqual(result, 0, 'Не верно рассчитываются очки за два промаха!')

    def test_result_hits(self):
        """
        Тест на два попадания

        :return: None
        """
        bowling = bowling_engine.Bowling(game_result='23')
        result = bowling.results_collection()
        self.assertEqual(result, 5, 'Не верно рассчитываются очки за два попадания!')


if __name__ == '__main__':
    unittest.main()
