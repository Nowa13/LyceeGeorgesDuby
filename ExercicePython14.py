n=10
while n>0:
    j=-1
    while j<1 or j>3 or j>n:
        j=int(input("combien?"))
    n=n-j
    if n==0:
        print("vous avez perdu!")
    else:
        print("il en reste",n)
        if n%4==3:
            p=2
        elif n%4==0:
            p=3
        else:
            p=1
        print("j'en prends",p)
        n=n-p
        print("il en reste",n)
        if n==0:
            print("j'ai perdu")