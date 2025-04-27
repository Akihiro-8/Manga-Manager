# manga info class
class Manga:
    def __init__(self, id, title, author, genre, volume, released_year, publisher, status, price, rating, language, book_format, serialization):
        self.id = id 
        self.title = title
        self.author = author
        self.genre = genre
        self.volume = volume
        self.released_year = released_year
        self.publisher = publisher
        self.status = status
        self.price = price
        self.rating = rating
        self.language = language
        self.book_format = book_format
        self.serialization = serialization

    # to get string representation instead of object
    def __str__(self):
        return f'ID: {self.id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Volume: {self.volume}, Released Year: {self.released_year}, Publisher: {self.publisher}, Status: {self.status}, Price: {self.price}, Rating: {self.rating}, Language: {self.language}, Format: {self.book_format}, First printed in: {self.serialization}'

# manga handler class
class MangaManager:
    def __init__(self, filename='mangas.txt'):
        self.filename = filename
        self.mangas = self.show_manga()

    # to get current available manga list
    def show_manga(self):
        mangas = []
        try:
            # to read the file
            with open(self.filename, 'r') as file:
                for line in file:
                    # put data in each variable by spliting the data with '/'
                    id, title, author, genre, volume, released_year, publisher, status, price, rating, language, book_format, serialization = line.strip().split('/')
                    mangas.append(Manga(id, title, author, genre, volume, released_year, publisher, status, price, rating, language, book_format, serialization))
        except FileNotFoundError:
            print("Mangas file didn't exit!")
            pass
        return mangas
    
    # to get specific manga by id
    def get_manga_by_id(self, id):
        for manga in self.mangas:
            if manga.id == id:
                return manga
        return None

    # to save the manga info
    def save_manga_info(self):
        # to write in the file
        with open(self.filename, 'w') as file:
            # save the data using '/' as separator
            for manga in self.mangas:
                file.write(f"{manga.id}/{manga.title}/{manga.author}/{manga.genre}/{manga.volume}/{manga.released_year}/{manga.publisher}/{manga.status}/{manga.price}/{manga.rating}/{manga.language}/{manga.book_format}/{manga.serialization}\n")

    # to auto increase id
    def get_next_id(self):
        if not self.mangas:
            return 1
        return max(int(manga.id) for manga in self.mangas) + 1

    # to add the manga info by making a manga object
    def add_manga(self, title, author, genre, volume, released_year, publisher, status, price, rating, language, book_format, serialization):
        new_id = self.get_next_id()
        # create the manga object
        manga = Manga(str(new_id),title, author, genre, volume, released_year, publisher, status, price, rating, language, book_format, serialization)
        # add to the orginal manga list to get up to date data
        self.mangas.append(manga)
        # save the added manga
        self.save_manga_info()
        print("Sucessfully added.")
        

    # to display all mangas info
    def display_all_manga(self):
        return [manga for manga in self.mangas]
    
    # to search the mangas
    def search_manga(self, type, info):
        manga_list = []
        # if user want to search using manga title
        if type == '1':
            for manga in self.mangas:
                if manga.title.lower() == info.lower():
                    manga_list.append(manga)
        # if user want to search using manga author
        elif type == '2':
            for manga in self.mangas:
                if manga.author.lower() == info.lower():
                    manga_list.append(manga)
        # if user want to search by minimum rating
        elif type == '3':
            for manga in self.mangas:
                if float(manga.rating) >= float(info):
                    manga_list.append(manga)
        # return result list if the conditions are met
        return [manga for manga in manga_list]
        
    # to specify which one does user want to use for searching
    def search_prompt(self):
        print("Search Manga By:")
        print("1. Title")
        print("2. Author")
        print("3. Minimum Rating")
        choice = input("Enter option (1 or 2 or 3): ").strip()
        # 
        if choice in ['1', '2']:
            name = input("Enter name: ").strip()
            # call search function to search
            manga_list = self.search_manga(choice, name)
        elif choice == '3':
            while True:
                min_rating = input("Enter minimum rating: ")
                try:
                    min_rating = float(min_rating)
                    break
                except ValueError:
                    print("Please enter a valid rating (e.g. 3, 8, 8.5)")
            # call search function to search
            manga_list = self.search_manga(choice, str(min_rating))
        else:
            print("Invalid choice. Enter 1 or 2 or 3")
            return
        if manga_list:
            # if the manga list is not empty print results
            print("Result list of mangas")
            for manga in manga_list:
                print(manga)
        else:
            # if the given data is not matched
            print("No matching manga found!")
    
    # to update the existing data
    # new data are set as none by default
    def update(self, id, new_title=None, new_author=None, new_genre=None, new_volume=None, new_released_year=None, new_publisher=None, new_status=None, new_price=None, new_rating=None, new_language=None, new_book_format=None, new_serialization=None):
        for manga in self.mangas:
            # look for the matching one with the id
            if manga.id == id:
                # set new value to their respective one if the new value is not none
                if new_title:
                    manga.title = new_title
                if new_author:
                    manga.author = new_author
                if new_genre:
                    manga.genre = new_genre
                if new_volume:
                    manga.volume = new_volume
                if new_released_year:
                    manga.released_year = new_released_year
                if new_publisher:
                    manga.publisher = new_publisher
                if new_status:
                    manga.status = new_status
                if new_price:
                    manga.price = new_price
                if new_rating:
                    manga.rating = new_rating
                if new_language:
                    manga.language = new_language
                if new_book_format:
                    manga.book_format = new_book_format
                if new_serialization:
                    manga.serialization = new_serialization
                # update the file back
                self.save_manga_info()
                print("Successfully updated.")
                print(manga)
                break

    # to delete the manga of the given id
    def delete_manga(self, id):
        # updating the manga list to delete the matching one with the given id
        self.mangas = [manga for manga in self.mangas if manga.id != id]
        # resave the file
        self.save_manga_info()
        print("Successfully deleted.")