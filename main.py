def main():
    # Grabs the text file
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # Links the text to the word count function
    num_words = number_of_words(text)
    
    # Links the text to the letter count function
    letter_count = number_of_letters(text)

    # Takes the results from letter count in which it gets formatted
    report = match_report(letter_count)
    
    print(f"--- Begin report of {book_path} ---\nThere are {num_words} words found in the document.\n\n\n{report}\n---End report---")
    

# Gets the text out of the file 
def get_book_text(path):
    with open(path) as f:
        return f.read()


# Word count for the text file    
def number_of_words(text):
    split_words = text.split()
    return len(split_words)


# My first solution
''''
def number_of_letters(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    output = []
    low_case = text.lower()
    for i in alphabet:
        output.append(f"{i}: {low_case.count(i)}")
    return output     
'''

# Takes the text, sorts and lowers it before counting the matches while skipping spaces and new lines
def number_of_letters(text):
    chars = {}
    sort = sorted(text.lower())
    for i in sort:
        if i == " ":
            continue
        if i == "\n":
            continue
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars


# Takes the sorted matched letters from the function above to format it
def match_report(result):
    n = ""
    for i in result:
        n += f"The letter {i} was found {result[i]} times\n"
    return n   
   
    


main()

