import os
import sys
import polib
import requests
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()


def check_kateglo(word):
    r = requests.get('http://kateglo.com/api.php?format=json&phrase=' + word)
    return (r.headers.get('content-type') == 'application/json')


def process(filepath):
    print('# Processing :' + filepath)
    po = polib.pofile(filepath)
    suspicious = []
    for entry in po:
        output = stemmer.stem(entry.msgstr.encode('utf-8')).split(' ')
        for word in output:
            if word and not check_kateglo(word):
                suspicious.append(word)
    print(suspicious)
    print('\n')


def tranverse(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            if (file_[-3:] == '.po'):
                filepath = os.path.join(root, file_)
                process(filepath)


if __name__ == '__main__':
    if (len(sys.argv) >= 2):
        p = sys.argv[1]
        if (os.path.isfile(p) and p[-3:] == '.po'):
            process(p)
        elif (os.path.isdir(p)):
            tranverse(p)
        else:
            print 'Not a path nor po file path'
    else:
        print('Usage : python checker_id.py /path/to/tranverse')
