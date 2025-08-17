import sys
from stats import count_words, count_chars, sorted_alphas

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def usage(argv):
    print(f"Usage: python3 {argv[0]} <path_to_book>")


def main():
    #print(f"{len(sys.argv)=}")
    if len(sys.argv) < 2:
        usage(sys.argv)
        sys.exit(1)

    file = sys.argv[1]
    print("============ BOOKBOT ============")
    
    print(f"Analyzing book found at {file}...")

    text = get_book_text(file)

    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_chars_dict = count_chars(text)
    #for key in num_chars_dict:
    #    print(f"'{key}': {num_chars_dict[key]}")

    sorted = sorted_alphas(num_chars_dict)
    for entry in sorted:
        print(f"{entry['name']}: {entry['num']}")

    print("============= END ===============")

main()