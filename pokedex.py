import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Pokedex")
fenetre.geometry("680x480")

class Pokemon:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity

    def show_informations(self):
        print(f"Nom : {self.name}")
        print(f"Type : {self.type}")
        print(f"Capacité : {self.capacity}")

pokemon = Pokemon("Pikachu", "Electrique", "statik")


list_pokemon = tk.Listbox(fenetre)
list_pokemon.pack()

label_info = tk.Label(fenetre, text="Pokemon ?")
label_info.pack()

fenetre.mainloop()