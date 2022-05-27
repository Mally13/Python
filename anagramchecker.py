# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    sword=word.strip()
    sanagram=anagram.strip()

    if len(sword)== len(sanagram):
        sortedsword=sorted(sword)
        sortedsanagramlist=sorted(sanagram)

        if (sortedsword==sortedsanagramlist):
            print(word +" and " + anagram +" are anagram \N{grinning face}!")
            return True
        else:
            print(word +" and " + anagram +" are not anagram!")
            return False
    
    else:
        print(word +" and " + anagram +" are not anagram!")
        return False

print("""
An anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original 
letters exactly once.

For example, the word anagram itself can be rearranged into nag a ram,
also the word binary into brainy and the word adobe into abode
""")

word=str(input('Enter your first word or phrase: ')).lower()
anagram=str(input('Enter your second word or phrase: ')).lower()

print("Lets find out ...")

find_anagram(word, anagram)