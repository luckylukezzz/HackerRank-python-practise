#https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        if attrs:
            for a,b in attrs:
                print("-> {} > {}".format(a,b))
    
    def handle_startendtag(self, tag, attrs):
        print (tag)
        if attrs:
            for a,b in attrs:
                print("-> {} > {}".format(a,b))
x=""        
for _ in range(int(input())):
    x+=input()
    
parser = MyHTMLParser()   
parser.feed(x)
