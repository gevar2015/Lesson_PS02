import requests
import pprint

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Текстовый Post запрос title",
    "foo": "Текстовый Post запрос foo",
    "body": "Текстовый Post запрос content",
    "bar": "Текстовый Post запрос bar",
    "userId": 1
}

response = requests.post(url, data=data)

print(response.status_code)
print(f"Ответ - {response.json()}")



