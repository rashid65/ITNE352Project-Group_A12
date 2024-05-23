import socket
import threading
import requests
import json
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="7558a150954e4dcaafa560b8d6f689c5")

def NEWHeadlines(): #changed it to us??
    url = f'https://newsapi.org/v2/top-headlines?country=us&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(url)
    return response.json()

def NEWSources():
    GETMsg = f'https://newsapi.org/v2/sources?pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def savejson(fileName, data):
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4)

def Headline_KeyWord(Keyword): #tested worked fine
    GETMsg = f'https://newsapi.org/v2/top-headlines?q={Keyword}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def Headline_category(category): #tested worked fine
    GETMsg = f'https://newsapi.org/v2/top-headlines?category={category}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def WhichCateWasChosen(Num):
    Num = int(Num) - 1
    categoryList = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    return categoryList[Num]

def Headline_country(countryNum):
    countries = ["au","nz","ca","ae","sa","gb","us","eg","ma"]
    country = countries[int(countryNum)-1]
    GETMsg = f'https://newsapi.org/v2/top-headlines?country={country}&pageSize=15&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def ServeClient(Sock_a, SockName): # Thread 
    print("connected to ", SockName , "\n")
    try:
        ClientName = Sock_a.recv(1024).decode('ascii')
        print("the client name is ", ClientName)
        Noquit = True
        while Noquit:
            Back = True
            while Back:
                Back = False
                MenuChoice = Sock_a.recv(1024).decode('ascii') #here it will receive either 1 for headlines or 2 for sources
                if MenuChoice == "1":
                    HeadlineChoice = Sock_a.recv(1024).decode('ascii')

                    if HeadlineChoice == "1":
                        ClientKeyword = Sock_a.recv(1024).decode('ascii')
                        Data = Headline_KeyWord(ClientKeyword)
                        fileName = f'A12_{ClientName}_SearchByKeyword'
                        savejson(fileName,Data)
                    
                    if HeadlineChoice == "2":
                        ClientCatNum = Sock_a.recv(1024).decode('ascii')
                        ClientCat = WhichCateWasChosen(ClientCatNum)
                        Data = Headline_category(ClientCat)
                        fileName = f'A12_{ClientName}_SearchByCategory'
                        savejson(fileName,Data)
                    
                    if HeadlineChoice == "3":
                        Clientcountry = Sock_a.recv(1024).decode('ascii')
                        Data = Headline_country(Clientcountry)
                        fileName = f'A12_{ClientName}_SearchByCountry'
                        savejson(fileName,Data)

                    if HeadlineChoice == "4":
                        data = NEWHeadlines()
                        fileName = f'A12_{ClientName}_ListAllHeadlines'
                        savejson(fileName,data)

                    if HeadlineChoice == "5":
                        Back = True
                        continue
                    print(f"i got ur message {ClientName} ur headline choice number {HeadlineChoice}")
                #---------------------------------------SOURCE---------------------------------------------------------------------------
                elif MenuChoice == "2":
                    SoruceChoice = Sock_a.recv(1024).decode('ascii')
                    if SoruceChoice == "5":
                        Back = True
                        continue
                    #API code for sources

                    print(f"i got ur message {ClientName} ur soruce choice number {SoruceChoice}")
                elif MenuChoice == "3":
                    Noquit = False
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