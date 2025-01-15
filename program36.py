class Publisher:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Publisher: {self.name}")

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages
