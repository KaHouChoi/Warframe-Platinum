import requests

def price(items):
    for i in items:
        
        url = items[i].get("url_name")
        response = requests.get(f"https://api.warframe.market/v1/items/{url}/orders")
        print(response.json())

    return items