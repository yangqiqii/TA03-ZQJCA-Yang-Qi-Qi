import requests
import json

api_key = "RGC6YA5ZJFKM6OPR"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}"
response = requests.get(url)
data = response.json()
#data.keys()
#json.dumps(data["Realtime Currency Exchange Rate"], indent = 4)
forex = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

def api():
    """
    Function does not require parameter 
    Function returns real time currency conversion rate from USD to SGD
    """
    print(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}")
api()