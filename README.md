Grandpy
-------

The purpose of this project is to allow user to ask to GrandPy an address request. Then GrandPy, if he is kind,
will transfer your demand to Google place and Wikipedia. In addition the web site will display a map with a marker
and a wikipedia link associated to user search.
The user can type several searches, they will be displayed line by line in a scrollbar.
If GrandPy doesn't known the address, he will display a message...
Don't be too insistent, GrandPy is old.

## Main steps of the script
1. The user fullfill a form,
2. Application applies a filter via a stopwords list to the user search, 
3. Then the application call api google place to retrieve lat/lng of the address and displays a map with a red marker,
4. Moreover, with lat / lng previously found, there is an another call, to wikipedia api this time to retreive a short story about the user search
and the url link associated to user search.

## class ApiGoogle
* def getKey:
	* get api google secret key
* def search_api_google:
	* do api call
  * get api response
  * create the dictionnary response
	
## class ApiWikipedia
* def search_api_wikipedia:
	* call api wikipedia by lat/lng criteria
  * return wikipedia summary and link

## class Parser
* def delete_stopwords:
	* load stopword list
  * delete stopword in user search and return the result

## Prerequisite
* get your api google key visit https://developers.google.com/maps/gmp-get-started

## Installing

Fork the project on your local machine and launch the script via these commands:

    pip install -r requirements.txt
    python app.py
