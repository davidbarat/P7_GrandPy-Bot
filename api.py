import os
import sys
import cgi
import json
# import gmaps
import requests
from stop_words import stops
from boto.s3.connection import S3Connection


class ApiGoogle():

    def init_api_maps(self):
    
        if 'api_google_key' in os.environ:
            self.api_google_key = os.environ['api_google_key']
        else:
            self.api_google_key = S3Connection(os.environ['api_google_key'])
        
        # gmaps.configure(api_key=self.api_google_key)
        self.url =  "https://maps.googleapis.com/maps/api/staticmap?"
        self.zoom = 17

    
    def search_api_google(self, search_post):

        self.r = requests.get(
            self.url + "center=" + str(search_post) + "&zoom=" +
            str(self.zoom) + "&size=400x400" + "&markers=color:red" + "&key="
            + self.api_google_key
            ) 

        self.f = open(
            '/Users/david/OpenClassrooms/P7/grandpy/P7_GrandPy-Bot/tests/test.png', 
            'wb') 
        self.f.write(self.r.content) 
        self.f.close() 

        

class ApiWikipedia():

    def __init__(self):
        print('test')
