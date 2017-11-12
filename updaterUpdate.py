plt.ion()
plt.plot(x, y)
plt.pause(.001)
while True:
    req = requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json')
    dataNew = req.json()
    timeT = (dataNew['time']['updated'].split())[3].split(':')
    absTime = (int(timeT[0]) * 60) + int(timeT[1])
    data['latest'] = absTime
    data['price'].append(dataNew['bpi']['USD']['rate_float'])
    x = np.linspace(0, len(data['price']), len(data['price']))
    y = data['price']
    plt.clf()
    plt.plot(x, y)
    plt.pause(.001)
    plt.show(block=False)
    plt.pause(60)