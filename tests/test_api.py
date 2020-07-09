import pytest
import requests
import gmap
import gmplot
import gmaps
from ipywidgets.embed import embed_minimal_html
import wikipedia

# key = "AIzaSyAm4J19gegHgeTzeZvg7g9MznXGdkVoivU"

# gmaps.configure(api_key=key)

# new_york_coordinates = (40.75, -74.00)
# fig = gmaps.figure(center=new_york_coordinates, zoom_level=12)

# embed_minimal_html('/Users/david/OpenClassrooms/P7/grandpy/static/img/export.html', views=[fig])

# gmap.apikey = key
# gmap = gmplot.GoogleMapPlotter(40.75, -74.00, 18)
# Location where you want to save your file.
# gmap.draw("/Users/david/OpenClassrooms/P7/grandpy/tests/map11.html")

def test_get_response_api_googlemaps():
     response = requests.get("http://api.zippopotam.us/us/90210")
     assert response.status_code == 200

# print(wikipedia.search("Coronavirus"))

