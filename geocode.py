import requests
import json

API_KEY = "AIzaSyANKZenrKFyT1N5dC427dHbo_-BAD1DmA4"
BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

# function to convert an address to coordinates
# function input should be a string of an address
# such as "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"
# function returns a tuple of (lat, lng)

## feel free to change or edit

def get_coordinate(addr):
	params_dict = {}
	params_dict["address"] = addr
	params_dict["key"] = API_KEY

	resp = requests.get(BASE_URL, params = params_dict)
	resp_dict = json.loads(resp.text)
	lat = resp_dict["results"][0]["geometry"]["location"]["lat"]
	lng = resp_dict["results"][0]["geometry"]["location"]["lng"]

	return (lat, lng)


#addr1 = "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"

#print(get_coordinate(addr1))
