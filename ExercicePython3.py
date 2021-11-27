# On demande à l'utilisateur de donner son poids en kg et sa taille en mètre
poids = float(input("Entrer votre poids en kg :"))
taille = float(input("Entrer votre taille en mètre (exemple 1.79) ! "))

# On calcule l'imc
imc = int(poids / taille ** 2)

# On affiche le résultat
print("Votre IMC est", imc)
