# Arman Uddin
# Section 2N Tuesday 12:30pm - 1:45 pm

def inOrderVowel():
    word = ""
    alpha_check = ""
    with open("dictionary.txt", "r+") as dictionary:
        for char in dictionary:
            if char != '\n':
                word = word + char

            word = word.lower().strip()
            for letter in word:
                if isVowel(letter):
                    alpha_check = alpha_check + letter

            if alpha_check == 'aeiou':
                print(word)

            word = ""
            alpha_check = ""


def isVowel(letter):
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'

inOrderVowel()
# Prints Every Word from list on wikipedia
# Ex:
#   facetious
#   travertinous
#   abstenious
#   aeiou
#
# Does not print:
#   testing
#   Hello World
#   eiaou
#   aeeeeiiiioouu