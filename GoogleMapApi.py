### Get geocode with address
## 1. Via URL
import requests

response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA')

resp_json_payload = response.json()

print(resp_json_payload['results'][0]['geometry']['location'])

## 2. Via google api library
import googlemaps

api_key = 'AIzaSyDwD9nM2ji-RaosF3daGGluzLpB0KYBhxY'
gmaps = googlemaps.Client(key=api_key)
# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print(geocode_result[0]['geometry']['location'])
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
