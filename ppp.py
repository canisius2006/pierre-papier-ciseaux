"""Here is the documentation of this module, here, we import this to the logique"""
#Ici, importation du module random
import random 
#Importation du module os et sys pour pouvoir assurer la gestion de la localisation de l'image au cas où la compression se fera en fichier exe
import os, sys

# Donc ici, les boutons vont renvoyer des nombres

# Ici, 0 réprésente pierre, 1 papier et 2 ciseau
def reussir(utilisateur:int,ordinateur:int) -> str:
    """cette fonction va nous permettre de savoir si le joueur à gagner ou non . En fait, il retourne le nom de celui qui gagne """
    match utilisateur:
        case 0:
            match ordinateur:
                case 0:
                    resultat = 'nul'
                case 1:
                    resultat = 'ordinateur'
                case 2:
                    resultat = 'utilisateur'
        case 1:
            match ordinateur:
                case 0:
                    resultat = 'utilisateur'
                case 1:
                    resultat = 'nul'
                case 2:
                    resultat = 'ordinateur'
        case 2:
            match ordinateur:
                case 0:
                    resultat = 'ordinateur'
                case 1:
                    resultat = 'utilisateur'
                case 2:
                    resultat = 'nul'
    return resultat


def point(resultat: str) -> tuple:
    """Cette fonction va nous permettre d'accorder le système de points
    L'utilisateur est en indice zéro du tuple"""
    if resultat == "ordinateur":
        points = 0,10
    if resultat == "nul":
        points = 0,0
    if resultat == "utilisateur":
        points = 10,0
    return points


def choix_ordi():
    """Cette fonction va nous permettre à l'ordinateur de choisir un nombre pour le jeu"""
    choix = random.randint(0,2)
    return choix


def resource_path(relative_path):
    """Cette fonction va nous permettre de trouver le bon chemin d'une photo quelle soit compiler en exe ou en py"""
    try:
        #le fichier temporaire que crée l'app lors de l'exécution
        base_path = sys._MEIPASS
    except :
        base_path = os.path.abspath('.')
    return os.path.join(base_path,relative_path)






























































tableau = ['pierre','papier','ciseau']
recompense = {'utilisateur':0,'ordinateur':0}
def jeux():
    """Fonction principale"""
    while True:
        try:
            print("Nous allons commencer notre jeu de Pierre papier ciseaux",',\n',"Choissisez un numéro parmi ceux disponibles")
            valeur = int(input("""\n1- Pierre \n2- Papier \n3- Ciseaux\n""")) -1 #Parce que dans mon programme, le premier indice est 0
            if valeur in [0,1,2]:
                pass
            else:
                print("La valeur que vous avez choisi n'est pas dans l'intervalle ")
                input()
                continue
        except:
            print("Veillez à bien entrer une valeur entière")
            continue
        print("Vous avez choisi ",tableau[valeur])
        choix = choix_ordi()
        print("L'ordinateur a choisi ",tableau[choix])
        input()
        vainqueur = reussir(valeur,choix)
        if vainqueur == 'ordinateur':
            print("L'ordinateur a gagné")
        elif vainqueur == 'utilisateur':
            print("Vous avez gagné")
        elif vainqueur == 'nul':
            print("C'est un match nul")
        input()
        print("Vous gagnez ",point(vainqueur)[0])
        print("L'ordinateur gagne ",point(vainqueur)[1])
        recompense['utilisateur']+=point(vainqueur)[0]
        recompense['ordinateur']+=point(vainqueur)[1]
        input()
        x = recompense['utilisateur']
        y = recompense['ordinateur']
        print(f"Vous êtes à {x} points et l'ordinateur est à {y} points")
        reprendre = input("Est-ce que vous voulez reprendre ?(1 ou 2 ): \n")
        if int(reprendre) == 1:
            continue
        else:
            print("A tout à l'heure")
            break

if __name__=="__main__":
    jeux()

