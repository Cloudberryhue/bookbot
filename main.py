def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    book_word = count_the_words(text)
    character_count = count_the_characters(text)
    #print(character_count)
    book_dict = character_count.copy()
    dict_report = dict_list(book_dict)
    sort_key = sort_on(book_dict)
    dict_report.sort(key=sort_on, reverse=True)
    filtered_list = []
    for dict_item in dict_report:
        for char, count in dict_item.items():
            if char.isalpha():
                filtered_list += dict_item.items()
    
    print(f"--- Begin report of {book_path} --- \n{book_word} words found in the document")
    for x ,z in filtered_list:
        print(f"The '{x}' character was found {z} times")
    print("--- End report ---")

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

def dict_list(char_dict):
    report_list = [{k: v} for k, v in char_dict.items()]
    return report_list

def sort_on(item):
    return list(item.values())[0]



main()