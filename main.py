import time

class DistributedLock:
    locked = False

    def acquire(self):
        if DistributedLock.locked:
            return False
        DistributedLock.locked = True
        return True

    def release(self):
        DistributedLock.locked = False

lock = DistributedLock()

if lock.acquire():
    print("Working safely...")
    time.sleep(2)
    lock.release()
