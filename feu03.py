import sys
from pathlib import Path


def sudoku_resolve(sudoku):
    # on cherche une case vide
    case = find_empty_box(sudoku)
    
    # si plus de case vide alors c'est gagné
    if not case:
        return True  
    
    # coordonnées de la case vide
    line, col = case

    for num in range(1, 10):  
        if is_valid(sudoku, line, col, num):
            # notre fichier sudoku est une chaine de caractère d'où le str()
            sudoku[line][col] = str(num)  

            if sudoku_resolve(sudoku):  
                return True
            # on remet un point si c'est pas la solution
            sudoku[line][col] = "." 

    return False  


def find_empty_box(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == ".":
                return i, j 
    return None  


def is_valid(sudoku, line, col, num):
    # Vérifier la ligne
    # notre fichier sudoku est une chaine de caractère d'où le str()
    if str(num) in sudoku[line]:
        return False
    
    # Vérifier la colonne
    # notre fichier sudoku est une chaine de caractère d'où le str()
    if str(num) in [sudoku[i][col] for i in range(9)]:
        return False
    
    # Vérifier le carré 3x3
    start_line, start_col = (line // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            # notre fichier sudoku est une chaine de caractère d'où le str()
            if sudoku[start_line + i][start_col + j] == str(num):
                return False
    
    return True


def load_file(file_name):
    path_ = Path.cwd()
    fichier = path_ / file_name
    try:
        with open(fichier, "r", encoding="utf-8") as fichier:
            # On met le fichier en liste par ligne seulement si la ligne n'est pas vide
            resultat = [list(ligne.rstrip("\n")) for ligne in fichier if ligne]

        return resultat
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier.name} n'existe pas.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return []
    
   
def len_arguments_is_valid(arguments,lenght):
    return len(arguments) == lenght


def has_arguments_end_with(argument,suffix):
    return argument.endswith(suffix)


def has_arguments_error(arguments):
    arguments_lenght = 1
    suffix = "txt"
    if not len_arguments_is_valid(arguments,arguments_lenght):
        print(f"Le nombre d'agument doit être de {arguments_lenght}")
        return True
    for argument in arguments:
        if not has_arguments_end_with(argument,suffix):
            print(f"Le nom de fichier ne termine pas pas {suffix}")
            return True
    return False


def display(result):
   
    for i in range(9):
        for j in range(9):
            print(result[i][j],end="")
        print()


def board_is_not_ok(sudoku):
    if not sudoku:
        return True
    
    lenght_sudoku_ok = len(sudoku) == 9 and all(len(i)==9 for i in sudoku)
    if not lenght_sudoku_ok:
        return True
    
    return False


def get_arguments():
    arguments = sys.argv[1:]
    return arguments


def sudoku():
    arguments = get_arguments()

    if has_arguments_error(arguments):
        return

    sudoku = load_file(arguments[0])
    
    if board_is_not_ok(sudoku):
        return
    
    result = sudoku_resolve(sudoku)
    if result:
        display(sudoku)  
    

sudoku()