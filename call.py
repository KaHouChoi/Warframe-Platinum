import requests

response = requests.get("https://api.warframe.market/v1/items") 
print(response.json())