import socket
import threading
import requests
import json
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="7558a150954e4dcaafa560b8d6f689c5")

def NEWHeadlines():
    GETMsg = f'https://newsapi.org/v2/top-headlines?&apiKey={"7558a150954e4dcaafa560b8d6f689c5"}' #eddited
    response = requests.get(GETMsg)
    return response.json()

def NEWSources():
    GETMsg = f'https://newsapi.org/v2/sources?apiKey={"7558a150954e4dcaafa560b8d6f689c5"}'
    response = requests.get(GETMsg)
    return response.json()

def savejson(fileName, data):
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4)

def ServeClient(Sock_a, SockName): # Thread 
    print("connected to ", SockName , "\n")
    try:
        ClientName = Sock_a.recv(1024).decode('ascii')
        print("the client name is ", ClientName)
        Back = True
        while Back:
            Back = False
            MenuChoice = Sock_a.recv(1024).decode('ascii') #here it will receive either 1 for headlines or 2 for sources
            if MenuChoice == "1":
                HeadlineChoice = Sock_a.recv(1024).decode('ascii')
                if HeadlineChoice == "5":
                    Back = True
                    continue
                
                print(f"i got ur message {ClientName} ur headline choice number {HeadlineChoice}")
                #API code for headlines
                if HeadlineChoice == "5":
                    continue

            elif MenuChoice == "2":
                SoruceChoice = Sock_a.recv(1024).decode('ascii')
                print(f"i got ur message {ClientName} ur soruce choice number {SoruceChoice}")
                #API code for sources
                if SoruceChoice == "5":
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