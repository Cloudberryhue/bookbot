def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    book_word = count_the_words(text)
    #print(text)
    print(book_word)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_the_words(book):
    words = book.split()
    return len(words)

main()