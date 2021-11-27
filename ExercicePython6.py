a=int(input("ton age"))
if a<0:
    print("age non valide")
else:
    if a<8:
        p=5
    elif a==8:
        p=10
    else:
        p=20
    print(p)
