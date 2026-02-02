import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Pokedex")
fenetre.geometry("680x480")

class Pokemon:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity

pokemon1 = Pokemon("Bulbizarre", "Plante, Poison", "Engrais, Chlorophyle")
pokemon2 = Pokemon("Salameche", "Feu", "Brasier, Force Soleil")
pokemon3 = Pokemon("Pikachu", "Electrique", "Statik, Paratonnerre")

def show_pokemon():
    selection = list_pokemon.curselection()
    if selection:
        if selection[0] == 0:
            label_info.config(text=f"{pokemon1.name} est un pokemon de type {pokemon1.type},")
            label_capacity.config(text=f"Capacités : {pokemon1.capacity}")

        if selection[0] == 1:
            label_info.config(text=f"{pokemon2.name} est un pokemon de type {pokemon2.type},")
            label_capacity.config(text=f"Capacités : {pokemon2.capacity}")

        if selection[0] == 2:
            label_info.config(text=f"{pokemon3.name} est un pokemon de type {pokemon3.type},")
            label_capacity.config(text=f"Capacités : {pokemon3.capacity}")
    else:
        label_info.config(text="Il faut choisir un Pokemon !")

list_pokemon = tk.Listbox(fenetre)
list_pokemon.pack()

list_pokemon.insert(tk.END, "Bulbizarre")
list_pokemon.insert(tk.END, "Salameche")
list_pokemon.insert(tk.END, "Pikachu")

button = tk.Button(fenetre, text="Affiche le pokemon", command=show_pokemon)
button.pack()

label_info = tk.Label(fenetre, text="Pokemon ?")
label_info.pack()

label_capacity = tk.Label(fenetre, text="")
label_capacity.pack()

fenetre.mainloop()