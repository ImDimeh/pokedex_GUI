import pypokedex
import PIL.Image , PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO
import random

window = tk.Tk()
window.geometry("600x500")
window.title("POKEDEX")
window.config(padx=10, pady=10)

title_label = tk. Label(window, text="POKEDEX ")
title_label.config(font=("Arial", 32))
title_label.pack (padx=10, pady=10)

pokemon_image = tk.Label(window )
pokemon_image.pack()






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
    proba = random.randint(1 , 5)
    

    if (proba == 1):
        response = http.request('GET', pokemon.sprites.front.get('shiny'))
        title_label.config(fg="#FFD700")
        print("shiny")
    else:
        title_label.config(fg="black")
        response = http.request('GET', pokemon.sprites.front.get('default'))
    
    image = PIL.Image.open(BytesIO(response.data))
    img = PIL.ImageTk.PhotoImage(image)
    dictionnaireTypeAndColor = {"normal":"#ADACAC" ,"water":"#66ABE1"  ,"fire":"#F7786B" ,"grass":"#8BD674" ,"electric":"#FFCE4B" ,"ice":"#7ED4C9" ,"fighting":"#D56723" ,"poison":"#C183C1" ,"ground":"#D78555" ,"flying":"#748FC9" ,"psychic":"#FA8581" ,"bug":"#92BC2C" ,"rock":"#CDBD72" ,"ghost":"#7B62A3" ,"dark":"#6F6E78" ,"dragon":"#7383B9" ,"steel":"#5A8EA1" ,"fairy":"#EBA8C3"}
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} {pokemon.name}")
    pokemon_types.config(text=f"{pokemon.types}")
    
    window.config(bg=dictionnaireTypeAndColor[pokemon.types[0]])
    label_id_name.config(bg=dictionnaireTypeAndColor[pokemon.types[0]])
    text_id_name.config(bg=dictionnaireTypeAndColor[pokemon.types[0]])
    btn_load.config(bg=dictionnaireTypeAndColor[pokemon.types[0]])
                     

label_id_name = tk.Label(window, text="ID_or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack (padx=10, pady=10)

text_id_name = tk.Text(window, height=1 , width=20 , bg="black" , fg="white" )
text_id_name.config (font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button (window, text="Load Pokemon" , command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)




window.mainloop()
