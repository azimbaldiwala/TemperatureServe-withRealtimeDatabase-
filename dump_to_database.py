from scraper import get_values
from database import insert_data
from time import sleep


# Runs in background...


def dump():
    while True:
        t, h = get_values()
        insert_data(t, h)
        sleep(120)
        print('Data inserted into database')

dump()