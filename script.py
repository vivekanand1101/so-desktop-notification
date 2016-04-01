import sys
import requests
from bs4 import BeautifulSoup
from time import sleep

from App import *

def is_valid_syntax(argv):
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: python script.py <tags with spaces in between> \n')
        sys.stderr.write('Ctrl-C to close the program \n')
        return False
    else:
        return True

def is_valid_tag(tag):
    url = "http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest" % tag
    r = requests.get(url)
    if r.status_code == 404:
        sys.stderr.write('Please check the tag(s) %s \n' % tag)
        sys.stderr.write('The following url should not return 404: \n')
        sys.stderr.write('http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest \n' % tag)
        sys.stderr.write('Processing other tag(s)... \n')
        return False
    else:
        return True

def get_question_from_tag(tag, last_ques):
    url = "http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest" % tag
    r = requests.get(url)
    while r.status_code is not 200:
        r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all("link")
    qurl = data[2].get('href')
    print qurl
    question = qurl[qurl.find('questions') + 19:]
    if last_ques[str(tag)] != str(question):
        app = App(tag.upper() + '\n' + qurl)

def main(argv):
    if is_valid_syntax(argv):
        try:
            tags = []
            last_ques = {}
            for i in sys.argv[1:]:
                if is_valid_tag(i):
                    tags.append(i)
                    last_ques[str(i)] = ' '
            while True:
                for tag in tags:
                    get_question_from_tag(tag, last_ques)
                sleep(60)
        except KeyboardInterrupt:
            sys.stderr.write('\nBye \n')
            return True
    else:
        return True

if __name__ == "__main__":
    sys.exit(main(sys.argv))
