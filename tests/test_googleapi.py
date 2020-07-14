import pytest
import requests
import gmap
import gmplot
import gmaps
from ipywidgets.embed import embed_minimal_html
import wikipedia
import json
from boto.s3.connection import S3Connection
import os

api_google_key = S3Connection(os.environ['api_google_key'])

# api_google_key = "AIzaSyAm4J19gegHgeTzeZvg7g9MznXGdkVoivU"

gmaps.configure(api_key=api_google_key)

new_york_coordinates = (40.75, -74.00)
fig = gmaps.figure(center=new_york_coordinates, zoom_level=12)

embed_minimal_html('/Users/david/OpenClassrooms/P7/grandpy/P7_GrandPy-Bot/static/img/export.html', views=[fig])

# gmap.apikey = key
# gmap = gmplot.GoogleMapPlotter(40.75, -74.00, 18)
# Location where you want to save your file.
# gmap.draw("/Users/david/OpenClassrooms/P7/grandpy/tests/map11.html")

api_google_key = "AIzaSyAm4J19gegHgeTzeZvg7g9MznXGdkVoivU"

url_maps = 'https://www.google.com/maps/search/?api=1&'
parameters = 'ecouen'
url_maps_json = 'https://maps.googleapis.com/maps/api/geocode/json?address='
def test_get_response_api_googlemaps():
     response = requests.get(url_maps + parameters)
     assert response.status_code == 200
     response = requests.get(url_maps_json + parameters + '&key=' + api_google_key)
     # assert response_body["places"][0]["place name"] == "Beverly Hills"
     # response_body = response.json()
     # print(response.json())

# print(wikipedia.search("Coronavirus"))


# https://fr.wikipedia.org/w/api.php?action=opensearch&search=ecouen