import pytest
import requests
import gmaps
import wikipedia
import json
import os
import geojson
import re


def test_search_api_google():
    api_gmap_key = (os.environ['api_google_key'])
    url_maps = 'https://www.google.com/maps/search/?api=1&'
    parameters = 'ecouen'
    url_maps_json = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    response = requests.get(url_maps + parameters)
    assert response.status_code == 200
    response = requests.get(
         url_maps_json + parameters + '&key=' + api_gmap_key
         )
    response_body = response.json()
    assert response_body[
         "results"][0]["address_components"][0]["short_name"] == 'Écouen'
    
    # print(response.json())

def test_search_api_wikipedia():
    lat_ecouen = 49.018834
    lng_ecouen = 2.378926
    list_res = ["Château d'Écouen", 'Écouen']
    res_wiki = wikipedia.geosearch(
         lat_ecouen, lng_ecouen)
    assert all([a == b for a, b in zip(res_wiki, list_res)])
