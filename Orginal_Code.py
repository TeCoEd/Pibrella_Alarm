#A Simple door alarm:

import pibrella as pib
import signal
import time
import smtplib
import datetime

##pib.light.off()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login("your_email_address_here", "your_password_here")

def send_an_email(state):
    if state ==True:
        message = "THE DOOR IS CLOSED SAFE"
    else:
        message = "THE DOOR IS OPEN QUICK CHECK IT"
    server.sendmail("your_email_address_here", "their_adresss", message)

while True:
    time_of_event = time.asctime(time.localtime(time.time()))
    if pib.input.a.read()==1:
        pib.buzzer.off()
        print "THE DOOR IS NOW CLOSED " + time_of_event
        pib.light.red.off()
        pib.light.green.on()
        send_an_email(True)
        time.sleep(5)

    elif pib.input.a.read()==0:
        Open_Time = time_of_event
        print"THE DOOR IS OPEN THE CAT/CHILD HAS ESCAPED " + Open_Time
        pib.light.green.off()
        pib.light.red.blink(0.7, 0.3)
        send_an_email(False)
        pib.buzzer.fail()
        time.sleep(5)
        
signal.pause()
