import tkinter as tk
from PIL import ImageTk, Image

fenetre = tk.Tk()
fenetre.title("Pokedex")
fenetre.geometry("680x480")

class Pokemon:
    def __init__(self, name, type, capacity, image):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.img = image


pokemons = [
    Pokemon("Bulbizarre", "Plante, Poison", "Engrais / Chlorophyle", "img/bulbizarre.png"),
    Pokemon("Salameche", "Feu", "Brasier / Force Soleil", "img/salameche.png"),
    Pokemon("Pikachu", "Electrique", "Statik / Paratonnerre", "img/pikachu.png")
]


def show_pokemon():
    global image
    selection = list_pokemon.curselection()

    # Si aucun pokemon selectionné
    if not selection:
        label_info.config(text="Il faut choisir un Pokemon !")
        label_capacity.config(text="")
        return
    
    # Affiche les informations du pokemon selectionné
    pokemon = pokemons[selection[0]]
    label_info.config(text=f"{pokemon.name} est un Pokémon de type {pokemon.type}.")
    label_capacity.config(text=f"Capacités : {pokemon.capacity}")

    image = ImageTk.PhotoImage(Image.open(pokemon.img).resize((200, 200)))
    label_img.config(image=image) 


def add_pokemon():
    #Recupere le nom entre par l'utilisateur
    name_valeur = entry_name.get() 

    # verifie si le nom est vide
    if not name_valeur:
        label_info.config(text="Il faut écrire une pokemon !")
        label_capacity.config(text="")
        return
    
    # Recupere type et capacite
    type_valeur = entry_type.get()
    capacity_valeur = entry_capacity.get()

    # Nouveau pokemon 
    new_pokemon = Pokemon(name_valeur, type_valeur, capacity_valeur, image=f"img/{name_valeur.lower()}.png")
    pokemons.append(new_pokemon)

    # infos pour utilisateur
    label_info.config(text=f"{new_pokemon.name} a été ajouté au pokedex,")
    label_capacity.config(text="")
    label_img.config(image="")

    # Ajouter a la liste le nouveau pokemon
    list_pokemon.insert(tk.END, new_pokemon.name)

    # Efface le contenu entry apres utilisation
    entry_name.delete(0, tk.END)
    entry_type.delete(0, tk.END)
    entry_capacity.delete(0, tk.END)

    # Enregister pokemon
    save_pokemon = open(f"save_pokemon.txt", "a", encoding="UTF-8")
    save_pokemon.write(f"{new_pokemon.name},{new_pokemon.type},{new_pokemon.capacity},{new_pokemon.img} \n")
    save_pokemon.close

def load_pokemon():
    with open("save_pokemon.txt", "r", encoding="UTF-8") as file:
        for line in file:
            name, type, capacity, img = line.split(",")
            pokemon = Pokemon(name, type, capacity, img)
            pokemons.append(pokemon)
            list_pokemon.insert(tk.END, name)
                        

# Création d'une listbox pour lister les pokemons
list_pokemon = tk.Listbox(fenetre, width=50)
list_pokemon.place(x=50, y=50)

list_pokemon.insert(tk.END, "Bulbizarre")
list_pokemon.insert(tk.END, "Salameche")
list_pokemon.insert(tk.END, "Pikachu")

# Chargement des pokemons enregistrés
load_pokemon()

# Création d'un button pour afficher les pokemons
button = tk.Button(fenetre, text="Affiche le pokemon", command=show_pokemon)
button.place(x=50, y=230)

# Label qui indique le nom et le type de pokemon
label_info = tk.Label(fenetre, text="Pokemon ?")
label_info.place(x=50, y=270)

# Label qui indique les capacités du pokemon
label_capacity = tk.Label(fenetre)
label_capacity.place(x=50, y=300)

# Label: support pour afficher l'image
label_img = tk.Label(fenetre)
label_img.place(x=400, y=50)

# Label qui informe l'utilisateur sur ce qu'il doit faire
label_add_pokemon = tk.Label(fenetre, text="Ajoute un pokemon")
label_add_pokemon.place(x=400, y=300)

entry_name = tk.Entry(fenetre)
entry_name.place(x=400, y=320)

# Label qui informe l'utilisateur sur ce qu'il doit faire
label_add_type = tk.Label(fenetre, text="Ajoute le type de pokemon")
label_add_type.place(x=400, y=340)

entry_type = tk.Entry(fenetre)
entry_type.place(x=400, y=360)

# Label qui informe l'utilisateur sur ce qu'il doit faire
label_add_capacity = tk.Label(fenetre, text="Ajoute les capacités")
label_add_capacity.place(x=400, y=380)

entry_capacity = tk.Entry(fenetre)
entry_capacity.place(x=400, y=400)

# Ajouter un pokemon
button = tk.Button(fenetre, text="Validé", command=add_pokemon)
button.place(x=400, y=430)

fenetre.mainloop()

#https://github.com/gaelramos-ship-i/pokedex