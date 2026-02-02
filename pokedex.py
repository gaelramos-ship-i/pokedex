import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Pokedex")
fenetre.geometry("680x480")

class Pokemon:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity


pokemons = [
    Pokemon("Bulbizarre", "Plante, Poison", "Engrais, Chlorophyle"),
    Pokemon("Salameche", "Feu", "Brasier, Force Soleil"),
    Pokemon("Pikachu", "Electrique", "Statik, Paratonnerre")
]


def show_pokemon():
    selection = list_pokemon.curselection()
    if not selection:
        label_info.config(text="Il faut choisir un Pokemon !")
        label_capacity.config(text="")
        return
    
    pokemon = pokemons[selection[0]]
    label_info.config(text=f"{pokemon.name} est un Pokémon de type {pokemon.type}.")
    label_capacity.config(text=f"Capacités : {pokemon.capacity}")
        

def add_pokemon():
    valeur = entry.get()
    if valeur == "":
        label_info.config(text="Il faut écrire une pokemon !")
        label_capacity.config(text="")
    else:
        type_valeur = entry_type.get()
        capacity_valeur = entry_capacity.get()

        new_pokemon = Pokemon(valeur, type_valeur, capacity_valeur)

        list_pokemon.insert(tk.END, new_pokemon.name)

        button.config(text="Ajoute un type")
        
        label_info.config(text=f"{new_pokemon.name}, est un pokemon de type {new_pokemon.type}")

        button.config(text="Ajoute les capacités")

        label_capacity.config(text=f"Capacités : {new_pokemon.capacity}")


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

label_add_pokemon = tk.Label(fenetre, text="Ajoute un pokemon")
label_add_pokemon.pack()

entry = tk.Entry(fenetre)
entry.pack()

label_add_type = tk.Label(fenetre, text="Ajoute le type de pokemon")
label_add_type.pack()

entry_type = tk.Entry(fenetre)
entry_type.pack()

label_add_capacity = tk.Label(fenetre, text="Ajoute les capacités")
label_add_capacity.pack()

entry_capacity = tk.Entry(fenetre)
entry_capacity.pack()

button = tk.Button(fenetre, text="Validé", command=add_pokemon)
button.pack()

fenetre.mainloop()