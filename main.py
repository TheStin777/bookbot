from stats import get_book_text, char_stats,to_sort
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    num_words = get_book_text(sys.argv[1])
    num_char  = char_stats(sys.argv[1])
    sorted_chars  = to_sort(num_char)
    lines = []

    for item in sorted_chars:
        ch = item["char"]
        count = item["num"]
        if not ch.isalpha():
            continue
        lines.append(f"{ch}: {count}")
    alphabetized = "\n".join(lines)
    print (f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}\n----------- Word Count ----------\nFound {num_words} total words \n--------- Character Count -------\n{alphabetized}\n============= END ===============\n")

main()
