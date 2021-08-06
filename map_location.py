import requests
from flask import Flask,render_template

"""

r.json()
{'items': [{'title': 'London, England', 'id': 'here:cm:namedplace:20337454', 'resultType': 'locality', 'localityType': 'city', 'address': {'label': 'London, England', 'countryCode': 'GBR', 'countryName': 'England', 'county': 'London', 'city': 'London', 'postalCode': 'SW1A 2'}, 'position': {'lat': 51.50643, 'lng': -0.12719}, 'mapView': {'west': -0.56316, 'south': 51.28043, 'east': 0.28206, 'north': 51.68629}, 'scoring': {'queryScore': 1.0, 'fieldScore': {'city': 1.0}}}]}

"""


URL = "https://geocode.search.hereapi.com/v1/geocode"
location = input("Enter the location here: ") #taking user input
#api_key = 'YOUR_API_KEY' # Acquire from developer.here.com

api_key = 'GEx9WHfF8QfmVMEXlDPc_fXFDZrpbFZGGxw4uDt1sxQ'
PARAMS = {'apikey':api_key,'q': location}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
data = r.json()
#print(data)

#Acquiring the latitude and longitude from JSON
latitude = data['items'][0]['position']['lat']
#print(latitude)
longitude = data['items'][0]['position']['lng']
#print(longitude)

#Flask code
app = Flask(__name__)
@app.route('/')

def map_func():
	return render_template('map_by_coordinate.html.jinja',apikey=api_key,latitude=latitude,longitude=longitude)#map_by_coordinate.html.jinja is my HTML file name

if __name__ == '__main__':
    app.run(debug = False)

