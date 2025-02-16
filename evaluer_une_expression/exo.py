import sys
# operation prioritaire PEMDAS:

# Parenthèses
# Exposant
# Multiplication
# Division
# Addition
# Soustraction

def essai_evaluer_expression(expression,total=0):
    # on split l'entrée
    split_expression = expression.split()

    # on met les opération dans l'ordre de priorité
    if expression:
        if "(" and ")" in expression:
            indice_parenthese_ouverte = expression.index('(')
            indice_parenthese_fermee = expression.index(')')
            total = evaluer_expression(expression[indice_parenthese_ouverte+1:indice_parenthese_fermee],total)
        
        # on gère la multiplication
        elif "*" in expression:
            # on cherche l'indice de l'opérateur
            indice_operateur = split_expression.index('*')
            # on fait l'opération
            total += int(split_expression[indice_operateur-1]) * int(split_expression[indice_operateur+1]) 
            
        elif "/" in expression:
            # on cherche l'indice de l'opérateur
            indice_operateur = split_expression.index('/')
            # on fait l'opération
            total += int(split_expression[indice_operateur-1]) / int(split_expression[indice_operateur+1]) 
        
        elif "+" in expression:
            # on cherche l'indice de l'opérateur
            indice_operateur = split_expression.index('+')
            # on fait l'opération
            total += int(split_expression[indice_operateur-1]) + int(split_expression[indice_operateur+1]) 
         
        elif "-" in expression:
            # on cherche l'indice de l'opérateur
            indice_operateur = split_expression.index('-')
            # on fait l'opération
            total += int(split_expression[indice_operateur-1]) - int(split_expression[indice_operateur+1]) 


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


def evaluer_expression(expression,total=0):
    # on met les opération dans l'ordre de priorité
    if expression:
        if "(" and ")" in expression:
            indice_parenthese_ouverte = expression.index('(')
            indice_parenthese_fermee = expression.index(')')
            total = evaluer_expression(expression[indice_parenthese_ouverte+1:indice_parenthese_fermee],total)
        
        # on gère la multiplication
        elif "*" in expression:
            # on split l'entrée
            split_expression = expression.split()
            # afin de pouvoir chercher l'indice de l'opérateur
            indice_multiplication = split_expression.index('*')
            # on fait l'opération
            total += int(split_expression[indice_multiplication-1]) * int(split_expression[indice_multiplication+1]) 
            # puis on efface l'opération effectuée
            del split_expression[indice_multiplication-1 : indice_multiplication+2]
            # pour y mettre le résultat
            split_expression.insert(indice_multiplication-1,str(total))

            #print(split_expression)
            # on continue tant que la longueur de l'expression est > 1
            if len(split_expression) !=1:
                total = evaluer_expression(" ".join(split_expression))
                #print(total)
            else:
                # et sinon on retourne le résultat
                return total
            #print(total)

        elif "/" in expression:
            
            split_expression = expression.split()
            indice_division = split_expression.index('/')
            
            total += int(split_expression[indice_division-1]) / int(split_expression[indice_division+1]) 
            
            del split_expression[indice_division-1 : indice_division+2]

            split_expression.insert(indice_division-1,str(total))

            #print(split_expression)
            if len(split_expression) !=1:
                total = evaluer_expression(" ".join(split_expression))
                #print(total)
            else:
                return total
            #print(total)

        elif "+" in expression:
            
            split_expression = expression.split()
            #print("split",split_expression)
            indice_addition = split_expression.index('+')
            #print("indice",indice_addition)
        
            total += int(split_expression[indice_addition-1]) + int(split_expression[indice_addition+1]) 
            #print("total",total)

            del split_expression[indice_addition-1 : indice_addition+2]

            split_expression.insert(indice_addition-1,str(total))

            #print("split",split_expression)
            if len(split_expression) !=1:
                total = evaluer_expression(" ".join(split_expression))
                #print(total)
            else:
                return total

        elif "-" in expression:
            
            split_expression = expression.split()
            #print(split_expression)
            indice_soustraction = split_expression.index('-')
            #print(indice_soustraction)

            total += int(split_expression[indice_soustraction-1]) - int(split_expression[indice_soustraction+1]) 
            
            del split_expression[indice_soustraction-1 : indice_soustraction+2]

            split_expression.insert(indice_soustraction-1,str(total))

            #print(split_expression)
            if len(split_expression) !=1:
                total = evaluer_expression(" ".join(split_expression))
                #print(total)
            else:
                return total
            #print(total)

    return total      
    
        


def verification_arguments(arguments):
    ok = True
    
    return ok


def afficher(chaine):
   print(chaine)


def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        resultat = essai_evaluer_expression(arguments[0])
        resultat_eval = eval(arguments[0])
        if resultat == resultat_eval:
            afficher(resultat)
        else:
            erreur()
        
        
    else:
        erreur()