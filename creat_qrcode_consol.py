try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_L
    import termcolor
    import os
except:
    import os
    os.system("pip install qrcode[pil]")
    os.system("pip install termcolor")
    import qrcode
    from qrcode.constants import ERROR_CORRECT_L
    from termcolor import *
valid = False
url_qrcode = input("entrée l'url du qrcode: ")
name_qrcode = input("entrée le nom du qrcode: ")
while valid == False:
    print("vous pouvez choisire les couleur suivente : \n"
          + termcolor.colored("red", "red", attrs=["bold"]) + "   " +
          termcolor.colored("blue", "blue", attrs=["bold"]) + "   " +
          termcolor.colored("green", "green", attrs=["bold"]) + "   " +
          termcolor.colored("yellow", "yellow", attrs=["bold"]) + "\n"
          + termcolor.colored("brown", attrs=["bold"]) + "   " +
          termcolor.colored("orange", "light_red", attrs=["bold"]) + "   " +
          termcolor.colored("white", attrs=["bold"]) + "   " +
          termcolor.colored("black", "black", "on_white", attrs=["bold"]))
    
    color_qrcode = input("entrez la couleur du qrcode: ")
    
    color_font_qrcode = input("entrez la couleur de font du qrcode: ")
    
    try:
        qr = qrcode.QRCode(
                    version=3, error_correction=    ERROR_CORRECT_L,
                    box_size=3,
                    border=5
                )
        qr.add_data(url_qrcode)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color_qrcode, back_color=color_font_qrcode)
        img.save(name_qrcode + ".png")
        valid = True
    except:
        os.system("clear")
        os.system("cls")
        print("vous n'avais pas du rentré les bonne couleur ")