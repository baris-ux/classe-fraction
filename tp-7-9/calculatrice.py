import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma fenêtre Tkinter")
fenetre.geometry("400x400")
fenetre.configure(bg="lightblue")

def on_click():
    text1_content = text1.get("1.0", tk.END).strip()  # Enlever les espaces superflus
    text2_content = text2.get("1.0", tk.END).strip()

    try:
        number1 = int(text1_content)
        number2 = int(text2_content)

        # Effectuer l'opération en fonction de la sélection
        if operation.get() == "Addition":
            result = f"Addition: {number1 + number2}"
        elif operation.get() == "Soustraction":
            result = f"Soustraction: {number1 - number2}"
        elif operation.get() == "Multiplication":
            result = f"Multiplication: {number1 * number2}"
        elif operation.get() == "Division":
            if number2 != 0:
                result = f"Division: {number1 / number2}"
            else:
                result = "Division par zéro impossible."
        else:
            result = "Aucune opération sélectionnée."

        label.config(text=result)

    except ValueError:
        label.config(text="Veuillez entrer des nombres valides s'il vous plaît")

# Partie supérieure
upper_frame = tk.Frame(fenetre)
upper_frame.pack(pady=20, padx=10, fill=tk.X)

# Partie inférieure
bottom_frame = tk.Frame(fenetre)
bottom_frame.pack(side=tk.BOTTOM, pady=20, padx=10, fill=tk.X)

# Ajouter les deux zones de texte
text1 = tk.Text(upper_frame, height=5, width=40, font=("Arial", 12))
text1.pack(side=tk.LEFT, padx=10, pady=5)

text2 = tk.Text(upper_frame, height=5, width=40, font=("Arial", 12))
text2.pack(side=tk.LEFT, padx=10, pady=5)

# Bouton pour effectuer l'opération
bouton = tk.Button(upper_frame, text="Cliquez ici", command=on_click, font=("Arial", 12))
bouton.pack(side=tk.LEFT, pady=10)

# Définir une variable pour l'opération choisie
operation = tk.StringVar()
operation.set(None)  # Aucun choix par défaut

# Création des Radiobuttons pour chaque opération
radiobutton_addition = tk.Radiobutton(upper_frame, text="Additionner", variable=operation, value="Addition", font=("Arial", 12))
radiobutton_addition.pack(side=tk.LEFT, padx=10)

radiobutton_soustraction = tk.Radiobutton(upper_frame, text="Soustraire", variable=operation, value="Soustraction", font=("Arial", 12))
radiobutton_soustraction.pack(side=tk.LEFT, padx=10)

radiobutton_multiplication = tk.Radiobutton(upper_frame, text="Multiplier", variable=operation, value="Multiplication", font=("Arial", 12))
radiobutton_multiplication.pack(side=tk.LEFT, padx=10)

radiobutton_division = tk.Radiobutton(upper_frame, text="Diviser", variable=operation, value="Division", font=("Arial", 12))
radiobutton_division.pack(side=tk.LEFT, padx=10)

# Label pour afficher le résultat
label = tk.Label(bottom_frame, text="Résultat affiché ici", font=("Arial", 14))
label.pack()

fenetre.mainloop()
