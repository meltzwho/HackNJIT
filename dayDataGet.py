import requests
import json
import time
import numpy as np

inF = open('dayData.txt', 'r+')
fullData = inF.read()
data = json.loads(fullData)
req = requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json')
dataNew = req.json()
timeT = (dataNew['time']['updated'].split())[3].split(':')
absTime = (int(timeT[0]) * 60) + int(timeT[1])
if(absTime-data['latest'] > 1):
    for i in range(absTime-data['latest']):
        data['price'].append(np.nan)
    else:
        inF.write(json.dumps(data))
        inF.close()
else:
    inF.close()

if( 0 == absTime-data['latest'] ):
    time.sleep(60)
while True:
    req = requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json')
    dataNew = req.json()
    timeT = (dataNew['time']['updated'].split())[3].split(':')
    absTime = (int(timeT[0]) * 60) + int(timeT[1])
    data['latest'] = absTime
    data['price'].append(dataNew['bpi']['USD']['rate'])
    writer = open('dayData.txt', 'w')
    writer.write(json.dumps(data))
    writer.close()
    time.sleep(60)