import sys

OPERATORS_LEVEL_0 = ["-", "+"]
OPERATORS_LEVEL_1 = ["*", "/", "//", "%"]
OPERATORS = OPERATORS_LEVEL_1 + OPERATORS_LEVEL_0

def expression_evaluation(expression):
    # Gérer les parenthèses récursivement
    while "(" in expression:
        expression = evaluation_of_the_expression_between_brackets(expression)
    
    # Évaluation sans parenthèses
    
    split_expression = splitting_expression(expression)
    while len(split_expression) > 1:
        # Gérer les opérations de niveau 1 en priorité
        
        split_expression = manage_operations(split_expression, OPERATORS_LEVEL_1)
        
        split_expression = manage_operations(split_expression, OPERATORS_LEVEL_0)
    
    return float(split_expression[0])


def splitting_expression(expression):
    # Ajouter des espaces autour des opérateurs pour un découpage plus précis
    for op in OPERATORS:
        expression = expression.replace(op, f' {op} ')
    return expression.split()


def evaluation_of_the_expression_between_brackets(expression):
    opened = [i for i, char in enumerate(expression) if char == '(']
    closed = [i for i, char in enumerate(expression) if char == ')']
    last_opened = opened[-1]
    first_opened = next(f for f in closed if f > last_opened)
    
    # Évaluer l'expression à l'intérieur des parenthèses
    brackets_expression = expression[last_opened + 1 : first_opened]
    result = expression_evaluation(brackets_expression)
    
    # Remplacer l'expression entre parenthèses par le résultat
    new_expression = (
        expression[:last_opened] + str(result) + expression[first_opened + 1:]
    )
    return new_expression


def manage_operations(expression, operators):
    i = 0
    while i < len(expression):
        if expression[i] in operators:
            gauche = float(expression[i - 1])
            droite = float(expression[i + 1])
            resultat = perform_operation(gauche, droite, expression[i])
            expression = expression[:i - 1] + [str(resultat)] + expression[i + 2:]
            i = 0  # Recommencer la vérification après modification
        else:
            i += 1
       
    return expression


def perform_operation(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ValueError("Division par zéro.")
        return a / b
    elif operator == "//":
        return a // b
    elif operator == "%":
        return a % b


def display(result):
    if result == int(result):
        print(int(result))
        return
    
    print(f"{result:.2f}")


def get_arguments():
    arguments = sys.argv[1:]
    return arguments


def result_is_valid(result,result_eval):
    if result != result_eval:
        print("Le résultat n'est pas correcte")
        print(f"il est de {result} et doit être de {result_eval}")
        return False
    return True


def evaluating_an_expression():
    arguments = get_arguments()
    expression = arguments[0]
    
    result = expression_evaluation(expression)
    result_eval = eval(expression)
    
    if result_is_valid(result,result_eval):
        display(result)
    
   
evaluating_an_expression()
    
   
