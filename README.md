from urllib.request import urlopen
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_price = False
        self.books = []
        self.current_title = ""
        self.current_price = ""

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "title":
                    self.current_title = attr[1]
                    self.in_title = True
        if tag == "p":
            for attr in attrs:
                if attr == ("class", "price_color"):
                    self.in_price = True

    def handle_data(self, data):
        if self.in_price:
            self.current_price = data.strip()
            if self.current_title:  
                self.books.append((self.current_title, self.current_price))
                self.current_title = ""
            self.in_price = False

url = "http://books.toscrape.com/"
html = urlopen(url).read().decode("utf-8")
parser = MyHTMLParser()
parser.feed(html)
for title, price in parser.books:
    print(f"Title: {title}, Price: {price}")
