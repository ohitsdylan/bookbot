import sys
from stats import count_words
from stats import count_characters
from stats import book_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    # print(get_book_text("books/frankenstein.txt"))
    # print(count_words("books/frankenstein.txt"))
    # print(count_characters("books/frankenstein.txt"))
    print(book_report(sys.argv[1]))

main()