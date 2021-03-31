from tkinter import *
from tkinter.ttk import *

from random import random

answers = []
right_answer = ""

window = Tk()

def check(el):
    global answers
    global right_answer
    global verb

    #print(right_answer)
    #print(verb)

    #for i in answers:
    #    print(i.get())

    for widget in el.winfo_children():
        widget.destroy()

    answer_gerund = answers[0].get()
    #print(answer_gerund)

    answer_infinitive = answers[1].get()
    #print(answer_infinitive)

    win = False

    if right_answer == "Gerund" and answer_gerund == True and answer_infinitive == False:
        win = True

    if right_answer == "Infinitive" and answer_gerund == False and answer_infinitive == True:
        win = True

    if right_answer == "Both" and answer_gerund == True and answer_infinitive == True:
        win = True

    result_label = Label(el, text=f"{win}, \"{verb}\" используется с {right_answer}").pack()

    btn_next = Button(el, text="Next >>", command=lambda e=el: ask_question(e)).pack()



frm = LabelFrame(text="Generate screen")
frm.pack()


gerund = [
    "admit",
    "appreciate",
    "avoid",
    "be worth",
    "burst out",
    "can't help",
    "can't stand",
    "consider",
    "delay",
    "deny",
    "discuss",
    "dislike",
    "enjoy",
    "fancy",
    "feel like",
    "finish",
    "forgive",
    "give up",
    "imagine",
    "involve",
    "keep",
    "mention",
    "mind",
    "miss",
    "postpone (put off)",
    "practice",
    "resist",
    "risk",
    "spend time",
    "suggest",
    "be/get used to",
    "look forward to",
    "object to",
    "how/what about",
    "it's not good/use",
    "there is no point (in)",
    "what's the point/use of"]

infinitive = [
    "afford",
    "agree",
    "appear",
    "arrange",
    "ask",
    "attempt",
    "be glad/pleased",
    "be able/surprised etc",
    "choose",
    "decide",
    "expect",
    "fail",
    "happen",
    "help",
    "hope",
    "learn",
    "manage",
    "offer",
    "prepare",
    "plan",
    "pretend",
    "promise",
    "refuse",
    "seem",
    "want",
    "wish",
    "would like/prefer",
    "used to"]

both = [
    "begin",
    "continue",
    "like",
    "love",
    "hate",
    "prefer",
    "start",
    "intend"]


def first_screen(el):
    Label(el, text='Welcome to my quiz!\n Press "Start" to continue...').pack()
    Button(el, text="Start", command=lambda e=el: ask_question(e)).pack()

first_screen(frm)

def ask_question(el):

    global answers
    global right_answer
    global verb

    for widget in el.winfo_children():
        widget.destroy()

    r = random()
    #print("Random=", r)

    if len(infinitive) + len(both) + len(gerund) == 0:
        all_done(el)

    k1 = len(gerund)/(len(infinitive) + len(both) + len(gerund))

    #print ("K1=", k1)

    k2 = len(infinitive)/(len(gerund) + len(both) + len(infinitive))

    #print ("K2=", k2)

    k3 = 1 - k1 - k2

    #print ("K3=", k3)
    item = ""

    right_answer = ""
    if r <= k1:
        item = gerund.pop()
        right_answer = "Gerund"
        #print("K1 - gerund")
    elif r > k2 and r <= k1 + k2:
        item = infinitive.pop()
        right_answer = "Infinitive"
        #print("K2 - infinitive")
    else:
        item = both.pop()
        right_answer = "Both"
        #print("K3 - infinitive")

    #print(right_answer)

    verb = item
    question = Label(el, text=f"\"{item}\" используется с герундием (+ing), инфинитивом (to + V) или и тем и другим ?").pack()

    answers.clear()
    answers.append(BooleanVar())
    answers.append(BooleanVar())
    ch_1 = Checkbutton(el, text="Gerund", variable=answers[0], onvalue=1, offvalue=0).pack(anchor=W)
    ch_2 = Checkbutton(el, text="Infinitive", variable=answers[1], onvalue=1, offvalue=0).pack(anchor=W)

    btn_next = Button(el, text="Next >>", command=lambda e=el: check(e)).pack()



def all_done(el):
    for widget in el.winfo_children():
        widget.destroy()

    all_done_label = Label(el, text=f"Вопросы закончились, поздравляю").pack()

    btn_next = Button(el, text="Next >>", command=lambda e=el: check(e)).pack()


window.mainloop()
