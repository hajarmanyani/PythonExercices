"""
ECXERCICE 3

"""

long1= float(input("Donner la 1er longueur du triangle \n"))
long2= float(input("Donner la 2er longueur du triangle \n"))
long3= float(input("Donner la 3er longueur du triangle \n"))

if long1==long2 and long2==long3:
    print("Le triangle est equilatéral \n")
elif long1==long2 and long3!=long2 or long2==long3 and long1!=long2 or long1==long3 and long2!=long1:
    print("Le triangle est isocèle \n")
else:
    print("Le triangle est scalène \n")  

"""
Exercice 4

"""

i=0
liste = []
x=9
while x!=0:
    if x!=0:
        x=float(input(f"Donnez une valeur {i+1} "))
        liste.append(x)
        i=i+1
    else:
        break

s=0
for l in liste:
    s+=l
    
moyenne=s/(i-1)
print(f"La moyenne est {moyenne}")





