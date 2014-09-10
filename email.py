import smtplib
fromaddr='abhi.darkness@gmail.com'
toaddr='abhi.darkness@gmail.com'
msg ="What's up"
username='abhi.darkness@gmail.com'
password='password'
server=smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr,toaddr,msg)
server.quit()






