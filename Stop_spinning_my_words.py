# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.

# Examples:
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"


def spin_words(sentence):
    
    words = []
    output_word = []
    output = ""
    change =""
    i= 0

    words =sentence.split()
    for word in words:
        if len(word) >= 5:
            for char in range(len(word) - 1, -1,-1):
                change += word[char]
            output_word.append(change)
        else:
            output_word.append(word)
        change = ""
    
    output = ' '.join(output_word)

    return output

if __name__ == "__main__":

    sentence = "Hey fellow warriors"
    output = spin_words(sentence)

    print(output)