# 2248321, Marcelo Coriat Hijar
# 6226989, Alek Hanachian

# fonction qui retourne True si l'annee est bissextile
def bissextile(annee:int):
    if annee % 4 == 0:
        if (annee % 100 == 0) and (annee % 400 != 0):
            return False
        else:
            return True
    else:
        return False

# fonction pour calculer le prix total selon la qte et le prix de chaque volaille
def prixAchat(qtePoulet:int, qteDinde:int, qtePoule:int):
    prixFinal:float = round(((qtePoulet * 2.25) + (qteDinde * 4.75) + (qtePoule * 15)), 2)
    return prixFinal


# fonction qui calcule le taux de mortalite de chaque animal
def tauxMortalite(type:str, qteInitiale:int):
    qteRestante:int = 0
    # verifie selon le type de chaque espece de volaille, arrondis a la position des entiers 
    if type == "poule":
        qteRestante = round(qteInitiale * 0.99)
    elif type == "poulet":
        qteRestante = round(qteInitiale * 0.95)
    elif type == "dindon":
        qteRestante = round(qteInitiale * 0.92)
    return qteRestante


# fonction pour definir quel type et prix selon le type et l'age de volaille
def prixMoulee(type:str, age:int):
    prix:int = 0
    qte:int = 0
    # check le type d'animal en premier et ensuite le prix pour l'age
    if type == "poulet":
        if age <= 4:
            prix = 20
            qte = 2
        # pas besoin de faire entre 4 et 8 puisque le code va aller de haut en bas et donc tomber dans la prochaine section lorsque necessaire
        # pas de difference de prix ni de qte entre 4 a 8 semaines et 8 a 10
        elif age <= 10:
            prix = 21
            qte = 4

    elif type == "dindon":
        if age <= 4:
            prix = 22
            qte = 3
        # qte et prix est la meme entre 4 a 8 et 8 a 10 semaines
        elif age <= 10:
            prix = 23
            qte = 5
        elif age <= 14:
            prix = 23
            qte = 11

    elif type == "poule":
        prix = ?????????????????
        qte = 6

    prixqte:list = [prix, qte]
    return prixqte


# fonction pour determiner la qte de sacs de litiere a acheter en fonction du nombre de semaines que l'animal vivera et quel animal
def qteLitiere(semaines:int, type:str):
    qteSacs:float = 0
    if type == "poule":
        # qte de sacs va etre multiplie par le nbre d'animaux hors de la fct et sera arrondi a la hausse apres
        qteSacs = semaines / 3
    elif type == "poulet": 
        qteSacs = semaines * 1.25
    elif type == "dindon":
        qteSacs = semaines * 3
    return qteSacs


# fonction pour calculer la qte de poulets abbatues pour semaines 4/8/10
def abattagePoulet(qte:int, age:int, qtePoules:int):
    qteAbattus:int = 0
    if age == 4:
        qteAbattus = round(qte / 3)
    if age == 8:
        qteAbattus = round(qtePoules / 2)
    if age == 10:
        qteAbattus = qte
    return qteAbattus


# fonction pour arrondir a la hausse si la valeur n'est pas egale a un total
def arrondirUP(unite:int, variableCheck:float):
    if variableCheck % unite == 0:
        return variableCheck
    else:
        # calcules la difference manquante entre la variableCheck et l'unite, la retourne pour arriver au multiple commun le plus pres vers le haut
        reste:int = variableCheck % unite
        reste = abs(unite - reste)
        return (round(variableCheck + reste))


# fonction calculant les frais initaux
def fraisInitiaux(qtePoules:int, qtePoulets:int, qteDindons:int):
    grandTotal:int = 0
    
    # ajout du cout inital des volailles
    grandTotal += prixAchat(qtePoulets, qteDindons, qtePoules)
    
    # creation de variables qui seront utilisees dans les calculs
    # litierePoule doit etre arrondi a la hausse a la fin de la boucle
    litierePoule:float = 0
    litierePoulet:float = 0
    # les variables mouleeType seront utilise pour calculer la qte de moulee a acheter, arrondis a la hausse au sac de 25 kg 
    mouleePoulet1:int = 0
    mouleePoulet2:int = 0
    mouleePoule:int = 0
    mouleeDindon1:int = 0
    mouleeDindon2:int = 0

    # calcule selon les semaines, s'arrette a la semaine 19 puisque toutes les vollailles seront abbatues a celle-ci (sauf bien sur les poules pondeuses)
    for i in range(1, 20):
        qtePoulets -= abattagePoulet(qtePoulets, i, qtePoules)
        # Calcule la qte de sacs de litieres necessaire, le total d'$ sera compte a la fin
        litierePoulet += qteLitiere(i, "poulet") * qtePoulets
        litierePoule += qteLitiere(i, "poule") * qtePoules
        grandTotal += (qteLitiere(i, "dindon") * qteDindons) * 9
        
        # calcul de la moulee pour chaque volaille par semaine de croissance
        # doit etre separe en 2 valeurs pour la difference de prix entre les 2 nourritures de chaque volaille
        # ******************************************************** manque la moulee de poule ******************************  
        if i <= 4:
            mouleePoulet1 += (prixMoulee("poulet", i)[1] * qtePoulets)
            mouleeDindon1 += (prixMoulee("dindon", i)[1] * qteDindons)
        else:
            mouleeDindon2 += (prixMoulee("dindon", i)[1] * qteDindons)
            mouleePoulet2 += (prixMoulee("poulet", i)[1] * qtePoulets)
            
    # arrondissement a la hausse pour acheter des sacs complets. 
    grandTotal += (arrondirUP(25, mouleePoulet1) * prixMoulee("poulet", 1)[0])
    grandTotal += (arrondirUP(25, mouleePoulet2) * prixMoulee("poulet", 5)[0])
    grandTotal += (arrondirUP(25, mouleeDindon1) * prixMoulee("dindon", 1)[0])
    grandTotal += (arrondirUP(25, mouleeDindon2) * prixMoulee("dindon", 5)[0])
    grandTotal += (arrondirUP(1, litierePoule) * 9)
    grandTotal += (arrondirUP(1, litierePoulet) * 9)

    

