from random import *
n=randint(0,100)
essais=1
u=-1
while u!=n and essais<8:
    u=int(input("A quel nombre vous pensez ?"))
    essais=essais+1
    if u>n:
        print("Le nombre cherché est + petit")
    elif u<n:
        print("Le nombre cherché est + grand")
if u==n:
    print("trouvé")
else:
    print("trop lent")