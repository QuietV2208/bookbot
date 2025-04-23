from stats import sorted_list, count_chars, count_text



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    path = "./books/frankenstein.txt"
    words = count_text(get_book_text(path))     # returns word count of from get_book_text
    chars = count_chars(get_book_text(path))    # returns dict {letter: times_occured}
    lst =  sorted_list(count_chars(get_book_text(path)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for i in lst:
        print(f"{i["letter"]}: {i["num"]}") 
    print("============= END ===============")

main()
