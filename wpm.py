import time
import random
from tkinter import *

words = []
user_words = []
score = 0

def timer(count):
    if count > 0:
        time = window.after(1000, timer, count-1)
        test()
    timer_label.config(text=count)


def random_words():
    lines = open("words.txt").read().splitlines()
    for word in range(50):      #generate 50 random words
        word = random.choice(lines)
        words.append(word)
        text_label.config(text=words)

def test():
    global score
    user = user_label.get()
    if user in words:
        user_words.append(user)
        user_label.delete(0, "end")
        score += 1
        words_guessed_label.config(text=f"You have guessed: {score} words")
    user_words_label.config(text=user_words)



def start():
    timer(60)
    random_words()
    #window.bind("<Return>", test)  # do function when Enter pressed

window = Tk()
window.title("Words per minute")
window.geometry("1000x750")
timer_label = Label(text="60")
timer_label.grid(column=0, row=0)
text_label = Label(text="How many words can you type in one minute?")
text_label.grid(column=0, row=1)
user_label = Entry(width=40)
user_label.grid(column=0, row=2)
user_words_label = Label(text="")
user_words_label.grid(column=0, row=3)

words_guessed_label = Label(text="You have guessed: 0 words")
words_guessed_label.grid(column=2, row=4)
start_button = Button(text="Start", command=start)
start_button.grid(column=0, row=4)
window.mainloop()
