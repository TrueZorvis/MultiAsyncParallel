import random
import threading
import time
import datetime


class HorseRace:
    def __init__(self):
        self.barrier = threading.Barrier(parties=4)
        self.horses = ['Artex', 'Frankel', 'Bucephalus', 'Barton']

    def lead(self):
        horse = self.horses.pop()
        time.sleep(random.randrange(1, 5))
        print(f'\n{horse} reached the barrier at {datetime.datetime.now()}')
        self.barrier.wait()

        print(f'\n{horse} started at {datetime.datetime.now()}')

        time.sleep(random.randrange(1, 5))
        print(f'\n{horse} finished at {datetime.datetime.now()}')

        self.barrier.wait()
        print(f'\n{horse} went sleeping at {datetime.datetime.now()}')


if __name__ == '__main__':
    print('Prepare to racing')

    race = HorseRace()
    for x in range(4):
        thread = threading.Thread(target=race.lead)
        thread.start()
