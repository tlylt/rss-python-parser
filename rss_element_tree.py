import requests
import xml.etree.ElementTree as ET
import json
mytree = ET.parse('rss.xml')
myroot = mytree.getroot()
rsssongs=[]
count = 1
showname = "ANS"
stuff = []

for child in myroot.findall('channel/item'):
    stuff.append(child)
    stuff = stuff[::-1]
for child in stuff:
    title=child.find('title').text
    link=child.find('enclosure').attrib
    image=child.find('{http://www.itunes.com/dtds/podcast-1.0.dtd}image').attrib
    url=link['url']
    image_link=image['href']
    dicd={"name":title,"url":url,"image_link":image_link}
    rsssongs.append(dicd)
   
    count += 1

songs={"songs":rsssongs}

with open("songs.json", "w") as write_file:
    json.dump(songs, write_file)






