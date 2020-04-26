import requests

request = requests.get(
    "https://www.johnlewis.com/philippe-starck-for-kartell-masters-chair/black/p326288"
)

# <p class="price price--large">£177.00 </p>

# Returns the full html code of the requested page.
print(request.content)
