import json
import requests
url  = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"

response = requests.get(url=url)
data = json.loads (response.text)
print(len(data))
for i in data:
    if i.get('id') == 'bitcoin':
        print(i)
        break