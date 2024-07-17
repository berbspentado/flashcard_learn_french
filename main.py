from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=850, height=576, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="images/card_front.png")
canvas.create_image(425,260, image = logo_img,)
canvas.grid(column=1,row=1,columnspan=2)

wrong_bt = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_bt, highlightthickness=0)
button_wrong.grid(column=1,row=2)

right_bt = PhotoImage(file="images/right.png")
button_right = Button(image=right_bt, highlightthickness=0)
button_right.grid(column=2,row=2)

foreign_text = canvas.create_text(425,150, text="Japanese", fill="black", font=("Ariel", 40, "italic"))
canvas.grid(column=1,row=1)

english_text = canvas.create_text(425,263, text="English", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=1,row=1)

window.mainloop()