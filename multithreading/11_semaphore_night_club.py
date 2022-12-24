import threading
import time


class NightClub:
    def __init__(self):
        self.bouncer = threading.Semaphore(value=3)

    def guest(self, guest_id):
        print(f'\nguest {guest_id} is waiting for entering the night club')
        self.bouncer.acquire()

        print(f'\nguest {guest_id} is dancing')
        time.sleep(1)

        print(f'\nguest {guest_id} is leaving the night club')
        self.bouncer.release()

    def open_club(self):
        for x in range(1, 51):
            t = threading.Thread(target=self.guest, args=[x])
            t.start()


if __name__ == '__main__':
    club = NightClub()
    club.open_club()
