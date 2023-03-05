#https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for a,b in attrs:
            print("-> {} > {}".format(a,b))
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for a,b in attrs:
            print("-> {} > {}".format(a,b))
x=""        
for _ in range(int(input())):
    x+=input()
    
parser = MyHTMLParser()   
parser.feed(x)
