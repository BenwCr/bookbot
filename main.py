book_path = "books/frankenstein.txt"
alphabet_string = 'abcdefghijklmnopqrstuvwxyz'

def main():
    text = book_text(book_path)
    wordCount = word_count(text)
    charDict = char_count(text)
    char_sort_list = sort_character(charDict)
    
    print(f"\n--- Begin report of {book_path} ---\n")
    print(f"{wordCount} words found in the document\n")
    for d in char_sort_list:
        print(f"The '{d[0]}' character was found {d[1]} times")
    print("\n--- End report ---")
    
def book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    list=text.split()
    return(len(list))

def char_count(text):
    loweredCase = text.lower()
    dictResult = {}
    for char in loweredCase:
        count = 0
        if char not in dictResult and char in alphabet_string: #chat must appear in alphabet_list
            dictResult[char] = 1
        elif char in alphabet_string:
            dictResult[char] += 1


    return dictResult



def sort_character(dict):
    return sorted(dict.items(), key=lambda item: item[1],reverse=True)


main ()