import sys


def indice_lettre(lettre):
    return ord(lettre.lower()) - 96


def affiche_ligne(lettre, nb_espaces, lettre_courante, largeur_ligne):
    if lettre_courante == 'a':
        return("a".center(largeur_ligne, ' ')) + '\n'
    elif lettre_courante == lettre:
        return(lettre_courante.ljust(largeur_ligne - 1) + lettre_courante) + '\n'
    else:
        return("".ljust(nb_espaces) + lettre_courante.ljust(largeur_ligne - nb_espaces * 2 - 1) + lettre_courante + "".ljust(nb_espaces)) + '\n'


def diamond(lettre):
    alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    revert = []
    nb = 0
    nb_espaces = indice_lettre(lettre) - 1
    largeur_ligne = indice_lettre(lettre) * 2 - 1
    diamond = ''
    for i in alpha:
        if i == lettre:
            diamond += affiche_ligne(lettre, nb_espaces, i, largeur_ligne)
            nb_espaces = 1
            break
        revert.append(i)
        diamond += affiche_ligne(lettre, nb_espaces, i, largeur_ligne)
        nb_espaces -= 1
        nb += 1
    revert.sort(reverse=True)
    for j in revert:
        diamond += affiche_ligne(lettre, nb_espaces, j, largeur_ligne)
        nb_espaces += 1
    return diamond

# Juste pour pouvoir le lancer en ligne de commande
argv = sys.argv

if len(argv) > 2 or len(argv) == 1:
    print('usage : python diamond.py a')
else:
    lettre = sys.argv[1].lower()
    print(diamond(lettre))
