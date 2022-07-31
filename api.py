# Import modules to run code
import requests
import json

# Assign api key to the variaable "api_key"
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
    # Assign 
    api_key = "RGC6YA5ZJFKM6OPR"
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}"
    response = requests.get(url)
    data = response.json()
    # Use data.keys() to 
    #json.dumps(data["Realtime Currency Exchange Rate"], indent = 4)
    forex = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    return f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}"
print(api())