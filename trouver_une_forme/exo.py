import sys


def trouver_une_forme(line,columns):
    pass
        


def verification_arguments(arguments):
    ok = False
    if len(arguments) == 2:
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
      pass
        
    else:
        erreur()