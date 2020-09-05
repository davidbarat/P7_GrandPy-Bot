import os
import sys
import cgi
import json
import requests
from stop_words import stops
import wikipedia


class ApiGoogle():

    def __init__(self):
        
        self.url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        
    def getKey(self):

        if 'api_google_key' in os.environ:
            self.api_google_key = os.environ['api_google_key']

        return(self.api_google_key)

    def search_api_google(self, search_post):

        self.response = requests.get(
            self.url + "input=" + str(search_post)
            + "&inputtype=textquery&fields=formatted_address,geometry,rating" +
            "&key=" +
            self.api_google_key)

        print('search post ' + search_post)
        self.response_json = self.response.json()
        if self.response_json['status'] != 'OK':
            return(False)

        else:
            self.best_resultat = self.response_json['candidates'][-1]
            self.lat = str(
                self.best_resultat['geometry']['location']['lat'])
            self.lng = str(
                self.best_resultat['geometry']['location']['lng'])
            self.formatted_address = str(
                self.best_resultat['formatted_address'])

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
        self.summary_wiki = str(
            wikipedia.summary(self.res_wiki[0], sentences=1))
        self.summary_wiki_clean = (self.summary_wiki.replace("'", " "))
        self.url_wiki = wikipedia.page(self.res_wiki[0]).url
        return(self.summary_wiki_clean, self.url_wiki)
