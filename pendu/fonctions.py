# -*- coding: utf-8 -*-
import random
import pickle

def mot_a_trouver(liste_mots):
    return random.choice(liste_mots)

def afficher_score(scores, pseudo):
    print("Votre score est de {} points ".format(scores[pseudo]))

def demander_lettre():
    lettre = input("Quelle est votre lettre ou votre proposition ?")
    return lettre

def retrouver_score_joueur(scores, pseudo):
    score = 0
    try:
        score = scores[pseudo]
        print ("welcome back {} !".format(pseudo))
    except:
        print ("Bienvenue {}, ravi de faire votre connaissance".format(pseudo))
        scores[pseudo] = 0
    afficher_score(scores,pseudo)
    return score

def masquer(mot_a_trouver, lettres_jouees):
    mot_masque = str()
    #for i, lettre in enumerate(mot_a_trouver):
    for lettre in mot_a_trouver:
        if lettre in lettres_jouees:
            mot_masque = mot_masque + lettre + " "
        else:
            mot_masque+="_"
    trouve = "_" not in mot_masque
    return mot_masque, trouve

def charger_scores(nom_fichier):
    with open(nom_fichier,'rb') as fichier_scores:
        scores= dict()
        scores_depickler = pickle.Unpickler(fichier_scores)
        try:
            scores = scores_depickler.load()
        except EOFError:
            print("Vous êtes mon premier joueur, Bravo !")
        return scores

def sauvegarder_scores(nom_fichier, scores):
    with open(nom_fichier, 'wb') as fichier_scores:
        scores_pickler= pickle.Pickler(fichier_scores)
        scores_pickler.dump(scores)

def continuer_a_jouer():
    reponse = input("Voulez-vous continuer à jouer (o/n)?")
    if reponse == "o" or reponse == "O":
        return True
    else:
        return False
        
    
        
        
