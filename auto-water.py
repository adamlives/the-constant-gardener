import RPi.GPIO as gpio
import time
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

def send_notification(mail_to, mail_subject, mail_text):
    gmail_SENDER = 'adamshackleton1310@gmail.com'
    gmail_PASSWORD = ''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_SENDER, gmail_PASSWORD)

    mail_body = '\r\n'.join(['To: %s' % mail_to,
                         'From: %s' % gmail_SENDER,
                         'Subject: %s' % mail_subject,
                         '', mail_text])

    try:
        server.sendmail(gmail_SENDER, [mail_to], mail_body)
        print('email sent')
    except:
        print('error')

    server.quit()

def update_last_watered(plant):
    headers = {'Content-Type': 'application/json'}
    body = {'name': plant}
    url = 'https://192.168.1.81/gardener/api/v1.0/setWatered'
    r = requests.put(url=url, json=body, headers=headers, verify=False)
    if r.status_code == 200:
    	send_notification('adamlives@hotmail.com', 'Plant Last Watered Updated', plant + ' watered and last watered time has been updated')
    else:
        send_notification('adamlives@hotmail.com', 'Update failed', "Couldn't update last watered time for " + plant)

def pump_water(pin=18):
    print("Pumping")
    gpio.setup(pin, gpio.OUT)
    time.sleep(5)
    gpio.cleanup(pin)
    # send_notification('adamlives@hotmail.com', 'Plant Watered', 'Plant has been watered')

def setup_input(channel=17):
    print("setup input channel")
    gpio.setmode(gpio.BCM)
    gpio.setup(channel, gpio.IN)
    # gpio.add_event_detect(channel, gpio.BOTH, bouncetime=300)
    # gpio.add_event_callback(channel, callback)

logging.basicConfig(filename="watering.log", level=logging.DEBUG, format='%(asctime)s %(message)s')

channel = 17
setup_input(channel)

input_value = gpio.input(channel)
print("Input value:", input_value)
logging.info("Input Value: %d", input_value)
if input_value:
    print("pumping water")
    # send_notification('adamlives@hotmail.com', 'Plant too dry', 'The plant is now too dry')
    pump_water(18)
    update_last_watered('Marcus')
