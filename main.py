from book import show_book, save_book, load_book
import os
from dotenv  import load_dotenv

load_dotenv()
name = input("🌺 whats your name : ")
print("🌺 nice to meat you 🌺")

admin_mode = input("🌺 do you want admin mode yes/no : ")


if admin_mode == "yes":

        admin_password = input("🌺 pleas enter admin password : ")
        
        if admin_password == os.getenv("ADMIN_PASSWORD"):
                print("🌺 admin mode 🌺")
        else : 
                 print("🌺 worng 🌺")

else:
        print("🌺 you may countinue 🌺")
        
        
how_many_book = int(input("🌺 how many book do you want : "))

books = load_book()

for i in range(how_many_book):
    book_name = input("🌺 enter a task: ")
    priority = input("🌺 enter a priority (low , medium , high) : ").lower()
    book = {
        "book_name": book_name,
        "priority": priority
    }
books.append(book)
        
show_book(books)
save_book(books)
