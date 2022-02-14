#1
import multiprocessing
import random
import time


def print_time():
    value = random.randint(0, 100) / 100
    time.sleep(value)
    print("I slept for ", value, " seconds")


if __name__ == '__main__':
    for n in range(3):
        proc = multiprocessing.Process(target=print_time)
        proc.start()
