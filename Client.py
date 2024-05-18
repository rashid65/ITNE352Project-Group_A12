import socket

def MainClient():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 49999))

        ClientName = input("what would you like to be your username? ")
        s.sendall(ClientName.encode('ascii'))
        
        
        data = s.recv(1024)
        print("Server said: ", data.decode('ascii'))
        
if __name__ == "__main__":
    MainClient()