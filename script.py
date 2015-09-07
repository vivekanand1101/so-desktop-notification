from sys import argv
import requests
from bs4 import BeautifulSoup
#from notify2 import notify2
from time import sleep
import notify2
def send_message(title, message):
    notify2.init("Init")
    notice = notify2.Notification(title, message)
    notice.show()
    return

url = "http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest" % argv[1]
while True:
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text)
    data = soup.find_all("link")
    question = data[2].get('href')
    question = question[question.find('questions') + 19:]
    send_message("Question %s: " % argv[1].upper(), question)
    sleep(60)
