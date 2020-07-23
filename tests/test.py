import requests
import os

api_key = (os.environ['api_google_key'])
# url variable store url 
url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# center defines the center of the map, 
# equidistant from all edges of the map.  
center = "Ecouen"
  
# zoom defines the zoom 
# level of the map 
zoom = 15
  
# get method of requests module 
# return response object 
r = requests.get(
    url + "center=" + center + "&zoom=" +
    str(zoom) + "&size=400x400" + "&key=" +
    api_key
    ) 
  
# wb mode is stand for write binary mode 
f = open(
    '/Users/david/OpenClassrooms/P7/grandpy/P7_GrandPy-Bot/tests/test.png',
    'wb') 
  
# r.content gives content, 
# in this case gives image 
f.write(r.content) 
  
# close method of file object 
# save and close the file 
f.close() 

# https://maps.googleapis.com/maps/api/staticmap?center=Albany,+NY&zoom=13&scale=1&size=600x300&maptype=roadmap&format=png&visual_refresh=true&key=
