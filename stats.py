def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    text = get_book_text(book_text)
    words = text.split()
    count = f"{len(words)}"
    return count

def count_characters(book_text):
    dict = {}
    text = get_book_text(book_text)
    letters = text.lower().split()
    
    for letter in letters:
        for char in letter:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    return dict

def book_report(book_text):

    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    list = []

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_text}")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    def sort_on(list):
        return list["num"]
    
    for i in char_count:
        list.append({"item": i, "num": char_count[i]})

    list.sort(reverse=True, key=sort_on)
    
    for x in list:
        if x["item"].isalpha():
            print(f"{x['item']}: {x['num']}")

    print("============= END ===============")