import os
import sys
import cgi
import json
import requests
from stop_words import stops
from boto.s3.connection import S3Connection
import wikipedia


class ApiGoogle():

    def __init__(self):
        
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?"


    def getKey(self):

        if 'api_google_key' in os.environ:
            self.api_google_key = os.environ['api_google_key']
        else:
            self.api_google_key = S3Connection(os.environ['api_google_key'])

        return(self.api_google_key)

    def search_api_google(self, search_post):

        self.response = requests.get(
            self.url + "address=" + str(search_post) + "&language=fr" + "&key=" + 
            self.api_google_key)
        print('search post ' + search_post)
        self.response_json = self.response.json()
        print('response from google')
        print(self.response_json)
        self.lat = str(self.response_json['results'][0]['geometry']['location']['lat'])
        self.lng = str(self.response_json['results'][0]['geometry']['location']['lng'])
        self.formatted_address = str(self.response_json['results'][0]['formatted_address'])

        return(
            self.lat, 
            self.lng, 
            self.api_google_key,
            self.formatted_address)


class ApiWikipedia():

    def __init__(self):

        wikipedia.set_lang("fr")  

    def search_api_wikipedia(self, lat, lng):

        self.res_wiki = wikipedia.geosearch(lat, lng)
        self.summary_wiki = str(wikipedia.summary(self.res_wiki[0], sentences=1))
        self.summary_wiki_clean = (self.summary_wiki.replace("'", " "))
        self.url_wiki = wikipedia.page(self.res_wiki[0]).url
        return(self.summary_wiki_clean, self.url_wiki)
