import json
def show_book(books):
    for book in books:
        print(f"your book is {book}")

def save_book(books):
    with open("book.json", "w", encoding="utf-8") as File:
        json.dump(books, File, ensure_ascii=False, indent=2)

def load_book():

    try:

        with open("book.json", "r", encoding="utf-8")as File:
            return json.load(File)
        
    except (FileNotFoundError, json.decoder.JSONDecodeError):

        return[]

