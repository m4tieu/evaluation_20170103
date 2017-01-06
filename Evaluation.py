import time
import datetime

tablTheme = []
tablQuest = []
tablQcm = []
tablRep = []
tablStamp = []
line = ""

# Fonction qui lit le fichier questions.qs et trie les lignes
def fetch():
    with open("questions.qs","r") as qs:
        # Lit le fichier questions.qs ligne par ligne
        for line in qs:
            line = line.rstrip()
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
                # on stocke le timestamp dans le tableau Stamp
                tablStamp.append(time.strftime("%H h %M min %S sec"))
                # la reponse est stockee dans le tableau reponse
                tablRep.append(rep)
        # sinon si le tableau qcm n'est pas vide
        elif tablQcm[i] != "" :
            # on affiche le contenu de l'index qcm
            print tablQcm[i]
            # si i a atteint la longueur du tableau OU si l'index suivant contient une question OU un theme
            if i == len(tablQuest) - 1 or tablQuest[i+1] != "" or tablTheme[i+1] != "":
                # on demande la reponse au qcm
                rep= raw_input("Ecrivez la bonne reponse. ")
                # on stocke le timestamp dans le tableau Stamp
                tablStamp.append(time.strftime("%H h %M min %S sec"))
                # la reponse est stockee dans le tableau reponse
                tablRep.append(rep)

def write():
    # on ouvre le fichier index.html en mode ecriture (ou on le cree si le fichier n'existe pas) la variable f correspond au fichier
    with open("resultat/index.html","w+") as f:
        i = 0
        j = 0
        # cette fonction ecrit le nom de la thematique dans les balises html appropriees
        def debTheme() : f.write('<article>\r\n<h3>' + tablTheme[i] + '</h3>\r\n')
        # cette fonction ecrit le numero de la question, nom de la question et timestamp dans leurs balises html appropriees
        def question() : f.write('<section>\r\n<h4><span>Question '+ str(j+1) +'</span> ' + tablQuest[i] + ' <span>' + tablStamp[j] + '</span></h4>\r\n')
        # cette fonction ecrit une reponse dans les balises html appropriees
        def reponse() : f.write('<p>' + tablRep[j] + '</p>\r\n</section>\r\n\n')
        # cette fonction ferme la balise article qui a ete ouverte dans la fonction debTheme
        def finTheme() : f.write('</article>\r\n')
        # on ecrit le debut du document html (inutile d'en faire une fonction car on ne l'ecrit qu'une seule fois)
        f.write('<html>\r\n<head>\r\n<meta http-equiv="content-type" content="text/html; charset=utf-8" />\r\n<title>evaluations du 03 janvier 2017 - Lunel</title>\r\n<link rel="stylesheet" type="text/css" href="style.css">\r\n</head>\r\n\n<body>\r\n<h1>evaluations du 03 janvier 2017 - Lunel</h1>\r\n<h2>Paul Maillard</h2>\r\n')
        # tant que i se trouve dans l'etendue de la longueur du tableau
        for i in range(len(tablQuest)):
            #  si le tableau theme n'est pas vide
            if tablTheme[i] != "":
                # si on est pas au debut du questionnaire
                if j != 0:
                    # on ferme la balise article
                    finTheme()
                # on ouvre un nouveau theme
                debTheme()
            # sinon si le tableau theme n'est pas vide
            elif tablQuest[i] != "":
                # on appelle la fonction question
                question()
                # puis on appelle la fonction reponse
                reponse()
                # si j est inferieur ou egal a la longueur du tableau reponse
                if j <= len(tablRep):
                    # on incremente j
                    j += 1
        # on appelle la fonction finTheme
        finTheme()
        # on ecrit les balises de fin du document
        f.write('</body>\r\n</html>')

fetch()
eval()
write()
