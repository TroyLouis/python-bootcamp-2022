class Book():
    def __init__(self, pages, author, title):
        self.pages = pages
        self.author = author
        self.title = title

    def __str__(self):
        return f'{self.title} by {self.author} is {self.pages} pages.'

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Book object deleted.")

if __name__ == "__main__":
    book = Book(700, "J.K. Rowling", "Harry Potter")
    print(book)
    print(len(book))
    del(book)
