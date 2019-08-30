from tkinter import Entry, Tk

root = Tk()

def func(event):
    print("You hit return.")
    global e
    global word
    word = e.get()
    root.destroy()


root.bind('<Return>', func)


e = Entry(root, bd=5, width=20, show="*")
e.pack()
e.focus_set()
root.mainloop()

#word = input("Please input a word for someone to guess: ")
word = word.lower()
length = len(word)
print("The input has", length, "letters")

current_string = list("-"*length)
game_over = False
letters_guessed = []
strike_count = 0
print("".join(current_string))

while not game_over:
    guessed_letter = input("Please guess a letter: ")
    while len(guessed_letter) != 1:
        guessed_letter = input("Guess only one letter: ")
        print("".join(current_string))

    guessed_letter = guessed_letter.lower()
    while guessed_letter in letters_guessed:
        guessed_letter = input("Letter already guessed: ")
        print("".join(current_string))

    letters_guessed.append(guessed_letter)

    if guessed_letter in word:
        for i in range(0, length):
            if word[i] == guessed_letter:
                current_string[i] = guessed_letter
    else:
        strike_count += 1
        print("You have", strike_count, "Strikes")

    print("".join(current_string))
    if strike_count == 6:
        game_over = True
        print("Game is over")
        print("The word was", word)

    if "-" not in current_string:
        print("YOU WON")
        game_over = True
