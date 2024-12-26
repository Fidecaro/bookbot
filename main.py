def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_count = characters(text)
    #print(text)
    #print("words: " ,count(text))
    #print(letter_count)
    letter_count_list=dic_convert(letter_count)    
    letter_count_list.sort(reverse=True, key=sort_on)
    print_report(letter_count_list,text)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count(text):
    words = text.split()
    wordcount = len(words)
    count = 0
    for i in words:
        count +=1
    print(count)
    return wordcount

def characters(string):
    lowered_string = string.lower()
    alphabet={    
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0
    }
    
    for char in lowered_string:
        try:
            alphabet[char] +=1
        except:
            pass
    return alphabet

def dic_convert(dic):
    list = []
    for char in dic:
        list.append({"char": char, "num": dic[char]})
    return list


def sort_on(dict):
    return dict["num"]

def print_report(report,text):
    print(count(text),"--- Begin report of books/frankenstein.txt ---")
    print(" words found in the document")
    print()
    for lett in report:
        print("The ", lett["char"] , " character was found " , lett["num"] ," times")
    print("--- End report ---")

main()