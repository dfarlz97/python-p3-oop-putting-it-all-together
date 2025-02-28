#!/usr/bin/env python3

class Book:
    def __init__(self, title, author="", page_count=0, genre=""):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.genre = genre
    
 
    def set_page_count(self,page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    
    def get_page_count(self):
        return self._page_count
    

    page_count = property(get_page_count, set_page_count)