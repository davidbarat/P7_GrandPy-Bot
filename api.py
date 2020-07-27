import os
import sys
import cgi
import json
import requests
from stop_words import stops
from boto.s3.connection import S3Connection


class ApiGoogle():

    def __init__(self):
    
        if 'api_google_key' in os.environ:
            self.api_google_key = os.environ['api_google_key']
        else:
            self.api_google_key = S3Connection(os.environ['api_google_key'])
        
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?"

    def search_api_google(self, search_post):

        self.response = requests.get(
            self.url + "address=" + str(search_post) + "&key=" + 
            self.api_google_key)
    
        self.response_json = self.response.json()
        self.lat = self.response_json['results'][0]['geometry']['location']['lat']
        self.lng = self.response_json['results'][0]['geometry']['location']['lng']
        return(self.lat, self.lng)


class ApiWikipedia():

    def __init__(self):

        self.url_wiki = "https"
