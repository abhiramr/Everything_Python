import time
import subprocess

def current_time():
    print("The current time is :")
    print(str(subprocess.check_output(['date']))[2:-3])

def stopwatch():
    try:
        num=int(input("Enter the minute upto which you want the stopwatch:"))
        while int(str(subprocess.check_output(['date']))[16:18])< num:
            print((str(subprocess.check_output(['date'])))[16:21])
            time.sleep(1)
        print("TIME UP!")
    except ValueError:
        print("Enter a valid integer.")
        current_time()
        stopwatch()

if __name__=='__main__':
    current_time()
    stopwatch()
