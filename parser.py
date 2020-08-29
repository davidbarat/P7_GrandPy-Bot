import os
import sys
import cgi
import json
from stop_words import stops


class Parser():


    def delete_stopwords(self, search_post):

        self.clean_search_post = ''
        self.list_search_post = search_post.split(" ")
        self.clean_search_post = [word for word in self.list_search_post if word.lower() not in stops]
        self.clean_search_post = [i.replace("'", "") for i in self.clean_search_post]
        print(self.clean_search_post)
        return(self.clean_search_post)