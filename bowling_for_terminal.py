# -*- coding: utf-8 -*-
import argparse
import bowling_engine


def terminal_results_collection():
    """
    Консольная программа для подсчета очков игры в боулинг на основе результатов фреймов

    :return: None
    """
    parser = argparse.ArgumentParser(
        description='Утилита для подсчета результата партии на основе данных результатов бросков', add_help=True
    )
    parser.add_argument('-result', '--result', type=str, help='Результат введенных данных бросков')
    args = parser.parse_args()

    if args.result:
        bowling = bowling_engine.Bowling(game_result=args.result, need_log=True)
        print(bowling.results_collection())
    else:
        print('Укажите параметры или воспользуйтесь --help')


if __name__ == '__main__':
    terminal_results_collection()
