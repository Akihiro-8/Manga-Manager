from manga import MangaManager #import mangaManager from manga.py file

# logo for the project
logo = '''
'||    ||'                                                  
 |||  |||   ....   .. ...     ... .  ....                   
 |'|..'||  '' .||   ||  ||   || ||  '' .||                  
 | '|' ||  .|' ||   ||  ||    |''   .|' ||                  
.|. | .||. '|..'|' .||. ||.  '||||. '|..'|'                 
                            .|....'                         
                                                            
'||    ||'                                                  
 |||  |||   ....   .. ...    ....     ... .   ....  ... ..  
 |'|..'||  '' .||   ||  ||  '' .||   || ||  .|...||  ||' '' 
 | '|' ||  .|' ||   ||  ||  .|' ||    |''   ||       ||     
.|. | .||. '|..'|' .||. ||. '|..'|'  '||||.  '|...' .||.    
                                    .|....'                 
                                                            '''

# show the options for user to choice
def print_options():
    print("1. Display all mangas")
    print("2. Total number of mangas")
    print("3. Add new manga")
    print("4. Search manga by Title or Author or Rating")
    print("5. Delete manga")
    print("6. Edit existing manga information.")
    print("7. Exit from manga manager\n")

def main():
    manga_manager = MangaManager() #make object of MangaManager class
    while True:
        print(logo) #print the logo
        print_options()
        choice = input("Choose an option: ") #ask user to choose an option
        print("-------------------\n")

        # if user choose to display all mangas
        if choice == '1': 
            mangas = manga_manager.display_all_manga()
            # check if there's any manga in file
            if len(mangas) == 0: # if no
                print("There's no manga available now!!!\n")  
            else:
                # if exists, print all mangas 
                for manga in mangas:
                    print(manga)
            print("\n*************************************************")         

        # if user choose to display total count of manga
        elif choice == '2':
            mangas = manga_manager.display_all_manga()
            print(f"Total number of things {len(mangas)}\n")
            print("\n*************************************************")   

        # if user choose to add new manga
        elif choice == "3":
            # ask required info from the user and use strip to remove extra mistake space
            title = input("Enter manga title: ").strip()
            author = input("Enter manga author: ").strip()
            genre = input("Enter manga genre: ").strip()
            volume = input("Enter manga volume: ").strip()
            # Get valid released year (int)
            while True:
                released_year = input("Enter released year: ").strip()
                if released_year.isdigit():
                    released_year = int(released_year)
                    break
                else:
                    print("Please enter a valid year (number only).")
            publisher = input("Enter manga publisher: ").strip()
            status = input("Enter manga status: ").strip()
            price = input("Enter manga price: ").strip()
            # Get valid rating (float)
            while True:
                rating = input("Enter rating(Between 1 to 10): ").strip()
                try:
                    rating = float(rating)
                    break
                except ValueError:
                    print("Please enter a valid rating (e.g. 3, 8, 8.5)")
            language = input("Enter manga language: ").strip()
            book_format = input("Enter manga format: ").strip()
            serialization = input("First publish in: ").strip()
            # call add_manga function using mang_manager obj to add data
            manga_manager.add_manga(title, author, genre, volume, released_year, publisher, status, price, rating, language, book_format, serialization)
            print("\n*************************************************")   

        # if user choose to search info from the manga list
        elif choice == "4":
            manga_manager.search_prompt()
            print("\n*************************************************")   

        # if user choose to delete a manga
        elif choice == "5":
            # ask for id number to delete
            id = input("Enter the ID of the manga you want to delete: ")
            # check does the manga with that Id exit or not
            manga = manga_manager.get_manga_by_id(id)
            if manga:
                print(manga)
                # if exit, double confirm it to be sure
                check = input("Do you want to delete this manga? y or n: ").strip().lower()
                if check == "y":
                    # call delete function to delete that specific manga
                    manga_manager.delete_manga(id)
            else: # if not found
                print("Manga with that ID not found!")
            print("\n*************************************************") 

        # if user choose to edit info of manga
        elif choice == "6":
            id = input("Enter the ID of the manga you want to update\n")
            # check does the manga with that Id exit or not
            manga = manga_manager.get_manga_by_id(id)
            if manga:
                print(manga)
                # if exit, double confirm it to be sure
                check = input("Do you want to update this manga? y or n: ").strip().lower()
                if check == 'y':
                    new_title = input("Enter new title: ").strip()
                    new_author = input("Enter new author: ").strip()
                    new_genre = input("Enter new genre: ").strip()
                    new_volume = input("Enter new volume: ").strip()
                    while True:
                        new_released_year = input("Enter new released year: ").strip()
                        if new_released_year.isdigit():
                            new_released_year = int(new_released_year)
                            break
                        else:
                            print("Please enter a valid year (number only).")                    
                    new_publisher = input("Enter new publisher: ").strip()
                    new_status = input("Enter new status: ").strip()
                    new_price = input("Enter new price: ").strip()
                    # Get valid rating (float)
                    while True:
                        new_rating = input("Enter new rating(Between 1 to 10): ").strip()
                        try:
                            new_rating = float(new_rating)
                            break
                        except ValueError:
                            print("Please enter a valid rating (e.g. 3, 8, 8.5)")
                    new_language = input("Enter new language: ").strip()
                    new_book_format = input("Enter new format: ").strip()
                    new_serialization = input("Enter new serialization: ").strip()
                    # call update function to update the latest info
                    manga_manager.update(id, new_title, new_author, new_genre, new_volume, new_released_year, new_publisher, new_status, new_price, new_rating, new_language, new_book_format, new_serialization)
            else:
                print("Manga with that ID not found!")
            print("\n*************************************************")   
        elif choice == "7":
            print("Finished")
            print("\n*************************************************")   
            break

        else:
            # giude the user to type only between 1 to 7
            print("Invalid choice!!!\nPlease type only between 1 to 7.\n")
            print("\n*************************************************")  
        still_using = input("Do you wanna continue using? Press y to continue.\n").strip().lower()

        # if you want to exit right after the activity
        if still_using == "y":
            pass
        else:
            print("Finished")
            print("\n*************************************************")  
            break

# call main function
if __name__ == "__main__":
    main()