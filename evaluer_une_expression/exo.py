import sys
# operation prioritaire PEMDAS:

# Parenthèses
# Exposant
# Multiplication
# Division
# Addition
# Soustraction

def evaluer_expression(expression,total=0):
    # on split l'entrée
    split_expression = expression.split()
    # on met les opération dans l'ordre de priorité
    
    # on gère les parenthèses
    if "(" and ")" in expression:
        # mais où sont elles ?
        indice_parenthese_ouverte = expression.index('(')
        indice_parenthese_fermee = expression.index(')')
        # on récupère l'expression entre parenthèses
        expression_entre_parenthèse = expression[indice_parenthese_ouverte+1:indice_parenthese_fermee] 
        # print(expression_entre_parenthèse)
        # et on l'envoie dan le fonction
        total += evaluer_expression(expression_entre_parenthèse)
        # on remplace les parenthèse par le total calculé
        expression = expression[:indice_parenthese_ouverte] + str(total) + expression[indice_parenthese_fermee+1:]
        # puis on renvoie dans la fonction
        total = evaluer_expression(expression)

    else:
        # on gère le modulo
        if "%" in expression:
            # on cherche l'indice de l'opérateur
            indice_operateur = split_expression.index('%')
            # on fait l'opération
            total += float(split_expression[indice_operateur-1]) % float(split_expression[indice_operateur+1]) 
        
        # on gère la multiplication
        elif "*" in expression:
            # on cherche l'indice de l'opérateur
            indice_operateur = split_expression.index('*')
            # on fait l'opération
            total += float(split_expression[indice_operateur-1]) * float(split_expression[indice_operateur+1]) 
        
        # on gère la division    
        elif "/" in expression:
            # on cherche l'indice de l'opérateur
            indice_operateur = split_expression.index('/')
            # on fait l'opération
            total += float(split_expression[indice_operateur-1]) / float(split_expression[indice_operateur+1]) 
        
        # on gère l'addition
        elif "+" in expression:
            # on cherche l'indice de l'opérateur
            indice_operateur = split_expression.index('+')
            # on fait l'opération
            total += float(split_expression[indice_operateur-1]) + float(split_expression[indice_operateur+1]) 

        # on gère la soustraction 
        elif "-" in expression:
            # on cherche l'indice de l'opérateur
            indice_operateur = split_expression.index('-')
            # on fait l'opération
            total += float(split_expression[indice_operateur-1]) - float(split_expression[indice_operateur+1]) 

        # puis on efface l'opération effectuée
        del split_expression[indice_operateur-1 : indice_operateur+2]
        # pour y mettre le résultat
        split_expression.insert(indice_operateur-1,str(total))

        #print(split_expression)
        # on continue tant que la longueur de l'expression est > 1
        if len(split_expression) !=1:
            total = evaluer_expression(" ".join(split_expression))
            #print(total)
        else:
            # et sinon on retourne le résultat
            return total
        #print(total)
    
    return total      

def verification_arguments(arguments):
    ok = True
    
    return ok


def afficher(chaine):
    if chaine == int(chaine):
        print(int(chaine))
    else:
        print(f"{chaine:.2f}")


def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        resultat = evaluer_expression(arguments[0])
        # on utilise la fonction eval pour vérifier si c'est juste
        resultat_eval = eval(arguments[0])
        # si c'est juste on affiche sinon erreur
        if resultat == resultat_eval:
            afficher(resultat)
        else:
            erreur()  
    else:
        erreur()