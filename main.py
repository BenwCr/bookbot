book_path = "books/frankenstein.txt"

def main():
    text = book_text(book_path)
    wordCount = word_count(text)
    charDict = char_count(text)
    print(f"{wordCount} words found in the document\n{charDict}")

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
        if char not in dictResult:
            dictResult[char] = 1
        else:
            dictResult[char] += 1


    return dictResult


main ()