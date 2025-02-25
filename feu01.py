import sys

OPERATEUR_NIVEAU_0 = ["-", "+"]
OPERATEUR_NIVEAU_1 = ["*","/","//","%"]

def evaluer_expression(expression):
    total = 0
    # on split l'entrée
    split_expression = expression.split()

    # on gère les parenthèses
    if "(" and ")" in expression:
        total = gestion_parentheses(expression,total)
       
    else: 
        # on regarde les indices des opérateur présent de niveau 0 et 1
        indice_operateur_niveau_0,indice_operateur_niveau_1 = gestion_indices_operateur(split_expression)
        # on gère l'ordre des opération
        indice_operateur, total =  gestion_operations(split_expression,indice_operateur_niveau_0,indice_operateur_niveau_1,total)
        
        # puis on efface l'opération effectuée
        del split_expression[indice_operateur-1 : indice_operateur+2]
        # pour y mettre le résultat
        split_expression.insert(indice_operateur-1,str(total))

        # on continue tant que la longueur de l'expression est > 1
        if len(split_expression) !=1:
            total = evaluer_expression(" ".join(split_expression))
        else:
            # et sinon on retourne le résultat
            return total
    
    return total 

def gestion_operations(split_expression,indice_operateur_niveau_0,indice_operateur_niveau_1,total):
    # on regarde si le % est le premier dans la liste des indices d'operateur niveau 1
    if "%" in split_expression and split_expression.index("%") == indice_operateur_niveau_1[0]:
        # on cherche l'indice de l'opérateur
        indice_operateur = indice_operateur_niveau_1[0]
        # on fait l'opération
        total += float(split_expression[indice_operateur-1]) % float(split_expression[indice_operateur+1]) 
    
    # on regarde si le * est le premier dans la liste des indices d'operateur niveau 1
    elif "*" in split_expression and split_expression.index("*") == indice_operateur_niveau_1[0]:
        # on cherche l'indice de l'opérateur
        indice_operateur = split_expression.index('*')
        # on fait l'opération
        total += float(split_expression[indice_operateur-1]) * float(split_expression[indice_operateur+1]) 
    
    # on regarde si le / est le premier dans la liste des indices d'operateur niveau 1
    elif "/" in split_expression and split_expression.index("/") == indice_operateur_niveau_1[0]:
        # on cherche l'indice de l'opérateur
        indice_operateur = split_expression.index('/')
        # on fait l'opération
        total += float(split_expression[indice_operateur-1]) / float(split_expression[indice_operateur+1]) 
    
    # on regarde si le + est le premier dans la liste des indices d'operateur niveau 0
    elif "+" in split_expression and split_expression.index("+") == indice_operateur_niveau_0[0]:
        # on cherche l'indice de l'opérateur
        indice_operateur = split_expression.index('+')
        # on fait l'opération
        total += float(split_expression[indice_operateur-1]) + float(split_expression[indice_operateur+1]) 

    # on regarde si le - est le premier dans la liste des indices d'operateur niveau 0
    elif "-" in split_expression and split_expression.index("-") == indice_operateur_niveau_0[0]:
        # on cherche l'indice de l'opérateur
        indice_operateur = split_expression.index('-')
        # on fait l'opération
        total += float(split_expression[indice_operateur-1]) - float(split_expression[indice_operateur+1]) 
    return indice_operateur,total

def gestion_indices_operateur(split_expression):
   
    indice_operateur_niveau_0 = [i for i,operateur in enumerate(split_expression) if operateur in OPERATEUR_NIVEAU_0]
    indice_operateur_niveau_1 = [i for i,operateur in enumerate(split_expression) if operateur in OPERATEUR_NIVEAU_1]
    return indice_operateur_niveau_0 , indice_operateur_niveau_1


def gestion_parentheses(expression,total):
     # mais où sont elles ?
    indice_parentheses_ouvertes, indice_parentheses_fermees  = indices_parentheses(expression)
    # on prend celles les plus à l'intèrieur
    indice_parenthese_ouverte = indice_parentheses_ouvertes[-1]
    indice_parenthese_fermee = indice_parentheses_fermees[0]
    # on récupère l'expression entre parenthèses
    expression_entre_parenthèse = expression[indice_parenthese_ouverte+1:indice_parenthese_fermee] 
    # et on l'envoie dans la fonction evaluer_expression
    total += evaluer_expression(expression_entre_parenthèse)
    # on remplace les parenthèse par le total calculé
    expression = expression[:indice_parenthese_ouverte] + str(total) + expression[indice_parenthese_fermee+1:]
    # puis on renvoie dans la fonction tant que expression existe
    total = evaluer_expression(expression)
    return total


def indices_parentheses(expression):
    ouvertes = [i for i, parenthese_ouverte in enumerate(expression) if parenthese_ouverte == '(']
    fermees = [i for i, parenthese_fermee in enumerate(expression) if parenthese_fermee == ')']
    return ouvertes, fermees


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
        #print(resultat,resultat_eval)
        if resultat == resultat_eval:
            afficher(resultat)
        else:
            erreur()  
    else:
        erreur()