def compter_occurrences_caractere(chaine, caractere):
    return chaine.count(caractere)

chaine = input("Entrez une chaîne de caractères : ")
caractere = input("Entrez le caractère à compter : ")
occurrences = compter_occurrences_caractere(chaine, caractere)
print("Le caractère '{}' apparaît {} fois dans la chaîne.".format(caractere, occurrences))
