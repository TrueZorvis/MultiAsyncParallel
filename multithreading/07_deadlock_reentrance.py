import threading

lock_obj = threading.Lock()
# lock_obj = threading.RLock()

print('acquire the 1st time')
lock_obj.acquire()

print('acquire the 2nd time')
lock_obj.acquire()

print('Releasing')
lock_obj.release()


# def reentrance():
#     print('start')
#     lock_obj.acquire()
#     print('acquired')
#     reentrance()
#
#
# reentrance()
