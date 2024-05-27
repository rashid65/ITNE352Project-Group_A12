import socket
import threading
import requests
import json
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="7558a150954e4dcaafa560b8d6f689c5")
def quitMe(Sock_a,ClientName):
    msg = Sock_a.recv(1024).decode('ascii')
    if msg == "Quit":
        return True
    return False

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

def Headline_country(countryNum):
    country = countryNum
    GETMsg = f'https://newsapi.org/v2/top-headlines?country={country}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

#Source functions
def NEWSources():
    GETMsg = f'https://newsapi.org/v2/sources?pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def SourceCategory(category):
    GETMsg = f'https://newsapi.org/v2/top-headlines/sources?category={category}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def SourceCountry(country):
    GETMsg = f'https://newsapi.org/v2/top-headlines/sources?country={country}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def Sourcelanguage(language):
    GETMsg = f'https://newsapi.org/v2/top-headlines/sources?language={language}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def ServeClient(Sock_a, SockName): # Thread 
    print("connected to ", SockName , "\n")
    try:
        ClientName = Sock_a.recv(1024).decode('ascii')
        print("the client name is ", ClientName)

        quitmenu1 = True
        finished = False
        while quitmenu1 and finished == False:
            MenuChoice = Sock_a.recv(1024).decode('ascii') #here it will receive either 1 for headlines or 2 for sources
            if MenuChoice == "Search Headlines":

                quitmenu2 = False
                while quitmenu2 == False:
                    HeadlineChoice = Sock_a.recv(1024).decode('ascii')
                
                    if HeadlineChoice == "Search by keywords":
                        ClientKeyword = Sock_a.recv(1024).decode('ascii')
                        Data = Headline_KeyWord(ClientKeyword)
                        fileName = f'A12_{ClientName}_SearchByKeyword.json'
                        print(f'clinet: {ClientName}, has requested Headline search by keyword ({ClientKeyword})')
                        savejson(fileName,Data)
                        Sock_a.sendall(fileName.encode('ascii'))
                        if quitMe(Sock_a,ClientName):
                            finished = True
                            break
                    
                    if HeadlineChoice == "Search by category":
                        ClientCat = Sock_a.recv(1024).decode('ascii')
                        Data = Headline_category(ClientCat)
                        fileName = f'A12_{ClientName}_SearchByCategory.json'
                        print(f'clinet: {ClientName}, has requested Headline search by category ({ClientCat})')
                        savejson(fileName,Data)
                        Sock_a.sendall(fileName.encode('ascii'))
                        if quitMe(Sock_a,ClientName):
                            finished = True
                            break

                    
                    if HeadlineChoice == "Search by country":
                        Clientcountry = Sock_a.recv(1024).decode('ascii')
                        Data = Headline_country(Clientcountry)
                        fileName = f'A12_{ClientName}_SearchByCountry.json'
                        print(f'clinet: {ClientName}, has requested Headline search by Ccuntry ({Clientcountry})')
                        savejson(fileName,Data)
                        Sock_a.sendall(fileName.encode('ascii'))
                        if quitMe(Sock_a,ClientName):
                            finished = True
                            break

                    if HeadlineChoice == "List all new headlines":
                        data = NEWHeadlines()
                        fileName = f'A12_{ClientName}_ListAllHeadlines.json'
                        print(f'clinet: {ClientName}, has requested list all Headlines')
                        savejson(fileName,data)
                        Sock_a.sendall(fileName.encode('ascii'))
                        if quitMe(Sock_a,ClientName):
                            finished = True
                            break

                    if HeadlineChoice == "Back to main menu":
                        break
        #---------------------------------------SOURCE---------------------------------------------------------------------------
            if MenuChoice == "List of Sources":
    
                quitmenu3 = False
                while quitmenu3 == False:
                    SourceChoice = Sock_a.recv(1024).decode('ascii')
                
                    if SourceChoice == "Search by category":
                        ClientCategory = Sock_a.recv(1024).decode('ascii')
                        data = SourceCategory(ClientCategory)
                        fileName = f'A12_{ClientName}_SorcesByCategory.json'
                        print(f'clinet: {ClientName}, has requested source search by category ({ClientCategory})')
                        savejson(fileName,data)
                        Sock_a.sendall(fileName.encode('ascii'))
                        if quitMe(Sock_a,ClientName):
                            finished = True
                            break

                    if SourceChoice == "Search by country":
                        clientCountry = Sock_a.recv(1024).decode('ascii')
                        data = SourceCountry(clientCountry)
                        fileName = f'A12_{ClientName}_SorcesByCountry.json'
                        print(f'clinet: {ClientName}, has requested source search by country ({Clientcountry})')
                        savejson(fileName,data)
                        Sock_a.sendall(fileName.encode('ascii'))
                        if quitMe(Sock_a,ClientName):
                            finished = True
                            break

                    if SourceChoice == "Search by language":
                        clientlanguage = Sock_a.recv(1024).decode('ascii')
                        data = Sourcelanguage(clientlanguage)
                        fileName = f'A12_{ClientName}_SorcesByLanguage.json'
                        print(f'clinet: {ClientName}, has requested source search by language ({clientlanguage})')
                        savejson(fileName,data)
                        Sock_a.sendall(fileName.encode('ascii'))
                        if quitMe(Sock_a,ClientName):
                            finished = True
                            break

                    if SourceChoice == "List all":
                        data = NEWSources()
                        fileName = f'A12_{ClientName}_ListAllsources.json'
                        print(f'clinet: {ClientName}, has requested list all sources')
                        savejson(fileName,data)
                        Sock_a.sendall(fileName.encode('ascii'))
                        if quitMe(Sock_a,ClientName):
                            finished = True
                            break

                    if SourceChoice == "Back to main menu":
                        break

            if MenuChoice == "Quit":
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