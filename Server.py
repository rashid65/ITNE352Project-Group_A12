import socket
import threading
import requests
import json
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="7558a150954e4dcaafa560b8d6f689c5")

#Headlines functions
def NEWHeadlines():
    url = f'https://newsapi.org/v2/top-headlines?country=us&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(url)
    return response.json()

def savejson(fileName, data):
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4)

def Headline_KeyWord(Keyword):
    GETMsg = f'https://newsapi.org/v2/top-headlines?q={Keyword}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def Headline_category(category):
    GETMsg = f'https://newsapi.org/v2/top-headlines?category={category}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def WhichCateWasChosen(Num):
    Num = int(Num) - 1
    categoryList = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    return categoryList[Num]

def Headline_country(countryNum):
    countrylist = ["au","nz","ca","ae","sa","gb","us","eg","ma"]
    country = countrylist[int(countryNum)-1]
    GETMsg = f'https://newsapi.org/v2/top-headlines?country={country}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

#Source functions
def NEWSources():
    GETMsg = f'https://newsapi.org/v2/sources?pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def SourceCategory(categoryNum):
    categorylist = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    category = categorylist[int(categoryNum)-1]
    GETMsg = f'https://newsapi.org/v2/top-headlines/sources?category={category}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def SourceCountry(countryNum):
    countryList = ["au","NZ","ca","ae","sa","gb","us","eg","ma"]
    country = countryList[int(countryNum)-1]
    GETMsg = f'https://newsapi.org/v2/top-headlines/sources?country={country}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def Sourcelanguage(languageNum):
    languagelist = ["ar","en"]
    language = languagelist[int(languageNum)-1]
    GETMsg = f'https://newsapi.org/v2/top-headlines/sources?language={language}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def ServeClient(Sock_a, SockName): # Thread 
    print("connected to ", SockName , "\n")
    try:
        ClientName = Sock_a.recv(1024).decode('ascii')
        print("the client name is ", ClientName)

        quitmenu1 = True
        while quitmenu1:
            MenuChoice = Sock_a.recv(1024).decode('ascii') #here it will receive either 1 for headlines or 2 for sources
            if MenuChoice == "Search Headlines":
                print("im in hedaings")
                quitmenu2 = False
                while quitmenu2 == False:
                    HeadlineChoice = Sock_a.recv(1024).decode('ascii')
                
                    if HeadlineChoice == "1":
                        ClientKeyword = Sock_a.recv(1024).decode('ascii')
                        Data = Headline_KeyWord(ClientKeyword)
                        fileName = f'A12_{ClientName}_SearchByKeyword.json'
                        savejson(fileName,Data)
                    
                    elif HeadlineChoice == "2":
                        ClientCatNum = Sock_a.recv(1024).decode('ascii')
                        ClientCat = WhichCateWasChosen(ClientCatNum)
                        Data = Headline_category(ClientCat)
                        fileName = f'A12_{ClientName}_SearchByCategory.json'
                        savejson(fileName,Data)
                    
                    elif HeadlineChoice == "3":
                        Clientcountry = Sock_a.recv(1024).decode('ascii')
                        Data = Headline_country(Clientcountry)
                        fileName = f'A12_{ClientName}_SearchByCountry.json'
                        savejson(fileName,Data)

                    elif HeadlineChoice == "4":
                        data = NEWHeadlines()
                        fileName = f'A12_{ClientName}_ListAllHeadlines.json'
                        savejson(fileName,data)

                    elif HeadlineChoice == "5":
                        break
                    print(f"i got ur message {ClientName} ur headline choice number {HeadlineChoice}")
        #---------------------------------------SOURCE---------------------------------------------------------------------------
            elif MenuChoice == "List of Soarces":
                print("im in Sources")
                quitmenu3 = False
                while quitmenu3 == False:
                    SourceChoice = Sock_a.recv(1024).decode('ascii')
                
                    if SourceChoice == "1":
                        ClientCategory = Sock_a.recv(1024).decode('ascii')
                        data = SourceCategory(ClientCategory)
                        fileName = f'A12_{ClientName}_SorcesByCategory.json'
                        savejson(fileName,data)
                    elif SourceChoice == "2":
                        clientCountry = Sock_a.recv(1024).decode('ascii')
                        data = SourceCountry(clientCountry)
                        fileName = f'A12_{ClientName}_SorcesByCountry.json'
                        savejson(fileName,data)
                    elif SourceChoice == "3":
                        clientlanguage = Sock_a.recv(1024).decode('ascii')
                        data = SourceCountry(clientlanguage)
                        fileName = f'A12_{ClientName}_SorcesByLanguage.json'
                        savejson(fileName,data)
                    elif SourceChoice == "4":
                        data = NEWSources()
                        fileName = f'A12_{ClientName}_ListAllsources.json'
                        savejson(fileName,data)
                    elif SourceChoice == "5":
                        break
                    #API code for sources

                    print(f"i got ur message {ClientName} ur soruce choice number {SourceChoice}")
            elif MenuChoice == "3":
                quitmenu1 = False
                continue

    finally:
        Sock_a.close()
        print("Connection closed with", ClientName)

def MainServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 49999))
        s.listen()
        print("The server has been started...")
        
        while True:
            Sock_a, SockName = s.accept()
            client_thread = threading.Thread(target=ServeClient, args=(Sock_a, SockName))
            client_thread.start()


if __name__ == "__main__":
    MainServer()