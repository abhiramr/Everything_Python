import time,sys

def report_progress(ratio,width = 50):
    filled = '='* int(ratio*width)
    rest = '-' * (width - int(ratio*width))
    sys.stderr.write('\r|'+filled+rest+'|')
    sys.stderr.flush()

for i in range(101):
    report_progress(i/100.0,50)
    time.sleep(.01)
print('\n')
