import os
import sys
import cgi
import json
# import gmaps
import requests
from stop_words import stops
from boto.s3.connection import S3Connection


class Parser():


    def delete_stopwords(self,search_post):

        self.clean_search_post = ''
        self.list_search_post = search_post.split(" ")
        # print(self.list_search_post)
        self.clean_search_post = [word for word in self.list_search_post if word.lower() not in stops]
        print(self.clean_search_post)
        return(self.clean_search_post)