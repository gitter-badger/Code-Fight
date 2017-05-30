import signal
import time

class Timeout():
    """Timeout class using ALARM signal."""
    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)    # disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout()

def timeout(func, second):
    def wrapper(*args):
        try:
            with Timeout(second):
                return func(*args)
        except Timeout.Timeout:
            raise Timeout.Timeout()
    return wrapper
