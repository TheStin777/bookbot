from stats import get_book_text, char_stats,to_sort

def main():
    file_name = "./books/frankenstein.txt"
    num_words = get_book_text(file_name)
    num_char  = char_stats(file_name)
    sorted_chars  = to_sort(num_char)
    lines = []

    for item in sorted_chars:
        ch = item["char"]
        count = item["num"]
        if not ch.isalpha():
            continue
        lines.append(f"{ch}: {count}")
    alphabetized = "\n".join(lines)
    print (f"============ BOOKBOT ============\nAnalyzing book found at {file_name}\n----------- Word Count ----------\nFound {num_words} total words \n--------- Character Count -------\n{alphabetized}\n============= END ===============\n")

main()
