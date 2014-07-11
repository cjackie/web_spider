#!/usr/bin/python

import sys 
import urllib2 
from Parser import Parser
from urlparse import urljoin, urlparse

def is_link(link):
    if urlparse(link).scheme == "http" or urlparse(link).scheme == "https":
        return True
    else:
        return False

def spread(url, parser, links_set):
    content = None
    links_set.add(url)

    try:
        content = urllib2.urlopen(url, None, 500).read()
    except:
        pass

    result = []
    if not content is None:
        links = []
        try:
            parser.feed(content)
            links = parser.flush()
        except:
            pass

        for link in links:
            if not link in links_set:
                new_link = urljoin(url, link)
                if link[:1] == "#" or new_link in links_set or not is_link(new_link):
                    continue
                print new_link
                result += [new_link]
    return result

if __name__ == "__main__":
    if sys.argv < 2:
        print "usage: <url> "
        exit(1)

    urls = [sys.argv[1]]
    parser = Parser()
    all_links = set()
    
    while True:
        new_urls = []
        for url in urls:        
            new_urls = spread(url, parser, all_links)
        if len(new_urls) == 0:
            break;
        else:
            urls = [url for url in new_urls if url not in all_links]            


    

        
