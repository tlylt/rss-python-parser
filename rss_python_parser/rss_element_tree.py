import requests
import xml.etree.ElementTree as ET
mytree = ET.parse('rss.xml')
myroot = mytree.getroot()
count = 1
showname = "ANS"
stuff = []
for child in myroot.findall('channel/item'):
    stuff.append(child)
stuff = stuff[::-1]
for child in stuff:
    epno = str(count)
    item = (child.attrib)
    title=child.find('title').text
    link=child.find('link').text
    epno = epno.zfill(3)
    for image in myroot.findall('channel/item/{http://www.itunes.com/dtds/podcast-1.0.dtd}image'):
        stuff.append(image)
    stuff = stuff[::-1]
    for image in stuff:
        epno = str(count)
        item = (image.attrib)
        epno = epno.zfill(3)
        name = f"{showname}-{epno}"
    print(name)
    print(title)
    print(link)
    print(image.attrib)
    count += 1


    