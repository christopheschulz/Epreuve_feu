import sys

OPERATEUR_NIVEAU_0 = ["-", "+"]
OPERATEUR_NIVEAU_1 = ["*", "/", "//", "%"]

def evaluer_expression(expression):
    # Gérer les parenthèses récursivement
    while "(" in expression:
        expression = evaluer_parentheses(expression)
    
    # Évaluation sans parenthèses
    split_expression = decouper_expression(expression)
    while len(split_expression) > 1:
        # Gérer les opérations de niveau 1 en priorité
        split_expression = gerer_operations(split_expression, OPERATEUR_NIVEAU_1)
        split_expression = gerer_operations(split_expression, OPERATEUR_NIVEAU_0)
    
    return float(split_expression[0])

def decouper_expression(expression):
    # Ajouter des espaces autour des opérateurs pour un découpage plus précis
    for op in OPERATEUR_NIVEAU_0 + OPERATEUR_NIVEAU_1:
        expression = expression.replace(op, f' {op} ')
    return expression.split()

def evaluer_parentheses(expression):
    ouvertes, fermees = indices_parentheses(expression)
    derniere_ouverte = ouvertes[-1]
    premiere_fermee = next(f for f in fermees if f > derniere_ouverte)
    
    # Évaluer l'expression à l'intérieur des parenthèses
    sous_expression = expression[derniere_ouverte + 1 : premiere_fermee]
    resultat = evaluer_expression(sous_expression)
    
    # Remplacer l'expression entre parenthèses par le résultat
    nouvelle_expression = (
        expression[:derniere_ouverte] + str(resultat) + expression[premiere_fermee + 1:]
    )
    return nouvelle_expression

def gerer_operations(expression, operateurs):
    i = 0
    while i < len(expression):
        if expression[i] in operateurs:
            gauche = float(expression[i - 1])
            droite = float(expression[i + 1])
            resultat = effectuer_operation(gauche, droite, expression[i])
            expression = expression[:i - 1] + [str(resultat)] + expression[i + 2:]
            i = 0  # Recommencer la vérification après modification
        else:
            i += 1
    return expression

def effectuer_operation(a, b, operateur):
    if operateur == "+":
        return a + b
    elif operateur == "-":
        return a - b
    elif operateur == "*":
        return a * b
    elif operateur == "/":
        if b == 0:
            raise ValueError("Division par zéro.")
        return a / b
    elif operateur == "//":
        return a // b
    elif operateur == "%":
        return a % b

def indices_parentheses(expression):
    ouvertes = [i for i, c in enumerate(expression) if c == '(']
    fermees = [i for i, c in enumerate(expression) if c == ')']
    return ouvertes, fermees

def afficher(resultat):
    if resultat == int(resultat):
        print(int(resultat))
    else:
        print(f"{resultat:.2f}")


def main():
    arguments = sys.argv[1:]
    
    expression = arguments[0]
    try:
        resultat = evaluer_expression(expression)
        resultat_eval = eval(expression)
        if resultat == resultat_eval:
            afficher(resultat)
        else:
            print("Le résultat n'est pas correcte")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
    
   
