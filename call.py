import requests

def call():
    response = requests.get("https://api.warframe.market/v1/items") 

    with open("items.txt", "w") as f:
      print(response.json(), file=f)