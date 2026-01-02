from stats import get_book_text, char_stats

def main():
    file_name = "./books/frankenstein.txt"
    num_words = get_book_text(file_name)
    num_char  = char_stats(file_name)
    print (f"============ BOOKBOT ============\nAnalyzing book found at {file_name}\n----------- Word Count ----------\nFound {num_words} total words \n--------- Character Count -------\n {num_char}\n============= END ===============\n")

main()
