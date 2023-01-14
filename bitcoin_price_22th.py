import requests as req

def inform():
    print('price is good!')

response = req.get('https://api.coinbase.com/v2/prices/spot\?currency\=USD')#,
                    #proxies={'https':'HTTP://192.168.1.4:51320'})
#print('at this moment, bitcoin is %i dollars' % float(response.json()['data']['amount']))
print(response.json)

price = float(response.json()['data']['amount'])
my_good_price = 25000

if (price<my_good_price):
    inform()