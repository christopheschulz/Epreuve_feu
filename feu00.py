import sys


def display_rectangle(rows,columns):
    char = ""
    for i in range(columns):
        for j in range(rows):
            if i == 0 or i == columns-1:
                display_start_end_rows(j,rows)
            else:
                display_intermediate_row(j,rows)
        print()


def display_start_end_rows(j,rows):
    
    if j == 0 or j == rows-1:
        char = "o"
    else:
        char = "-"
    print(char,end="")


def display_intermediate_row(j,rows):
     # si début et fin de ligne on dessine avec |
    if j == 0 or j == rows-1:
        char = "|"
    # sinon on dessine avec un espace
    else:
        char = " "
    print(char,end="")


def get_arguments():
    arguments = sys.argv[1:]
    return arguments
    
    
def len_arguments_is_valid(arguments,lenght):
    return len(arguments) == lenght


def has_zero_in_argument(argument):
    return argument == 0


def is_digit(argument):
    return argument.isdigit()
        

def has_error(arguments):
    arguments_lenght = 2
    if not len_arguments_is_valid(arguments,arguments_lenght):
        print(f"Le nombre d'agument doit être de {arguments_lenght}")
        return True
    for argument in arguments:
        if not is_digit(argument):
            print("l'argument n'est pas un digit")
            return True
        if has_zero_in_argument(int(argument)):
            print("erreur 0 dans argument")
            return True
    return False


def warm_up():
    arguments = get_arguments()
    if not has_error(arguments):
        rows = int(arguments[0])
        columns = int(arguments[1])
        display_rectangle(rows,columns)


warm_up()