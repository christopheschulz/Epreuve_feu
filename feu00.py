import sys


def afficher_rectangle(line,columns):
    line = int(line)
    columns = int(columns)
    char = ""
    # afficher colonne
    for i in range(columns):
        # afficher ligne
        for j in range(line):
            # si début et fin de rectangle on dessine avec o et -
            if i == 0 or i == columns-1:
                # si début et fin de ligne on dessine avec o 
                if j == 0 or j == line-1:
                    char = "o"
                # sinon on dessine avec -
                else:
                    char = "-"
                print(char,end="")
            # sinon on dessine avec | et espace
            else:
                # si début et fin de ligne on dessine avec |
                if j == 0 or j == line-1:
                    char = "|"
                # sinon on dessine avec un espace
                else:
                    char = " "
                print(char,end="")
        print()
        

def main():
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
       line = arguments[0]
       columns = arguments[1]
       afficher_rectangle(line,columns)
    

def args_are_valid(arguments):

    if len(arguments) != 2:
        print("Deux arguments sont attendus (ligne,colonne) !")
        return False
    if "0" in arguments:
        print("Aucun zéro ne doit être présent dans vos arguments !")
        return False
    if not all(argument.isdigit() for argument in arguments):
        print("Tous vos arguments doivent être des chiffres !")
        return False
        
    return True


if __name__ == "__main__":
    main()