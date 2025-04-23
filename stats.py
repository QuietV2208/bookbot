
def count_text(book_string):
    string = book_string.split()
    num = len(string)
    return num

def count_chars(book_string):
    lower = book_string.lower() 
    words = lower.split()
    chars = {}
    for word in words: 
        for letter in word:
            if letter in chars:
                chars[letter] += 1
            else:
                chars[letter] = 1
    return chars

def sort_on(dict):
    return dict["num"]
            
def sorted_list(chars):
    lst = []
    for i in chars:
        ea = {}
        if i.isalpha():
            ea = dict(letter=i, num=chars[i])
            lst.append(ea)
    lst.sort(reverse=True, key=sort_on)
    return lst
