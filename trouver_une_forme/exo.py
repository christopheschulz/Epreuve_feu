import sys

from pprint import pprint
from pathlib import Path


chemin = Path.cwd()


def trouver_une_forme(board,to_find):
  
    
    return False





def charger_fichier(nom_fichier):
    fichier = chemin / nom_fichier
    try:
        with open(fichier, "r", encoding="utf-8") as fichier:
            resultat = [list(ligne.rstrip("\n")) for ligne in fichier]
        return resultat
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier.name} n'existe pas.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return []

   
def verification_arguments(arguments):
    ok = False
    if len(arguments) == 2:
        if arguments[0].endswith("txt") and arguments[1].endswith("txt"):
            ok = True
    return ok


def afficher(chaine):
   pass


def erreur():
    print("error")


def main():
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        board = charger_fichier(arguments[0])
        to_find = charger_fichier(arguments[1])
        if board and to_find:
            resultat = trouver_une_forme(board,to_find)
            print(resultat)
        else:
            erreur()   
    else:
        erreur()


if __name__ == "__main__":
    main()