
from stats import get_num_words, count_char, sort_list
import sys
if len(sys.argv) != 2:
    sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents




def main():
    char_view = count_char(get_book_text(sys.argv[1]))
    lists = sort_list(char_view)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    
   
    
    for l in lists:
        print(f"{list(l.keys())[0]}: {list(l.values())[0]} ")


main()

