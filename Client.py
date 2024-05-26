import socket
import json
import datetime

# Detail function
def showHeadlinesDetails(fileName):                                                                         # Convers json format data into a python list & dysplays the news
    with open(fileName, 'r') as f:                                                                          # Shows details about the news, and (if chosen) shows further details about a specific result
        results = json.load(f)
        articles = results["articles"]

        result_list = []

        for item in articles[:15]:
            result_list.append(item['source']['name'])
            result_list.append(item['author'])
            result_list.append(item['title'])

        num = 1
        for i in range(0, len(result_list), 3):
            print(num,".")
            print(f"   Source: {result_list[i]}")
            print(f"   Title: {result_list[i+2]}")
            print(f"   Author: {result_list[i+1]}")
            num += 1

    quitloop = False
    while quitloop == False:

        details_choice = input("choose a result to be displayed: \n")

        further_details = []
        result = articles[int(details_choice)-1]

        try:
            published_datetime = datetime.datetime.strptime(result['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            published_datetime = datetime.datetime.fromisoformat(result['publishedAt'])        
            
        publishing_date = published_datetime.date()
        publishing_time = published_datetime.time()

        print(f"\nSource Name: {result['source']['name']}")
        print(f"author : {result['author']}")
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Description: {result['description']}")
        print(f"Publishing Date: {publishing_date}")
        print(f"Publishing Time: {publishing_time}\n")
        quitloop = True

def showSourcesDetails(fileName):
    with open(fileName, 'r') as f:
        results = json.load(f)
        sources = results["sources"]

        source_list = []

        for item in sources[:5]:
            source_list.append(item['name'])

        num = 1
        for i in range(0, len(source_list)):
            print(num,". " + source_list[i])
            num += 1

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
                    print("\n~~~Search Headlines Menu~~~")
                    print("1- Search by keywords")
                    print("2- Search by category")
                    print("3- Search by country")
                    print("4- List all new headlines")
                    print("5- Back to main menu")

                    choice_Headline = input("\nChoose an option:\n")
                    
                    if choice_Headline < "1" or choice_Headline > "5": #checking if it was a charcter
                        print("Please choose a valid number")
                    elif int(choice_Headline) < 1 or int(choice_Headline) > 5: #checking the number range
                        print("Please choose a valid number")
                    else:
                        cs.sendall(choice_Headline.encode('ascii'))

                    if choice_Headline == "1":                                                     # Keyword option (Headlines)
                        choice_Headline_Keyword = input("Enter the Keyword you want to search for: ")
                        cs.sendall(choice_Headline.encode('ascii'))

                        json_file = cs.recv(1024).decode('ascii')
                        showHeadlinesDetails(json_file)
                    
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

                        if choice_Headline_Catagory < "1" or choice_Headline_Catagory > "7": #checking if it was a charcter
                            print("Please choose a valid number")
                        elif int(choice_Headline_Catagory) < 1 or int(choice_Headline_Catagory) > 7: #checking the number range
                            print("Please choose a valid number")
                        else:
                            cs.sendall(choice_Headline_Catagory.encode('ascii'))

                            json_file = cs.recv(1024).decode('ascii')
                            showHeadlinesDetails(json_file)

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

                        if choice_Headline_Country < "1" or choice_Headline_Country > "9": #checking if it was a charcter
                            print("Please choose a valid number")
                        elif int(choice_Headline_Country) < 1 or int(choice_Headline_Country) > 9: #checking the number range
                            print("Please choose a valid number")
                        else:
                            cs.sendall(choice_Headline_Country.encode('ascii'))
                            json_file = cs.recv(1024).decode('ascii')
                            showHeadlinesDetails(json_file)

                    elif choice_Headline == "4":                                                   # top Headlines option

                        json_file = cs.recv(1024).decode('ascii')
                        showHeadlinesDetails(json_file)
                        
                    elif choice_Headline == "5":                                                   # Quit option
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
                    
                    if choice_Source < "1" or choice_Source > "5":
                        print("\nPlease choose a valid number")
                    elif int(choice_Source) < 1 or int(choice_Source) > 5:
                        print("\nPlease choose a valid number")
                    else:
                        cs.sendall(choice_Source.encode('ascii'))
                        
                    if choice_Source == "1":                                                       # Categories option (Source)
                        print("====== availble Categories ======")
                        print("1- Business")
                        print("2- Entertainment")
                        print("3- General")
                        print("4- Health")
                        print("5- Science")
                        print("6- Sports")
                        print("7- Technology")

                        choice_Source_Catagory = input("\nChoose a Catagory:\n")

                        if choice_Source_Catagory < "1" or choice_Source_Catagory > "7": #checking if it was a charcter
                            print("Please choose a valid number")
                        elif int(choice_Source_Catagory) < 1 or int(choice_Source_Catagory) > 7: #checking the number range
                            print("Please choose a valid number")
                        else:
                            cs.sendall(choice_Source_Catagory.encode('ascii'))
                            json_file = cs.recv(1024).decode('ascii')
                            showSourcesDetails(json_file)

                    
                    elif choice_Source == "2":                                                     # country option (Source)
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

                        if choice_Source_Country < "1" or choice_Source_Country > "9": #checking if it was a charcter
                            print("Please choose a valid number")
                        elif int(choice_Source_Country) < 1 or int(choice_Source_Country) > 9: #checking the number range
                            print("Please choose a valid number")
                        else:
                            cs.sendall(choice_Source_Country.encode('ascii'))
                            json_file = cs.recv(1024).decode('ascii')
                            showSourcesDetails(json_file)
                        
                    elif choice_Source == "3":                                                     #Language option (Source)
                        print("Available Languages")
                        print("1- Arabic (ar)")
                        print("2- English (en)")
                        choice_Source_Language = input("\nChoose a Language:\n")

                        if choice_Source_Language < "1" or choice_Source_Language > "3": #checking if it was a charcter
                            print("Please choose a valid number")
                        elif int(choice_Source_Language) < 1 or int(choice_Source_Language) > 3: #checking the number range
                            print("Please choose a valid number")
                        else:
                            cs.sendall(choice_Source_Language.encode('ascii'))
                            json_file = cs.recv(1024).decode('ascii')
                            showSourcesDetails(json_file)

                    elif choice_Source == "4":
                        json_file = cs.recv(1024).decode('ascii')
                        showSourcesDetails(json_file)

                    elif choice_Source == "5":
                            goback2 = True

            elif choice == "3":

                quit = True
                cs.close()
                break
 
      
if __name__ == "__main__":
    MainClient()