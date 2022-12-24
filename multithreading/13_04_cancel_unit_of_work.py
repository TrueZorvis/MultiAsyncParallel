import threading
import time

from multithreading.count_three_sum import read_ints


class ThreeSumUnitOfWork(threading.Thread):
    def __init__(self, ints, name='TestThread'):
        super().__init__(name=name)
        self.ints = ints
        self.stop_event = threading.Event()

    def run(self):
        print(f'{self.name} starts')
        self.count_three_sum(self.ints)
        print(f'{self.name} ends')

    def cancel(self):
        self.stop_event.set()

    def count_three_sum(self, ints, thread_name='t'):
        print(f'started count_three_sum in thread {thread_name}')

        n = len(ints)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    if self.stop_event.is_set():
                        print('task was cancelled')
                        counter = -1
                        return counter

                    if ints[i] + ints[j] + ints[k] == 0:
                        counter += 1
                        print(f'Triple found in thread {thread_name}: {ints[i]}, {ints[j]}, {ints[k]}')
        print(f'ended count_three_sum in thread {thread_name}. triplets count: {counter}')
        return counter


if __name__ == '__main__':
    print('started main')

    ints = read_ints('..\\data\\1Kints.txt')
    task = ThreeSumUnitOfWork(ints)
    task.start()

    time.sleep(3)

    task.cancel()

    task.join()

    print('end main')
