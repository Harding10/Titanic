
list_vide = []


mylist = input("Entres des nombre en les separant par une virgule ex 1,2,?,3: ").split(",")


for i in mylist:
    list_vide.append(int(i.strip()))
    
somme = sum(list_vide)
quantiter = len(list_vide)

moyenne = round(somme / quantiter,2)
    
print(f"somme des nombre est : " ,moyenne)

