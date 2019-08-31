
import operator
with open("words.txt","r") as f:
    word_list = f.read().splitlines()

five_letter = {}
for word in word_list:
    if len(word) == 5:
        five_letter[word[4]] = five_letter.get(word[4], 0)+ 1

sorted_x = sorted(five_letter.items(), key=operator.itemgetter(1))
print(sorted_x)