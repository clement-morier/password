import random
import hashlib
import json
import os

def newmotdepasse():
    return(input('Veuillez entrer votre mot de passe :'))

def verif(mot):
    motliste=[]
    for h in range (len(mot)):
        motliste.append((mot[h]))
    n=len(motliste)
    if n >= 8:
        for i in range(n):
            if mot[i].isupper() == True :
                for j in range(n):
                    if mot[j].islower() == True :
                        for k in range(n):
                            if mot[k].isdigit() == True :
                                for l in range(n):
                                    if mot[l] == '!' or mot[l] == '@' or mot[l] == '#' or mot[l] == '$' or mot[l] == '%' or mot[l] == '^' or mot[l] == '&' or mot[l] == '*' or mot[l] == '?' :
                                        m = hashlib.sha256()
                                        m.update(mot.encode('utf-8'))
                                        fichier="Mot_de_passe.json"
                                        taille = os.path.getsize(fichier)
                                        if taille == 0:
                                            data=[m.hexdigest()]
                                            with open("Mot_de_passe.json","w") as f:
                                                json.dump(data,f)
                                        else:
                                            with open("Mot_de_passe.json","r") as f:
                                                data = json.load(f)
                                            data.append(m.hexdigest())
                                            doublons(data)
                                            with open("Mot_de_passe.json","w") as f:
                                                json.dump(data, f)
                                        return True
    else :
         return False

def doublons(L):
    c=0
    L_unique=[]
    vide=[]
    for elem in L :
        if elem not in L_unique:
            vide=[elem]
            L_unique=L_unique+vide
    return(L_unique)

def aléatoire():
    Alphabet_minuscule=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Alphabet_majuscule=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    Chiffres=["0","1","2","3","4","5","6","7","8","9"]
    Spéciales=["!","@","#","$","%","^","&","*","!"]
    mdp=''
    i=random.randint(0,len(Alphabet_minuscule)-1)
    j=random.randint(0,len(Alphabet_majuscule)-1)
    k=random.randint(0,len(Chiffres)-1)
    m=random.randint(0,len(Spéciales)-1)
    mdp = mdp + Alphabet_minuscule[i] + Alphabet_majuscule[j] + Chiffres[k] + Spéciales[m]
    for t in range (3):
        w=random.randint(0,3)
        if w == 0:
            i=random.randint(0,len(Alphabet_minuscule)-1)
            mdp = mdp + Alphabet_minuscule[i]
        if w == 1:
            j=random.randint(0,len(Alphabet_majuscule)-1)
            mdp = mdp + Alphabet_majuscule[j]
        if w == 2:
            k=random.randint(0,len(Chiffres)-1)
            mdp = mdp + Chiffres[k]
        if w == 3:
            m=random.randint(0,len(Spéciales)-1)
            mdp = mdp + Spéciales[m]
    m = hashlib.sha256()
    m.update(mdp.encode('utf-8'))
    fichier="Mot_de_passe.json"
    taille = os.path.getsize(fichier)
    if taille == 0:
        data=[m.hexdigest()]
        with open("Mot_de_passe.json","w") as f:
            json.dump(data,f)
    else:
        with open("Mot_de_passe.json","r") as f:
            data = json.load(f)
        data.append(m.hexdigest())
        doublons(data)
        with open("Mot_de_passe.json","w") as f:
            json.dump(data, f)
    
c=0
while c < 4 :
    ouinon3=input('Ajouter un mot de passe aléatoire ? (Oui/Non) :')
    if ouinon3 == "Oui":
        aléatoire()
        break
    elif ouinon3 == "Non":
        Ouinon=input('Ajouter un nouveau mot de passe ? (Oui/Non) :')
        if Ouinon == "Oui" :
            if verif(newmotdepasse()) == True :
                print('Le mot de passe est valide')
                break
            else :
                print("Le mot de passe n'est pas valide")
        elif Ouinon == "Non" :
            ouinon2=input('Afficher les mot de passe enregistrés ? (Oui/Non) :')
            if ouinon2 == "Oui":
                with open("Mot_de_passe.json","r") as f:
                    data = json.load(f)
                print("Voici les mot de passe enregistrés :")
                for i in range (len(data)):
                    print(data[i])
                    break
            elif ouinon2 == "Non" :
                break
            else :
                print("Veuillez entrer une réponse valide")
        else :
            print("Veuillez rentrer une réponse valide")
    else:
        print("Veuillez rentrer une réponse valide")
    c+=1