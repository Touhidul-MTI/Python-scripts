#install python 3 and requests first
import requests
import json

web_url = 'http://freegeoip.net/json'
req = requests.get(web_url)
json_data = json.loads(req.text)

latitude = json_data['latitude']
longitude = json_data['longitude']
country = json_data["country_name"]
ip = json_data["ip"]

print("latitude: ",latitude)
print("longitude: ",longitude)
print("country:", country)
print("ip", ip)
