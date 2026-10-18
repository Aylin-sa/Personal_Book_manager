name = input("whats your name : ")
print("nice to meat you")

how_many_book = int(input("how many book do you want : "))
books = []

for i in range(how_many_book):
    book_name = input("please enter a book name : ")
   
    books.append(book_name)

print(f"your book is {books}")