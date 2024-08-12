from tkinter import *
import pandas as pd
import random
import os.path
# from time import time
# import copy

BACKGROUND_COLOR = "#B1DDC6"
countdown_timer = None
DF = pd.read_csv('data/french_words.csv')
dict = DF.to_dict(orient="records")




CHOSEN_WORD = None
CHOSEN_WORD_DICT = {}
PATH = r"D:\Projects\Python\100day_challenge\projects\31day\data\words_to_learn.csv"

        
def generate_words_to_learn():
    global CHOSEN_WORD, countdown_timer

    DF_TO_LEARN = pd.read_csv('data/words_to_learn.csv')
    dict_to_learn = DF_TO_LEARN.to_dict(orient="records")
    window.after_cancel(countdown_timer)

    print(f"{dict_to_learn} aaaa from word to learn")
    CHOSEN_WORD = random.choice(dict_to_learn)
    front_card()
    countdown_timer = window.after(3000,back_card)
    
    print(f'{CHOSEN_WORD}')

def check_words_to_learn_exist():
    global DF
    if os.path.exists(PATH) == True:
        print("naa")
        generate_words_to_learn()
    else:
        print("wala")
        generate_words()



def back_card():
    canvas.itemconfig(card_title,text="English",fill="White")
    canvas.itemconfig(canvas_image, image = card_back)
    canvas.itemconfig(card_word,text=f"{CHOSEN_WORD['English']}", fill= "white")


def front_card():
    canvas.itemconfig(card_title,text="French", fill="black")
    canvas.itemconfig(canvas_image, image = card_front)
    canvas.itemconfig(card_word,text=f"{CHOSEN_WORD['French']}", fill="black")


def generate_words():
    global CHOSEN_WORD, countdown_timer
    window.after_cancel(countdown_timer)
    CHOSEN_WORD = random.choice(dict)
    front_card()
    countdown_timer = window.after(3000,back_card)
    
    print(f'{CHOSEN_WORD}')
    # print(f'{type(CHOSEN_WORD)}')
    # print(f'{type(dict)}')
    # print(f'{dict}')
    
    # print(f"{CHOSEN_WORD['French']}")
    # print(f"{CHOSEN_WORD['English']}")
   
 

def remove_word():
    # check_words_to_learn_exist()
    if CHOSEN_WORD in dict:
        dict.remove(CHOSEN_WORD)
        df = pd.DataFrame(dict)
        df.to_csv("data/french_words.csv", mode='w', index=False,)

        words_to_learn_df = df.copy()
        words_to_learn_df.to_csv("data/words_to_learn.csv", mode='w', index=False)
        generate_words()
        

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
countdown_timer = window.after(3000,func = generate_words)

canvas = Canvas(width=850, height=576, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(425,260)
canvas.grid(column=1,row=1,columnspan=2)

card_title = canvas.create_text(425,150, text="Title", fill="black", font=("Ariel", 40, "italic"))
canvas.grid(column=1,row=1)
card_word = canvas.create_text(425,263, text="word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=1,row=1)

wrong_bt = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_bt, highlightthickness=0, command=check_words_to_learn_exist)
button_wrong.grid(column=1,row=2)

right_bt = PhotoImage(file="images/right.png")
button_right = Button(image=right_bt, highlightthickness=0, command=remove_word)
button_right.grid(column=2,row=2)

check_words_to_learn_exist()
# generate_words()





window.mainloop()











# def remove_words_to_learn():
#     generate_words()
#     df = pd.DataFrame(dict)
#     df.to_csv("data/words_to_learn.csv", mode='w', index=False)
#     dict = df.to_dict(orient="records")

#     print(dict)
    # if CHOSEN_WORD in dict:
    #     dict.remove(CHOSEN_WORD)
        

        
                


# def remove_word():
#     if CHOSEN_WORD in dict:
#         dict.remove(CHOSEN_WORD)
#         new_word_dict = copy.deepcopy(list(CHOSEN_WORD.values()))

#         # print(list(demoDictionary.values()))
#         df = pd.DataFrame([new_word_dict])
#         df.to_csv("data/words_to_learn.csv", mode='a', index=False, header=False)

#         generate_words()

#         print(f'{new_word_dict} aaaaa new dictionary' )
#         print(df)
   
#     else:
#         print("wala")

