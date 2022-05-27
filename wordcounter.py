def WordCounter(anytext):
    res = len(anytext.split())

    # total no of words
    print ("The number of words in string are : " + str(res))




mytext= input("Enter the text to be counted: ")
WordCounter(mytext)
