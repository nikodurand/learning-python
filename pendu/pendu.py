# -*- coding: utf-8 -*-
import donnees
import fonctions

fichier_score = 'scores'
scores = fonctions.charger_scores(fichier_score)

pseudo = input("Quel est votre pseudo ?")
score = fonctions.retrouver_score_joueur(scores, pseudo)
fonctions.sauvegarder_scores(fichier_score, scores)
nb_tentatives = donnees.nb_tentatives

continuer = True

while continuer:
    mot_a_trouver = fonctions.mot_a_trouver(donnees.liste_mots)
    nb_tentatives = donnees.nb_tentatives
    lettres_jouees = str()
    mot_masque, trouve = fonctions.masquer(mot_a_trouver, lettres_jouees)
    while (nb_tentatives > 0) and not trouve:
        print("Tentatives restantes : " + str(nb_tentatives))
        print("Lettres jouées : " + lettres_jouees)
        print("Mot à trouver : " + mot_masque)
        lettre = fonctions.demander_lettre()
        lettres_jouees += lettre
        if lettre in mot_a_trouver:
            print("La lettre {} est bien présente ! Super".format(lettre))
            mot_masque, trouve = fonctions.masquer(mot_a_trouver, lettres_jouees)
        else:
            print("Oh dommage, la lettre {} n'est pas dans le mot".format(lettre))
            nb_tentatives -= 1
    if trouve:
        print("Bravo vous avez trouvé :" + mot_a_trouver)
        score += nb_tentatives + 1
        print("Il vous restait {} tentatives".format(score))
        scores[pseudo] = score
        print("Votre nouveau score est de {} points".format(score))
        fonctions.sauvegarder_scores(fichier_score, scores)
    else:
        print("Nombre max de tentative atteint. Perdu ! Dommage !")
        print("Le mot à trouver était : " + mot_a_trouver)
    continuer = fonctions.continuer_a_jouer()
 
