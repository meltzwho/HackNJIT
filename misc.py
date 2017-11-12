import requests
import json
import numpy as np

def beginDay():
    writer = open('dayDataFormal.txt', 'w')
    req = requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json')
    dataBeg = req.json()
    timeT = (dataBeg['time']['updated'].split())[3].split(':')
    absTime = (int(timeT[0])*60)+int(timeT[1])
    store = { 'start' : absTime, 'latest' : absTime, 'price' : [dataBeg['bpi']['USD']['rate']] }
    writer.write(json.dumps(store))
    writer.close()

## Do in day loop before function call
inF = open('dayData.txt', 'r+')
fullData = inF.read()
data = json.loads(fullData)


## Inside looped function

x = np.linspace(0, len(data['price']), len(data['price']))
y = data['price']
ax.clear()
ax.plot(x, y)