#Algorithme du jeu du pendu
import os
import random
import unicodedata

#Définition des fonction

def lecture(nom_fichier):
    #Entrée: nom du fichier à lire
    #Sortie: le contenu du texte

    if os.path.exists(nom_fichier):
        #Ouvrir le fichier en mode lecture
        with open(nom_fichier, 'r', encoding='utf8') as fio:
            #Lire le contenu du fichier ligne par ligen
            mots = [ligne.strip() for ligne in fio]
            #contenu = unicodedata.normalize('NFD', contenu).encode(encoding='ASCII', errors='ignore').decode('utf8')
        return mots
    else:
        return True

def mot_au_hasard(liste):
    #Renvoie un mot au hasard dans une liste de mot
    return random.choice(liste)

def accent(mot):
    #Enlève les accents d'un mot
    return unicodedata.normalize('NFD', mot).encode(encoding='ASCII', errors='ignore').decode('utf8')

def separer_lettres(mot):
    #Fonction permettant de stocker les lettres d'un mot dans une liste
    lettres = [lettre for lettre in mot]
    return lettres

def chercher_lettre(guess,liste_lettres,reponse):
    #Test si la lettre donnée est dans le mot
    if guess in liste_lettres:
        #Si oui on regarde où
        for i, l in enumerate(liste_lettres):
            if l == guess:
                #On ajoute là ou les lettres dans la réponse
                reponse[i] = guess
        #on retourne true
        return True
    else:
        #Si non on retourne false
        return False


def demande_lettre(guess,tentatives):
    #Fonction de vérification de conformité de la réponse de l'utilisateur

    if guess == '': #L'utilisateur n'a rien écrit
        print("Tu n'as rien écrit")
        return(True)
    if len(guess) > 1: #L'utilisateur a écrit plusieurs lettres
        print("Tu as rentré plusieurs lettres")
        return True
    elif guess in tentatives: #L'utilisateur a déjà porposé cette lettre
        print("Tu as déjà proposé cette letttre")
        return(True)
    else:
        return(False)

def indice(tentatives,liste_lettres):
    #Détecte la première lettre de l'alphabet qui n'est pas dans le mot et
    #qui n'a pas été donnée auparavant
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for lettre in alphabet:
        if lettre not in tentatives and lettre not in liste_lettres:
            return lettre
    return None

def pendu(liste_lettres):
    #Algorithme de pendu
    vie = 6
    reponse = []
    tentatives = []
    for i in range(len(liste_lettres)):
        #Construction du mot composé de tirés
        reponse.append("_")

    while vie >0 and '_' in reponse:
        #Affichage du nombre de vie à l'utilisateur
        if vie > 1:
            print(f"Il vous reste {vie} vies.")
        else:
            print("Il vous reste 1 vies.")
            #Indice dans le cas où une seule vie restante
            print(f"Voici un indice: {indice(tentatives,liste_lettres)} n'est pas dans le mot.")


        #Tant qu'il reste une vie au joueur on affiche le mot caché et on demande
        #au joueur d'entrer une lettre
        print(''.join(reponse))
        guess = input("Entrez une lettre: ").lower()


        #Test de conformité de l'entrée
        while demande_lettre(guess,tentatives) != False:
            print(''.join(reponse))
            guess = input("Entrez une lettre: ").lower()

        #On stock les lettres déjà dites
        tentatives.append(guess)


        if chercher_lettre(guess,liste_lettres,reponse):
            #Si la lettre est dans le mot
            print(f"Bravo ! La lettre '{guess}' est dans le mot.")
            print("")
            print("")

        else:
            # Si la lettre n'est pas dans le mot
            vie -= 1
            print(f"Dommage, la lettre '{guess}' n'est pas dans le mot.")
            print("")
            print("")

    if '_' not in reponse:
        #Si le mot a été trouvé
        print(f"Félicitation vous avez trouvé le mot : {''.join(liste_lettres)}")
        print("")
        print("")
    else:
        # Si plus de vie
        print(f"Dommage vous n'avez plus de vie, le mot été : {''.join(liste_lettres)}")
        print("")
        print("")
    return 0


#Algorithme principal
def interface():
    print("Bienvenue dans le jeu du pendu")
    liste = lecture("mots_pendu.txt")

    if liste == True:
        #Si le fichier existe on le prend
        print("Pas de fichier mots_pendu.txt, sélection du jeu de donnée par défaut.")
        # On utilise le fichier texte fourni "texte.txt"
        liste = lecture("texte.txt")
        # On choisit un mot au hasard
        mot = mot_au_hasard(liste)
        # On enlève les potentiels accents
        mot = accent(mot)
        # Stockage des lettres dans une liste
        lettres = separer_lettres(mot)
        pendu(lettres)

    else:
        #Si le fichier n'existe pas on choisit celui par défaut
        print("Fichier mots_pendu.txt détécté.")
        # On choisit un mot au hasard
        mot = mot_au_hasard(liste)
        # On enlève les potentiels accents
        mot = accent(mot)
        # Stockage des lettres dans une liste
        lettres = separer_lettres(mot)
        pendu(lettres)

    print("Voulez-vous recommencer une partie ? oui/non")
    reponse = input().lower()
    while reponse != "oui" and reponse != "non":
        print("La réponse doit être oui ou non. ")
        reponse = input().lower()

    if reponse == "oui":
      interface()
    else:
        print("Aurevoir !")
    return 0

interface()