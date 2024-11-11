def sort_on(dict): # sorts the dictionary
    return dict["num"]

def count_words(text):    # counts the words
    words = text.split()
    number_of_words = len(words)
    return number_of_words


def count_characters(text): # counts the characters, returns it on dictionaries, sorted by most common
    characters_dict = {}
    lowered_string = text.lower()
    for character in lowered_string:
        if character.isalpha():
            if character in characters_dict:
                characters_dict[character] += 1
            else:
                characters_dict[character] = 1

    dictionary_list = []
    for char, num in characters_dict.items():
        char_dict = {'char': char, 'num': num}
        dictionary_list.append(char_dict)
    
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print_report(file_contents)
    
def print_report(text): # prints the report
    word_count = count_words(text)
    char_count = count_characters(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for item in char_count:  # loop through sorted list
        print(f"The '{item['char']}' character was found {item['num']} times")
        
    print("--- End report ---")

main()