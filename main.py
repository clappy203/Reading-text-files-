# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename): 
    '''
        This function reads a file from a directory.
        args: .txt file
    '''
    # [assignment] Add your code here 
    with open(filename,"r") as openfile:
        readfile = openfile.read()
        print(readfile)
    return readfile        

readfile = read_file_content("./story.txt")



def count_words():
    '''
        this function counts the occurrence of words in a file
    '''
    text = read_file_content("./story.txt")
    
    split_txt = text.split()
    
    word_count = {}

    for word in split_txt:
        if word in word_count:
            word_count[word] += 1
        else :
            word_count[word] = 1

    return word_count

print(count_words())

