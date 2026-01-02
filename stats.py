def get_book_text(book_title):
    with open(book_title) as f:
    
     file_contents = f.read()
     count_words = str.split(file_contents)
     return len(count_words)

def char_stats(book_title):
    with open(book_title) as p:
        letter = {}
        file_contents = p.read()
        lowered = str.lower(file_contents)
               
        for i in range (0, len(lowered)):
           ch = lowered[i]
           if ch not in letter:
                letter[ch] = 1
                
           else:
               letter[ch] = letter[ch] + 1

        return letter
               
               
           
           
        
    