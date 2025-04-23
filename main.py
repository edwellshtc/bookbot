import sys
from stats import character_num
from stats import word_count
from stats import get_book_text
from stats import report_list
from stats import sort_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    text = get_book_text(sys.argv[1])
    count = word_count(text)
    characters = character_num(text)
    report = report_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for character_dict in report:
        char = character_dict["char"]
        if char.isalpha():
            count = character_dict["count"]
            print(f"{char}: {count}")
    print("============= END ===============")


main()