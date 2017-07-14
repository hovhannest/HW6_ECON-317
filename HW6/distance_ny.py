import requests

key = ""

origin = 'New York, NY'

origin = origin.replace(" ", "+")
origin = origin.replace(",", "%2C")

destinations = ['Philadelphia, PA', 'Pittsfield, MA', 'Boston, MA', 'Providence, RI', 'Hartford, CT',
'Stamford, CT', 'Brick, NJ', 'Washington, DC', 'Allentown, PA', 'Albany, NY']

for i in range(len(destinations)):
	destinations[i] = destinations[i].replace(" ", "+")
	destinations[i] = destinations[i].replace(",", "%2C")

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origin + "&destinations="

# I can't "calculate" the distances inside a for loop, but I can request the distance for each sity (10 calls),
# but the best approche is to request 10 distances in 1 call (less time to waith for network responce + less money to spend on google)

for i in range(len(destinations)):
	url += destinations[i] + "|"

if url[-1] == "|":
	url = url[:-1]

if key != "":
	url += "&key=" + key

res = requests.get(url)

j = res.json()

destinations = j['destination_addresses']
origin = j['origin_addresses'][0]
distances = j['rows'][0]['elements']

for i in range(len(destinations)):
	print("Distance from " + origin + " to " + destinations[i] + " is " + distances[i]['distance']['text'])