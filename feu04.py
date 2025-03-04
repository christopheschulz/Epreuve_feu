import sys
from pathlib import Path


def find_greatest_square(board):

    len_board = len(board)
    len_line_board = len(board[0])
    # declarer la matrice de carré
    square_matrix = [[0]*len_line_board for _ in range(len_board)]
    max_square_size = 0
    
    for i in range(len_board):
        for j in range(len_line_board):
            if board[i][j] == ".":
                if i == 0 and j == 0:
                    square_matrix[i][j] = 0
                else: # on vérifie les valeurs dans les cases juste avant , en diagonale avant ,  juste audessus                               
                    square_matrix[i][j] = min(square_matrix[i][j-1],square_matrix[i-1][j-1],square_matrix[i-1][j]) + 1
            if square_matrix[i][j] > max_square_size:
                max_square_size = square_matrix[i][j]
                x,y = (i - max_square_size ) + 1 , (j - max_square_size ) + 1
    
    return x,y,max_square_size


def load_file(file_name):
    path_ = Path.cwd()
    fichier = path_ / file_name
    try:
        with open(fichier, "r", encoding="utf-8") as fichier:
            # On met le fichier en liste par ligne seulement si la ligne n'est pas vide
            first_line = fichier.readline().rstrip("\n")
            board = [list(ligne.rstrip("\n")) for ligne in fichier]
            #afficher(first_line,resultat)

        return first_line,board
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier.name} n'existe pas.")
        return [],[]
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return [],[]
    

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


def board_is_not_valid(title ,board):
    if not board or not title:
        return True

    len_line_board = [len(ligne) for ligne in board]
    if len(set(len_line_board)) != 1:
        return True
    
    allowed_charachter = set(title[-3:])
    for ligne in board:
        for caractere in ligne:
            if caractere not in allowed_charachter:
                return True
    
    return False


def display(first_line,board,square):
    len_board = len(board)
    len_line_board = len(board[0])
    
    x, y, square_size = square

    print(first_line)
    for i in range(len_board):
        for j in range(len_line_board):
            if x <= i < x + square_size and y <= j < y + square_size:
                print("o",end="")
            else: 
                print(board[i][j],end="")
        print()


def get_arguments():
    arguments = sys.argv[1:]
    return arguments


def greatest_square():
    arguments = get_arguments()

    if has_arguments_error(arguments):
        return
    
    title, board = load_file(arguments[0])
        
    if  board_is_not_valid(title,board):
        return
        
    result = find_greatest_square(board)
    display(title,board,result)


greatest_square()