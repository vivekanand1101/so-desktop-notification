import sys
import requests
from bs4 import BeautifulSoup
from time import sleep
import notify2

def send_message(title, message):
    notify2.init("Init")
    notice = notify2.Notification(title, message)
    notice.show()
    sleep(4)
    notice.close()
    return

def main(argv):
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: python script.py <tags with spaces in between> \n')
        sys.stderr.write('Ctrl-C to close the program \n')
        return True

    try:
        tags = []
        for i in sys.argv[1:]:
            url = "http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest" % i
            r = requests.get(url)
            if r.status_code == 404:
                sys.stderr.write('Please check the tag \n')
                sys.stderr.write('The following url should not return 404: \n')
                sys.stderr.write('http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest \n' % i)
                return True
            tags.append(i)
        while True:
            for i in tags:
                url = "http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest" % i
                r = requests.get(url)
                while r.status_code is not 200:
                        r = requests.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                data = soup.find_all("link")
                question = data[2].get('href')
                question = question[question.find('questions') + 19:]
                send_message("Question %s: " % i.upper(), question)
            sleep(60)
    except KeyboardInterrupt:
        sys.stderr.write('\nBye \n')
        return True

if __name__ == "__main__":
    sys.exit(main(sys.argv))
