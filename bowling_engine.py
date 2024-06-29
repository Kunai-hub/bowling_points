# -*- coding: utf-8 -*-
import logging
from abc import ABC, abstractmethod

# 10 кеглей. 10 фреймов. До двух бросков в одном фрейме.
# Результаты фреймов:
#   «Х» – «strike», все 10 кеглей сбиты первым броском.
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные.
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
# Вместо <число> может стоять прочерк «-», например, «-4» - ни одной кегли не было сбито за бросок (первый или второй).


STRIKE_POINTS = 20
SPARE_POINTS = 15
SKITTLE_COUNT = 10
FRAME_COUNT = 10


class BowlingError(Exception):
    pass


class InputValueError(BowlingError):
    pass


class MaxFrameError(BowlingError):
    pass


class StrikeError(BowlingError):
    pass


class SpareError(BowlingError):
    pass


class Bowling:
    """
    Программа для подсчета очков игры в боулинг на основе результатов фреймов
    """

    def __init__(self, game_result, need_log=False):
        """
        :param game_result: результаты игры в боулинг (очки в виде записи фрейма)
        :param need_log: флаг для логирования
        """
        if need_log:
            self.LOG_LEVEL = logging.INFO
        else:
            self.LOG_LEVEL = logging.CRITICAL

        logging.basicConfig(level=self.LOG_LEVEL, filename='bowling_points.log', encoding='utf8',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if not game_result:
            logging.critical('Вы не указали результаты вашей игры!!!')
            raise AttributeError('Вы не указали результаты вашей игры!!!')

        self.game_result = game_result
        self.total_score = 0
        self.frame = 1

    def results_collection(self):
        """
        Запуск сбора результатов

        :return: Итоговое количество очков
        """
        first_throw = FirstThrow()
        second_throw = SecondThrow()
        first_hit, second_hit = 0, 0

        logging.info('=== NEW GAME ===')
        logging.info(f'< {self.game_result} >')

        throw = first_throw
        for throw_symbol in self.game_result:
            if self.frame > FRAME_COUNT:
                logging.critical(f'Превышено максимально возможное количество фреймов ({FRAME_COUNT})!!!')
                raise MaxFrameError(f'Превышено максимально возможное количество фреймов ({FRAME_COUNT})!!!')
            try:
                throw_score = throw.process(symbol=throw_symbol)
            except BowlingError as exc:
                logging.critical(f'{exc}')
                raise exc

            self.print_frame_result(throw=throw, throw_symbol=throw_symbol, throw_score=throw_score)

            if isinstance(throw, FirstThrow):
                if throw_score == STRIKE_POINTS:
                    throw = first_throw
                    self.total_score += STRIKE_POINTS
                    self.frame += 1
                else:
                    first_hit = throw_score
                    throw = second_throw
            else:
                if throw_score == SPARE_POINTS:
                    self.total_score += SPARE_POINTS
                else:
                    second_hit = throw_score
                    total_skittle_hits = first_hit + second_hit
                    if total_skittle_hits < SKITTLE_COUNT:
                        self.total_score += total_skittle_hits
                    else:
                        logging.critical('Результаты превышают количество кеглей!!! Проверьте данные!!!')
                        raise AttributeError('Результаты превышают количество кеглей!!! Проверьте данные!!!')
                self.frame += 1
                throw = first_throw

        logging.info(f'=== TOTAL SCORE - {self.total_score} ===')
        logging.info('=== END GAME ===')

        return self.total_score

    def print_frame_result(self, throw, throw_symbol, throw_score):
        if self.total_score > 0 and isinstance(throw, FirstThrow):
            logging.info(f'Итого очков: {self.total_score}')
        logging.info(f'FRAME_{self.frame} {throw} - "{throw_symbol}" ===> {throw_score}')


class Throw(ABC):
    """
    Создание класса броска
    """

    def process(self, symbol):
        """
        Считывание символов в результате
        :param symbol: символ
        :return: количество очков
        """
        if symbol == 'X':
            return self.strike()
        elif symbol == '/':
            return self.spare()
        elif symbol == '-':
            return 0
        elif '1' <= symbol <= '9':
            return int(symbol)
        else:
            raise InputValueError(f'Получен неверный символ "{symbol}"!!!')

    @abstractmethod
    def strike(self):
        """
        Получение очков для strike
        :return: None
        """
        pass

    @abstractmethod
    def spare(self):
        """
        Получение очков для spare
        :return: None
        """
        pass


class FirstThrow(Throw):
    """
    Создание первого броска
    """

    def strike(self):
        return STRIKE_POINTS

    def spare(self):
        raise SpareError('Spare "/" не может быть первым броском!!! Ошибка данных!!!')

    def __str__(self):
        return self.__class__.__name__


class SecondThrow(Throw):
    """
    Создание второго броска
    """

    def strike(self):
        raise StrikeError(f'Strike "X" не может быть вторым броском!!! Ошибка данных!!!')

    def spare(self):
        return SPARE_POINTS

    def __str__(self):
        return self.__class__.__name__


if __name__ == '__main__':
    try:
        bowling = Bowling(game_result='X12', need_log=False)
        print(bowling.results_collection())
    except (BowlingError, BaseException) as exc:
        print(f'Ошибка {exc}')
