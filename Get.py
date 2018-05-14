import requests
import json
import codecs
import os

_ApiKey=''


def saveInStockFromApi():
    r = requests.get('https://api.torn.com/company/67815?selections=stock&key=' + _ApiKey)
    data = r.json()

    if data["error"]
        pass
    else:        
        fname = 'inStock.txt'
        if os.path.isfile(fname):
            try:
                print('File removed')
                os.remove(fname)
            except IOError as identifier:
                print(identifier)
                exit()
            
            try:
                with open(fname, 'wb') as f:
                    json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)
                    print('New file created')
            except IOError as identifier:
                print(identifier)
                exit()

        else:
            try:
                with open(fname, 'wb') as f:
                    json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)
                    print('New file created')
            except IOError as identifier:
                print(identifier)
                exit()