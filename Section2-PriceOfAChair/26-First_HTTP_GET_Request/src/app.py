import requests

request = requests.get("http://www.google.com")

# Returns the full html code of the requested page.
print(request.content)
