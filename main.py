from stats import get_book_text, char_stats

def main():
    num_words = get_book_text("./books/frankenstein.txt")
    num_char  = char_stats("./books/frankenstein.txt")
    print(f"Found {num_words} total words\n {num_char}")


main()
