def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def word_count(words):
    num_words = len(words.split())
    return num_words

def character_num(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_list(dict):
    return dict["count"]

def report_list(char_dictionary):
    sorted_list = []
    for char in char_dictionary:
        temp_dict = {}
        count = char_dictionary[char]
        temp_dict = {"char": char, "count": count}
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_list)
    return sorted_list






