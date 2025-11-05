import sys

from stats import f_num_words
from stats import f_num_letters
from stats import f_letter_freq_sort

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

v_filepath = sys.argv[1]
# file_contents = ""
# word_cnt = ""

def f_get_book_text(p):
    with open(p) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    v_get_book_text = f_get_book_text(v_filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {v_filepath}...")
    print("----------- Word Count ----------")

    v_num_words = f_num_words(v_get_book_text)
    print(f"Found {v_num_words} total words")

    print("--------- Character Count -------")

    v_num_letters = f_num_letters(v_get_book_text)
    # print(v_num_letters)

    v_letter_freq_sort = f_letter_freq_sort(v_num_letters)
    
    # print(v_letter_freq_sort)

    for i in v_letter_freq_sort:
        if i["letter"].isalpha():
           print(f"{i['letter']}: {i['num']}")

    # for i in v_letter_freq_sort:
    #     if v_split_dict.isalpha("letter"):
    #         print(v_letter_freq_sort)

    print("============= END ===============")

main()