import tkinter as tk
import string
import random

LONGUEUR_DEFAUT = 10

fenetre = tk.Tk()
fenetre.title("Générateur de mot de passe")
fenetre.geometry("250x100")

def generer(taille=10):
    speciaux = "[](){}*!;/,_-"
    caracteres = string.ascii_letters + string.digits + speciaux
    return ''.join(random.sample(caracteres, taille))

def generer_motdepasse():
    taille = int(entree.get())
    if taille > 0 and taille < 20:
        motdepasse.set(generer(taille))
    else:
        motdepasse.set("La taille est incorrecte")

motdepasse = tk.StringVar(value="Mot de passe")
label_motdepasse = tk.Label(textvariable=motdepasse)

frame = tk.Frame()
label_entree = tk.Label(frame, text="Longueur")
entree = tk.Entry(frame)
entree.insert(0, LONGUEUR_DEFAUT)
bouton = tk.Button(frame, command=generer_motdepasse, text="Générer")

label_motdepasse.pack(pady=20)

label_entree.grid(row=0, column=0)
entree.grid(row=0, column=1, padx=5)
bouton.grid(row=0, column=2)

frame.pack()
fenetre.mainloop()
