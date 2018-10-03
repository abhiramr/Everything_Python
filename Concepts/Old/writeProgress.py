from datetime import datetime
import sys

def writeProgress(timeNow, currentStatus):
    with open("./Progess.txt", "a") as myfile:
        myfile.write("\n"+timeNow+":"+currentStatus)


currentTime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
writeProgress(currentTime,sys.argv[1])


