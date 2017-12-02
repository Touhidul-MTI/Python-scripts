import requests
from bs4 import BeautifulSoup


page=1
counter=0
limit=True
while(limit):
    url="https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=San+Francisco%2C+CA&page="+str(page)
    
    req = requests.get(url)           
    soup = BeautifulSoup(req.content, "lxml")
    #soup = BeautifulSoup(req.content, "html.parser")
    '''
    if "html.parser" way doesn't work, then use "lxml" way.
    install lxml #pip install lxml
    '''

    if soup is None:
        limit = False
    else:
        links = soup.find_all("div",{"class":"info"})
        print("-------------------------------------",page)
        
        for link in links:
            print (counter,link.contents[0].find_all("a",{"class":"business-name"})[0].text)
            print (link.contents[1].find_all("p",{"class":"adr"})[0].text)

            try:
                print (link.contents[1].find_all("div",{"itemprop":"telephone"})[0].text)
            except:
                pass

            counter=counter+1

        page+=1
    print("-------------------------------------")


