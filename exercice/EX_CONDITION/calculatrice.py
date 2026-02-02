import sys

nbr1 = input("Entrez lz premier nombre: ")
nbr2 = input("Entrez le second nombre : ")
    
if not nbr1.isnumeric() or not nbr2.isnumeric():
        print(('Error: les deux nombre doivent etres des nombre Entiers.'))
        sys.exit()

nbr1 = int(nbr1)
nbr2 = int(nbr2)

operation = input("ENTREZ L'OPERATION ('+', '-', '*', '/'): ") 

match operation:
    case "+":
        result = nbr1 + nbr2 
    case "-":
        result = nbr1 - nbr2
    case "*":
        result = nbr1 * nbr2   
    case "/":
        if nbr2 == 0:
            print("Error: on ne peut pas diviser par zero.")
            sys.exit()
        result = round(nbr1 / nbr2, 2)
    case _:
        print("Error: l'operation n'est pas valide.")
        sys.exit()
        
phrase = f"Le resultat de {nbr1} {operation} {nbr2} est {result}."
print("------------------------RESULTAT DE L4OPERATION-------------------------")    
print(phrase)
        
        

        
