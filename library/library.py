class Book:
    def __init__(self, title="", author="", publisher="", copyright=""):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.copyright = copyright

    def __str__(self):
        return ("Title: %sAuthor: %sPublisher: %sCopyright: %s" %
                (self.title, self.author, self.publisher, self.copyright))


if __name__ == "__main__":
    with open("books.txt") as book_list:
        book1 = Book()
        book2 = Book()
        book3 = Book()
        book4 = Book()
        # need to read through each line and assign to corresponding variable
        contents = book_list.readlines()
        book1.title = contents[0]
        book1.author = contents[1]
        book1.publisher = contents[2]
        book1.copyright = contents[3]
        book2.title = contents[4]
        book2.author = contents[5]
        book2.publisher = contents[6]
        book2.copyright = contents[7]
        book3.title = contents[8]
        book3.author = contents[9]
        book3.publisher = contents[10]
        book3.copyright = contents[11]
        book4.title = contents[12]
        book4.author = contents[13]
        book4.publisher = contents[14]
        book4.copyright = contents[15]
        library = [book1, book2, book3, book4]
        print("The library has 4 books:\n")
        for books in library:
            print(books)
