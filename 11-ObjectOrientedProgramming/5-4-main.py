from module5_4 import Book
def main():
    dune = Book("Dune", "Frank Herbert", 567)
    print(dune)
    dune.open_book()
    dune.book_status()
    dune.next_page(13)
    dune.book_status()
    dune.close_book()
    dune.book_status()
    dune.next_page(13)
    
if __name__ == "__main__":
   main()
