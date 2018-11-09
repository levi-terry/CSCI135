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
        library = []
        for line in book_list:
            title = line
            author = book_list.readline()
            publisher = book_list.readline()
            copyright = book_list.readline()
            library.append(Book(title, author, publisher, copyright))
        print("The library has %d books:" % len(library))
        for books in library:
            print(books)
