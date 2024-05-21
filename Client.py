import socket

def MainClient():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs:
        cs.connect(("127.0.0.1", 49999))

        ClientName = input("what would you like to be your username? ") # Sends client name
        cs.sendall(ClientName.encode('ascii'))

        quit = False
        while quit == False:
            print("\n    ~~~Menu~~~")
            print("1- Search Headlines")
            print("2- List of Soarces")
            print("3- Quit")

            choice = input("\nChoose an option:\n")

            if int(choice) < 1 or int(choice) > 3:
                print("Please choose a valid number")
            else:
                    cs.sendall(choice.encode('ascii'))

            if choice == "1":

                goback = False
                while goback == False:
                    print("\n~~~Search Headlines Menu~~~")
                    print("1- Search by keywords")
                    print("2- Search by category")
                    print("3- Search by country")
                    print("4- List all new headlines")
                    print("5- Back to main menu")

                    choiceA = input("\nChoose an option:\n")
                    
                    if int(choiceA) < 1 or int(choiceA) > 5:
                        print("\nPlease choose a valid number")
                    else:
                        cs.sendall(choiceA.encode('ascii'))

                    if choiceA == "5":
                        goback = True

            elif choice == "2":

                goback = False
                while goback == False:
                    print("\n~~~List of Sources Menu~~~")
                    print("1- Search by category")
                    print("2- Search by country")
                    print("3- Search by language")
                    print("4- List all")
                    print("5- Back to main menu")

                    choiceB = input("\nChoose an option:\n")

                    if int(choiceB) < 1 or int(choiceB) > 5:
                        print("\nPlease choose a valid number")
                    else:
                        cs.sendall(choiceB.encode('ascii'))
                    if choiceB == "5":
                        goback = True

            elif choice == "3":

                quit = True
                cs.close()
                break
 
      
if __name__ == "__main__":
    MainClient()