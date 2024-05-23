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

         #===============================================Headline============================================================

            if choice == "1":

                goback = False
                while goback == False:
                    goback = False
                    print("\n~~~Search Headlines Menu~~~")
                    print("1- Search by keywords")
                    print("2- Search by category")
                    print("3- Search by country")
                    print("4- List all new headlines")
                    print("5- Back to main menu")

                    choice_Headline = input("\nChoose an option:\n")
                    
                    if int(choice_Headline) < 1 or int(choice_Headline) > 5:
                        print("\nPlease choose a valid number")
                        continue
                    else:
                        cs.sendall(choice_Headline.encode('ascii'))

                    
                    
                    if choice_Headline == "1":                                                     # Keyword option (Headlines)
                        choice_Headline_Keyword = input("Enter the Keyword you want to search for: ")
                        cs.sendall(choice_Headline_Keyword.encode('ascii'))
                    elif choice_Headline == "2":                                                   # Categories option (Headlines)

                        print("====== availble Categories ======")
                        print("1- Business")
                        print("2- Entertainment")
                        print("3- General")
                        print("4- Health")
                        print("5- Science")
                        print("6- Sports")
                        print("7- Technology")

                        choice_Headline_Catagory = input("\nChoose a Catagory:\n")

                        if int(choice_Headline_Catagory) < 1 or int(choice_Headline_Catagory) > 7:
                            print("Please choose a valid number")
                        else:
                            cs.sendall(choice_Headline_Catagory.encode('ascii'))

                    elif choice_Headline == "3":                                                   # country option (Headlines)

                        print("====== availble Countries ======")
                        print("1- Australia (au)")
                        print("2- New Zealand (NZ)")
                        print("3- Canada (ca)")
                        print("4- United Arab Emirates (ae)")
                        print("5- Saudi Arabia (sa)")
                        print("6- United Kingdom (gb)")
                        print("7- United States of America (us)")
                        print("8- Egypt (eg)")
                        print("9- Morocco (ma)")

                        choice_Headline_Country = input("\nChoose a Country:\n")

                        if int(choice_Headline_Country) < 1 or int(choice_Headline_Country) > 9:
                            print("Please choose a valid number")
                        else:
                            cs.sendall(choice_Headline_Country.encode('ascii'))

                    
                    elif choice_Headline == "4":                                                   # top Headlines option
                        print("requesting top headlines from the server...")
                        # do smth here send to server ?
                    elif choice_Headline == "5":
                            goback = True
            #=====================================********SOURCE*********============================================================
            elif choice == "2":

                goback2 = False
                while goback2 == False:
                    print("\n~~~List of Sources Menu~~~")
                    print("1- Search by category")
                    print("2- Search by country")
                    print("3- Search by language")
                    print("4- List all")
                    print("5- Back to main menu")

                    choice_Source = input("\nChoose an option:\n")

                    if int(choice_Source) < 1 or int(choice_Source) > 5:
                        print("\nPlease choose a valid number")
                    else:
                        cs.sendall(choice_Source.encode('ascii'))
                        
                    if choice_Source == "1":                                                                         # Categories option (Source)
                        print("====== availble Categories ======")
                        print("1- Business")
                        print("2- Entertainment")
                        print("3- General")
                        print("4- Health")
                        print("5- Science")
                        print("6- Sports")
                        print("7- Technology")

                        choice_Source_Catagory = input("\nChoose a Catagory:\n")

                        if int(choice_Source_Catagory) < 1 or int(choice_Source_Catagory) > 7:
                            print("Please choose a valid number")
                        else:
                            cs.sendall(choice_Source_Catagory.encode('ascii'))
                    
                    elif choice_Source == "2":                                                                       # country option (Source)
                        print("====== availble Countries ======")
                        print("1- Australia (au)")
                        print("2- New Zealand (NZ)")
                        print("3- Canada (ca)")
                        print("4- United Arab Emirates (ae)")
                        print("5- Saudi Arabia (sa)")
                        print("6- United Kingdom (gb)")
                        print("7- United States of America (us)")
                        print("8- Egypt (eg)")
                        print("9- Morocco (ma)")
                        choice_Source_Country = input("\nChoose a Country:\n")
                        if int(choice_Source_Country) < 1 or int(choice_Source_Country) > 9:
                            print("Please choose a valid number")
                        else:
                            cs.sendall(choice_Source_Country.encode('ascii'))

                    elif choice_Source == "3":                                                                        #Language option (Source)
                        print("Available Languages")
                        print("1- Arabic (ar)")
                        print("2- English (en)")
                        choice_Source_Language = input("\nChoose a Language:\n")
                        if int(choice_Source_Language) < 1 or int(choice_Source_Language) > 2:
                            print("please chose a valid number")
                        else:
                            cs.sendall(choice_Source_Language.encode('ascii'))
                    
                    elif choice_Source == "4":
                        print("smth")
                        #do smth here

                    elif choice_Source == "5":
                            goback2 = True

            elif choice == "3":
                quit = True
                cs.sendall(choice.encode('ascii'))
                cs.close()
                break
 
      
if __name__ == "__main__":
    MainClient()