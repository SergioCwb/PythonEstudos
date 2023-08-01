import requests, json
import pprint

url = "https://jsonplaceholder.typicode.com/todos/"
# params = {"q":"Girls"}

response = requests.get(url)

data = json.loads(response.text)

print(f"Achei {len(data)} itens no array")

i = 1
for item in data:
    print(f"Título {i}: {item['title']}")
    i += 1