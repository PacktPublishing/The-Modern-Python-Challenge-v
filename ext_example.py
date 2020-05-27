# -*- coding: utf-8 -*-
import math
from collections import defaultdict

file ='heart_dark.txt'
f = open(file, 'rb')
data = f.read()
data = str(data)
CHARACTERS =["Kurtz", "manager", "Russian",
             "pilgrims", "cannibals", "aunt",
             "brickmaker", "Accountant", "helmsman",
             "mistress", "intended", "Marlow",
             "Fresleven"]

def paginate(data, page_length):
    words = data.split()
    page_count = math.ceil(len(words) / page_length)
    pages = defaultdict(str)
    pointer = 0
    for page in range(1, page_count +1):
        pages[page] = words[pointer: pointer + page_length]
        pointer += page_length
    return pages    

def get_names(data, characters=CHARACTERS):
    data = data.strip().split()
    punctuation = '.,?!;-'
    data[:] = [word.strip(punctuation) for word in data]
    names = []
    for word in data:
        if word in characters:
            names.append(word)
    return set(names), len(names), len(characters)        

def make_index(names, pages):
    index = defaultdict(list)
    names = list(names[0])
    for name in names:
        for page in range(1, len(pages) + 1):
            if name in pages[page]:
                index[name].append(page)
    return index            

def print_index(index):
    for name, pages in sorted(index.items()):
        print("{:20}".format(name), end="", flush=True)
        for number in pages:
            print(number, end="," if not number == pages[-1] else "")
        print()    







