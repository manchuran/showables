import requests
from bs4 import BeautifulSoup


#Required functions

def getLinks(bsObj):
    links = []
    _time_frs = []
    for item in bsObj.find_all('table')[1].find_all('a'):
        links+=[(str(item).replace('<b>','').replace('</b>','').replace('</a>','').replace('<a href="','').replace(';','').split('">'))]
    for item in str(bsObj.find_all('table')[1]).split('<br/>')[:-1]:
        _time_frs+=[item.rsplit('at')[-1].replace('<b>','').replace('</b>','').strip()]   
    return [link + [_time_fr] for link,_time_fr in zip(links,_time_frs)]    
    
def getbsObj(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = response.content
    bsObj = BeautifulSoup(html)
    return bsObj
    
def getSection(bsObj):
    return bsObj.find_all('body')[0].find_all(attrs={"class": "bold"})[0].find_all('a')[2].contents[0]

def getUser(bsObj):
    return bsObj.find_all('table')[1].find_all(attrs={"class": "user"})[0].contents[0]

def getTime(bsObj):
    return [str(i).replace('<b>','').replace('</b>','') for i in bsObj.find_all('table')[1].find_all(attrs={"class": "s"})[0].find_all('b')]
    
    
#Scraper

#Import required libraries
import time
import csv
url_string = "https://www.nairaland.com/news"
f = open('nl.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(f)

#Specify number of pages to scrape in range function
for i in range(2):    
    try:
        #Assess Link    
        start_time = time.time()
        print(f"Downloading page {i}....", end='')
        div = getLinks(getbsObj(url_string + "/" + str(i)))
        end_time = time.time()
        print(f"time taken: {end_time-start_time}")

        print(f"Writing to file....",end='\n')
        
        #Add more details from each link to list
        final_links=[]
        for i, link in enumerate(div):
            bsObj = getbsObj(link[0])
            section = getSection(bsObj)
            user = getUser(bsObj)
            _time = getTime(bsObj)
            link += [section] + [user] + [_time]
            final_links += link
            print(f"Appending link {i}.....", end='\r')         
        
        #Write into csv file
        for row in div:
            csv_writer.writerow(row)
 
        #Sleeping 20 seconds. Consider sleeping for more time to conserve resources
        print(f"\nDone. Sleeping 20 secs...")
        time.sleep(20)
        
        div=[]
    except:
        continue
        
f.close()  