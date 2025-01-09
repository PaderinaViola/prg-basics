class Book:
    def __init__(self, title, author, page_numbers):
        self.title = title
        self.author = author
        self.page_numbers = page_numbers
        self.current_page = 1
        self.book_opened = False

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPage numbers: {self.page_numbers}\nCurrent page number: {self.current_page}"
    
    def open_book(self):
        self.book_opened = True

    def close_book(self):
        self.book_opened = False

    def next_page(self, numb_pages_ahead):
        if self.book_opened == True:
            self.current_page += numb_pages_ahead
        elif self.book_opened == False:
            print("Bro you can't change pages with a closed book")

    def previous_page(self, numb_pages_previous):
        self.current_page += numb_pages_previous

    def book_status(self):
        if self.book_opened:
            print(f"The book is opened on the page {self.current_page}")
        else:
            print(f"The book is closed")