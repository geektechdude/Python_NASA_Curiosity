#!/bin/python3
#geektechstuff
#NASA Curiosity Photo Viewer
#Made possible thanks to NASA's open APIs

import json, requests, os
from PIL import Image

#create directory to save img file to
os.makedirs('nasa_cur', exist_ok=True)

#Variables
api_key='demo_key'
#API keys avaiable from api.nasa.gov

dd=''
mm=''
yyyy=''
earth_date=''
#Earth date in YYYY-MM-DD format

url=''
#blank to start

image=''
#blank to start

print("Hi and welcome to GeekTechStuff's NASA Curiosity Photo Viewer")
print("")
print("Curiosity is a NASA rover on the planet Mars.")
print("Curiosity landed on Mars on 6th August 2012")
print("")
print("Please use dates in the format of YYYY-MM-DD")
print("")
print("")
print("Let's pick a date range after 2012-08-06 to view images from")

#Takes date input from the user
dd=input('Pick a date (DD):')
mm=input('Pick a month (MM):')
yyyy=input('Pick a year (YYYY):')

earth_date=yyyy+'-'+mm+'-'+dd
earth_date=str(earth_date)
#print(earth_date)
earth_date2=yyyy+mm+dd
earth_Date2=int(earth_date2)

#Checks the date is after 6th August 2012
if earth_date2 < '20120806':
    
    print('You did not choose a date after 2012-08-06')
    
else:
    #Gets the JSON file
    url='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date='+earth_date+'&api_key='+api_key
    #print(url)
    response=requests.get(url)
    response.raise_for_status()
    rover_data=json.loads(response.text)
    #print(rover_data)
    rover_data2=rover_data["photos"]

    #Prints the day number on Mars
    sol=rover_data2[0]
    sol=sol['sol']
    print('This photo was taken on sol',sol,'of the Curiosity mission')

    #display the image
    img_src=rover_data2[0]
    img_src=img_src['img_src']
    #print(img_src)
    
    res=requests.get(img_src)
    res.raise_for_status()
    imageFile = open(os.path.join('nasa_cur', os.path.basename(img_src)),'wb')
    for part in res.iter_content(100000):
                     imageFile.write(part)
    imageFile.close()

    Image.open(os.path.join('nasa_cur', os.path.basename(img_src))).show()
    

    

    
