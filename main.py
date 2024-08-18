book_path = "books/frankenstein.txt"

def main():
    text = book_text(book_path)
    wordcount = word_count(text)
    print(f"{wordcount} words found in the document")

def book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    list=text.split()
    return(len(list))


main ()