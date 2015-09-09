import sys
import requests
from bs4 import BeautifulSoup
from time import sleep
import notify2

def send_message(title, message):
    notify2.init("Init")
    notice = notify2.Notification(title, message)
    notice.show()
    return

def main(argv):
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: python script.py <tag> \n')
        sys.stderr.write('Ctrl-C to close the program \n')
        return True

    try:
        url = "http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest" % sys.argv[1]
        while True:
            r = requests.get(url)
            while r.status_code is not 200:
                    r = requests.get(url)
            soup = BeautifulSoup(r.text)
            data = soup.find_all("link")
            question = data[2].get('href')
            question = question[question.find('questions') + 19:]
            send_message("Question %s: " % sys.argv[1].upper(), question)
            sleep(60)
    except KeyboardInterrupt:
        sys.stderr.write('\nBye \n')
        return True

if __name__ == "__main__":
    sys.exit(main(sys.argv))
