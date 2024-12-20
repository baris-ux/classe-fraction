import tkinter as tk

def changer_couleur(event, label):
    if label.cget("bg") == "white":
        label.config(bg="blue")
    else:
        label.config(bg="white")

fenetre = tk.Tk()
fenetre.title("Fenêtre Grille 5x5")
fenetre.geometry("500x500")
fenetre.config(bg="lightblue")

for i in range(5):
    fenetre.grid_columnconfigure(i, weight=1, uniform="equal")
    fenetre.grid_rowconfigure(i, weight=1, uniform="equal")

for i in range(5):
    for j in range(5):
        label = tk.Label(fenetre, relief="solid", bg="white")
        label.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
        label.bind("<Button-1>", lambda event, label=label: changer_couleur(event, label))

fenetre.mainloop()
