import string
import random


def generer(taille=10):
    speciaux = "[](){}*!;/,_-"
    caractere = string.ascii_letters + string.digits + speciaux
    return ''.join(random.sample(caractere, taille))

mot_de_passe = generer()
print(mot_de_passe)
