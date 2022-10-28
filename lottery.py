import random

from crud import *


def init_db():
    init_prefix_table()
    init_root_table()
    init_suffix_table()
    print('init db')


def lottery(type):
    times = 0
    while True:
        vocabularies = select_vocabularies(type, times)
        if len(vocabularies) == 0:
            times += 1
        else:
            lottery = random.randint(0, len(vocabularies) - 1)
            update_times(type, vocabularies[lottery][0], times + 1)
            print(f'{type}: {vocabularies[lottery][0]} (the {times + 1} time)')
            return


def drawing():
    lottery('prefix')
    lottery('root')
    lottery('suffix')
