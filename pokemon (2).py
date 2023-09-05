import pypokedex
import PIL.Image , PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

window = tk.Tk()
window.geometry("600x500")
window.title("POKEDEX")
window.config(padx=10, pady=10)

title_label = tk. Label(window, text="POKEDEX ")
title_label.config(font=("Arial", 32))
title_label.pack (padx=10, pady=10)

pokemon_image = tk.Label(window )
pokemon_image.pack()



image = PIL.Image.open("votre_image.jpg")  # Remplacez "votre_image.jpg" par le chemin de votre propre image
photo = PIL.ImageTk.PhotoImage(image)


pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk. Label (window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

# FUNCTION
def load_pokemon ():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} {pokemon.name}")
    pokemon_types.config(text=f"{pokemon.types}")
                     

label_id_name = tk.Label(window, text="ID_or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack (padx=10, pady=10)

text_id_name = tk.Text(window, height=1 , width=20 , bg="black" , fg="white" )
text_id_name.config (font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button (window, text="Load Pokemon" , command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)


mainmenu = Menu(frame)
mainmenu.add_command(label = "Save", command= save)  
mainmenu.add_command(label = "Load", command= load)
mainmenu.add_command(label = "Exit", command= root.destroy)

window.mainloop()