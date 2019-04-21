''' Script to send a test mail'''

import smtplib
import os

FROM_ADDR = 'abhi.darkness@gmail.com'
TO_ADDR = 'abhi.darkness@gmail.com'
MSG = "What's up2"
USERNAME = 'abhi.darkness@gmail.com'
PASSWORD = os.environ["DUMMY_PASSWORD"]
SERVER = smtplib.SMTP('smtp.gmail.com:587')
SERVER.ehlo()
SERVER.starttls()
SERVER.login(USERNAME, PASSWORD)
SERVER.sendmail(FROM_ADDR, TO_ADDR, MSG)
SERVER.quit()
