from HTMLParser import HTMLParser

class Parser(HTMLParser):
    def __init__(self):
        self.links = []
        HTMLParser.__init__(self)
    
    def handle_starttag(self, tag, attrs):
        links = self.links
        if tag == "a":
            for attr in attrs:
                key, value = attr
                if key == "href":
                    links += [value]

    def flush(self):
        copy = self.links[:]
        self.links = []
        return copy
        
