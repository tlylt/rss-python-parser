import xml.etree.ElementTree as ET
import datetime
mytree = ET.parse('rss.xml')
myroot = mytree.getroot()
for x in myroot.findall('channel/item'):
    title=x.find('title').text
    link=x.find('link').text
    image=x.find('itunes:image').text
    print('Title:',title,'\n','Audio link:',link,'\n','Image link:',image)    



    