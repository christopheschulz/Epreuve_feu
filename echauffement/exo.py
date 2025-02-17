import sys


def afficher_rectangle(line,columns):
    line = int(line)
    columns = int(columns)
    charactère = ""
    # afficher colonne
    for i in range(columns):
        # afficher ligne
        for j in range(line):
            # si début et fin de rectangle on dessine avec o et -
            if i == 0 or i == columns-1:
                # si début et fin de ligne on dessine avec o 
                if j == 0 or j == line-1:
                    charactère = "o"
                # sinon on dessine avec -
                else:
                    charactère = "-"
                print(charactère,end="")
            # sinon on dessine avec | et espace
            else:
                # si début et fin de ligne on dessine avec |
                if j == 0 or j == line-1:
                    charactère = "|"
                # sinon on dessine avec un espace
                else:
                    charactère = " "
                print(charactère,end="")
        print()
        


def verification_arguments(arguments):
    ok = False
    if len(arguments) == 2 and "0" not in arguments:
        if arguments[0].isdigit() and arguments[1].isdigit() == 1:
            ok = True
    return ok


def afficher(chaine):
   pass


def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
       line = arguments[0]
       columns = arguments[1]
       afficher_rectangle(line,columns)
        
    else:
        erreur()