import requests

response = requests.get(
    "https://www.johnlewis.com/2020-apple-ipad-pro-12-9-inch-a12z-bionic-ios-wi-fi-256gb/space-grey/p4949087"
)
print(response.content)
