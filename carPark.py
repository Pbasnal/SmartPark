import pprint

print "hello"

import requests
url = 'https://...'
payload = {'ParkingZone': parking.ParkingZone, 'Cars': parking.Cars}

# POST with form-encoded data
r = requests.post(url, data=payload)