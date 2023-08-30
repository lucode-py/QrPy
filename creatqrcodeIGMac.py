# importation des module
from tkinter import *
from tkinter import messagebox
import os
import sys




try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_L
except:
    import os
    os.system("pip3 install qrcode[pil]")
    import qrcode
    from qrcode.constants import ERROR_CORRECT_L


color_qrcode: str = "black"
color_font_qrcode: str = "white"

# creation de la fenêtre
window = Tk()
window.title('QrPy')
window.geometry('950x550')
window.minsize(600, 350)
title = Label(window, text='Créer votre QR code', font=("calibri", 50))
title.pack(pady=12)

# création de la Frame qui contiaint les instructions
Frame = Frame(window)

label_entry_data = Label(Frame, text="entrer l'url du qrcode", font=("calibri", 18))
label_entry_data.pack()
entry_data = Entry(Frame, font=('calibri', 15))
entry_data.pack()

# fonction des boutton

def color_blue():
    global color_qrcode
    color_qrcode = "blue"

def color_red():
    global color_qrcode
    color_qrcode = "red"

def color_green():
    global color_qrcode
    color_qrcode = "green"

def color_white():
    global color_qrcode
    color_qrcode = "white"

def color_black():
    global color_qrcode
    color_qrcode = "black"
    
def color_bg_blue():
    global color_font_qrcode
    color_font_qrcode = "blue"
    
def color_bg_red():
    global color_font_qrcode
    color_font_qrcode = "red"

def color_bg_green():
    global color_font_qrcode
    color_font_qrcode = "green"
    
def color_bg_white():
    global color_font_qrcode
    color_font_qrcode = "white"
    
def color_bg_black():
    global color_font_qrcode
    color_font_qrcode = "black"

def enregistrée():
    try:
        data_get = entry_data.get()
        save_get = save_entry.get()
        if data_get == "" or save_get == "":
            messagebox.showerror('erreur', "Erreur:\n assurer vous d'avoir bien remplis tout les champs de texte")
        else:
            qr = qrcode.QRCode(
                version=3,
                error_correction=ERROR_CORRECT_L,
                box_size=10,
                border=5
            )
            qr.add_data(data_get)
            qr.make(fit=True)
            img = qr.make_image(fill_color=color_qrcode, back_color=color_font_qrcode)
            img.save(save_get + ".png")

    except:
        messagebox.showerror('erreur', "Erreur:\nassurer vous d'avoir bien remplis tout les champs de texte")

color_label = Label(Frame, text="cliquer sur la couleur du qrcode", font=("calibri", 18))
color_label.pack()
blue_button = Button(Frame, text="bleu", font=("calibri"), command=color_blue)
blue_button.pack()
red_button = Button(Frame, text="rouge", font=("calibri"), command=color_red)
red_button.place(x=70, y=85)
green_button = Button(Frame, text="verte", font=("calibri"), command=color_green)
green_button.place(x=(5), y=(85))
white_button = Button(Frame, text="blanc", font=("calibri"), command=color_white)
white_button.place(x=197, y=85)
black_button = Button(Frame, text="noire", font=("calibri"), command=color_black)
black_button.place(x=266, y=85)

# color de font 

label_color_back = Label(Frame, text="cliquer sur la couleur de font que tu veut", font=("calibri", 18))
label_color_back.pack()

color_back_bleu = Button(Frame, text="bleu", font=("calibri"), command=color_bg_blue)
color_back_bleu.pack()

color_back_red = Button(Frame, text="rouge", font=("calibri"), command=color_bg_red)
color_back_red.place(x=70, y=139.5)

color_back_green = Button(Frame, text="verte", font=("calibri"), command=color_bg_green)
color_back_green.place(x=5, y=139.5)

color_back_white = Button(Frame, text="blanc", font=("calibri"), command=color_bg_white)
color_back_white.place(x=197, y=139.5)

color_back_black = Button(Frame, text="noire", font=("calibri"), command=color_bg_black)
color_back_black.place(x=266, y=139.5)

save_label = Label(Frame, text="      entrer le nom de le nom de l'image      ", font=("calibri", 18))
save_label.pack()
save_entry = Entry(Frame, font=('calibri', 15))
save_entry.pack()

button_qrcode = Button(Frame, text="généré", font=("calibri", 20), command=enregistrée)
button_qrcode.pack()

Frame.pack(expand=YES)
window.mainloop()
