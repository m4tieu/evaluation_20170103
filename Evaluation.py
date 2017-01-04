tablTheme = []
tablQuest = []
tablQcm = []
tablRep = []
line = ""
evaluation = False

# Fonction qui lit le fichier questions.qs et trie les lignes
def fetch():
    with open("questions.qs","r") as qs:
        # Lit le fichier questions.qs ligne par ligne
        for line in qs:
            # line = line.rstrip()
            # a chaque fois qu'une ligne est stockee dans un tableau, les deux autres tableaux recoivent une case vide
            # si la ligne lue commence par ##, elle est stockee dans le tableau theme
            if line.startswith("##"):
                tablTheme.append(line)
                tablQuest.append("")
                tablQcm.append("")
            # si la ligne lue commence par #, elle est stockee dans le tableau questions
            elif line.startswith("#"):
                tablQuest.append(line)
                tablTheme.append("")
                tablQcm.append("")
            # si la ligne lue commence par -, elle est stockee dans le tableau qcm
            elif line.startswith("-"):
                tablQcm.append(line)
                tablTheme.append("")
                tablQuest.append("")

def eval():
    # tant que i se trouve dans la longueur du tableau
    for i in range(len(tablQuest)) :
        rep = ""
        # si l'index du tableau theme n'est pas vide
        if tablTheme[i] != "" :
            # on affiche le contenu de l'index theme
            print tablTheme[i]
        # sinon si le tableau questions n'est pas vide
        elif tablQuest[i] != "" :
            # si le tableau qcm suivant n'est pas vide
            if tablQcm[i+1] != "" :
                # on affiche le contenu de l'index du tableau questions
                print tablQuest[i]
            # sinon si le tableau qcm suivant est vide
            else :
                # on demande la reponse a la question indiquee
                rep= raw_input(tablQuest[i])
                # la reponse est stockee dans le tableau reponse
                tablRep.append(rep)
        # sinon si le tableau qcm n'est pas vide
        elif tablQcm[i] != "" :
            # on affiche le contenu de l'index qcm
            print tablQcm[i]
            # si i a atteint la longueur du tableau OU si l'index suivant contient une question
            if i == len(tablQuest) - 1 or tablQuest[i+1] != "" :
                # on demande la reponse au qcm
                rep= raw_input("Ecrivez la bonne reponse. ")
                # la reponse est stockee dans le tableau reponse
                tablRep.append(rep)

fetch()
eval()
