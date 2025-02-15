import sys
# operation prioritaire PEMDAS:

# Parenthèses
# Exposant
# Multiplication
# Division
# Addition
# Soustraction

def evaluer_expression(expression,total=0):
    
    if expression:
        if "(" and ")" in expression:
            indice_parenthese_ouverte = expression.index('(')
            indice_parenthese_fermee = expression.index(')')
            total = evaluer_expression(expression[indice_parenthese_ouverte+1:indice_parenthese_fermee],total)
        
        elif "*" in expression:

            split_expression = expression.split()
            indice_multiplication = split_expression.index('*')
           
            total += int(split_expression[indice_multiplication-1]) * int(split_expression[indice_multiplication+1]) 
            split_expression.remove(split_expression[indice_multiplication-1])
            split_expression.remove(split_expression[indice_multiplication-1])
            split_expression.remove(split_expression[indice_multiplication-1])

            split_expression.insert(indice_multiplication-1,str(total))

            print(split_expression)
            if len(split_expression) !=1:
                total = evaluer_expression(" ".join(split_expression))
                print(total)
            else:
                return total
            print(total)

        elif "/" in expression:
            
            split_expression = expression.split()
            indice_division = split_expression.index('/')
            
            total += int(split_expression[indice_division-1]) / int(split_expression[indice_division+1]) 
            
            split_expression.remove(split_expression[indice_division-1])
            split_expression.remove(split_expression[indice_division-1])
            split_expression.remove(split_expression[indice_division-1])

            split_expression.insert(indice_division-1,str(total))

            print(split_expression)
            if len(split_expression) !=1:
                total = evaluer_expression(" ".join(split_expression))
                print(total)
            else:
                return total
            print(total)

        elif "+" in expression:
            
            split_expression = expression.split()
            print("split",split_expression)
            indice_addition = split_expression.index('+')
            print("indice",indice_addition)
        
            total += int(split_expression[indice_addition-1]) + int(split_expression[indice_addition+1]) 
            print("total",total)
            split_expression.remove(split_expression[indice_addition-1])
            split_expression.remove(split_expression[indice_addition-1])
            split_expression.remove(split_expression[indice_addition-1])

            split_expression.insert(indice_addition-1,str(total))

            print("split",split_expression)
            if len(split_expression) !=1:
                total = evaluer_expression(" ".join(split_expression))
                print(total)
            else:
                return total

        elif "-" in expression:
            
            split_expression = expression.split()
            #print(split_expression)
            indice_soustraction = split_expression.index('-')
            #print(indice_soustraction)

            total += int(split_expression[indice_soustraction-1]) - int(split_expression[indice_soustraction+1]) 
            

            split_expression.remove(split_expression[indice_soustraction-1])
            split_expression.remove(split_expression[indice_soustraction-1])
            split_expression.remove(split_expression[indice_soustraction-1])

            split_expression.insert(indice_soustraction-1,str(total))

            print(split_expression)
            if len(split_expression) !=1:
                total = evaluer_expression(" ".join(split_expression))
                print(total)
            else:
                return total
            print(total)

    return total      
    
        


def verification_arguments(arguments):
    ok = True
    
    return ok


def afficher(chaine):
   pass


def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
         print("ok",evaluer_expression(arguments[0]))
        
    else:
        erreur()