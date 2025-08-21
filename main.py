from stats import get_word_count
from stats import sort_char_count
import sys

def main():
    if sys.argv.__len__() < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(path)} total words")
    print("--------- Character Count -------")
    chars = sort_char_count(path)
    for k in chars:
        print(f"{k["char"]}: {k["num"]}")
    print("============= END ===============")

main()
