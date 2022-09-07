import time, threading
import datetime

x = 0
my_time = None

def foo():
    print(x, "  ", my_time)
    threading.Timer(5, foo).start()

foo()

while(1):
    x = x + 1
    my_time = datetime.datetime.now()
