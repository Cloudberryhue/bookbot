def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    book_word = count_the_words(text)
    character_count = count_the_characters(text)
    #print(text)
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_the_words(book):
    words = book.split()
    return len(words)

def count_the_characters(characters):
    lower_character = characters.lower()
    character_dict = {}
    for i in lower_character:
        if i in character_dict:
            character_dict[i] += 1
        else:
            character_dict[i] = 1
    return character_dict


main()