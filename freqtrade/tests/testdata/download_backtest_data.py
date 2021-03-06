#!/usr/bin/env python3

"""This script generate json data from bittrex"""

from urllib.request import urlopen

CURRENCIES = ["ok", "neo", "dash", "etc", "eth", "snt"]

for cur in CURRENCIES:
    url1 = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=BTC-'
    url = url1+cur+'&tickInterval=fiveMin'
    x = urlopen(url)
    json_data = x.read()
    json_str = str(json_data, 'utf-8')
    with open('btc-'+cur+'.json', 'w') as file:
        file.write(json_str)
