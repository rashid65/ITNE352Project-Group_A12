import socket

def MainClient():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs:
        cs.connect(("127.0.0.1", 49999))

        ClientName = input("what would you like to be your username? ") # Sends client name
        cs.sendall(ClientName.encode('ascii'))

        quit = False
        while quit == False:
            print("\n~~~Menu~~~")
            print("1- Search Headlines")
            print("2- List of Soarces")
            print("3- Quit")

            choice = input("\nChoose an option:\n")

            if choice < "1" or choice > "3":
                print("Please choose a valid number")
            
            if choice == "1":

                print("\n~~~Search Headlines Menu~~~\n")
                print("1- Search by keywords")
                print("2- Search by category")
                print("3- Search by country")
                print("4- List all new headlines")
                print("5- Back to main menu")

                choiceA = input("\nChoose an option:\n")
                if choiceA < "1" or choiceA > "3":
                    print("Please choose a valid number")
                if choiceA == "5":
                    continue

            elif choice == "2":

                print("\n~~~List of Sources Menu~~~\n")
                print("1- Search by category")
                print("2- Search by country")
                print("3- Search by language")
                print("4- List all")
                print("5- Back to main menu")

                choiceB = input("\nChoose an option:\n")

                if choiceB < "1" or choiceB > "3":
                    print("Please choose a valid number")
                if choiceB == "5":
                    continue

            elif choice == "3":

                quit = True
                cs.close()
                break
 
      
if __name__ == "__main__":
    MainClient()