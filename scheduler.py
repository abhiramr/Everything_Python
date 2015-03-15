import time
import threading

def hello():
    print "Hello World"

def schedules():
    hello()
    schedules.n+=1
    print schedules.n
    threading.Timer(5, schedules).start()

schedules.n=1
schedules()
