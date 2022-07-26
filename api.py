import requests
import json
api_key = "RGC6YA5ZJFKM6OPR"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}"
response = requests.get(url)

data = response.json()
print(data.keys())
print(json.dumps(data["Realtime Currency Exchange Rate"], indent = 4))