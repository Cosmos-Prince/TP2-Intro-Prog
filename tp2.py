# 2248321, Marcelo Coriat Hijar
# 6226989, Alek Hanachian

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
    qte:float = 0
    # check le type d'animal en premier et ensuite le prix pour l'age
    # la qte indiquee dans le tableau et pour la periode donnee, d'ou les divisions dans la qte
    if type == "poulet":
        if age <= 4:
            prix = 20
            qte = 2/5
        # pas besoin de faire entre 4 et 8 puisque le code va aller de haut en bas et donc tomber dans la prochaine section lorsque necessaire
        elif age <= 8:
            prix = 21
            qte = 4/4
        elif age <= 10:
            prix = 21
            qte = 4/2

    elif type == "dindon":
        if age <= 4:
            prix = 22
            qte = 3/5
        elif age <= 8:
            prix = 23
            qte = 5/4
        elif age <= 10:
            prix = 23
            qte = 5/2
        elif age <= 19:
            prix = 23
            qte = 11/4

    elif type == "poule":
        prix = 21
        qte = 6/4

    # cree une liste contenant le prix et la qte de nourriture consomme par la volaille. 
    prixqte:list = [prix, qte]
    return prixqte


# fonction pour determiner la qte de sacs de litiere a acheter en fonction du nombre de semaines que l'animal vivera et quel animal
def qteLitiere(type:str):
    qteSacs:float = 0
    if type == "poule":
        # qte de sacs va etre multiplie par le nbre d'animaux hors de la fct et sera arrondi a la hausse apres
        qteSacs = 1 / 3
    elif type == "poulet": 
        qteSacs = 1.25
    elif type == "dindon":
        qteSacs =  3
    return qteSacs


# fonction pour calculer la qte de poulets abbatues pour semaines 4/8/10
# abbatus a la fin de la semaine aka au tt les dépenses de la semaines sont presents
def abattagePoulet(qte:int, age:int):
    qteRestants:int = 0
    if age == 5:
        qteRestants = round((2 * qte) / 3)
    elif age == 9:
        qteRestants = round(qte / 2)
    elif age == 11:
        qteRestants = 0
    else:
        qteRestants = qte
    return qteRestants


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
    grandTotal:float = 0
    
    # ajout du cout inital des volailles
    grandTotal += prixAchat(qtePoulets, qteDindons, qtePoules)
    
    # creation de variables qui seront utilisees dans les calculs
    # litierePoule doit etre arrondi a la hausse a la fin de la boucle
    litierePoule:float = 0
    litierePoulet:float = 0
    # les variables mouleeType seront utilise pour calculer la qte de moulee a acheter, arrondis a la hausse au sac de 25 kg 
    mouleePoulet1:float = 0
    mouleePoulet2:float = 0
    mouleePoule:float = 0
    mouleeDindon1:float = 0
    mouleeDindon2:float = 0

    # calcule selon les semaines, s'arrette a la semaine 19 puisque toutes les vollailles seront abbatues a celle-ci (sauf bien sur les poules pondeuses)
    for i in range(0, 19):
        qtePoulets = abattagePoulet(qtePoulets, i)
        # Calcule la qte de sacs de litieres necessaire, le total d'$ sera compte a la fin
        litierePoulet += qteLitiere("poulet") * qtePoulets
        litierePoule += qteLitiere("poule") * qtePoules
        grandTotal += (qteLitiere("dindon") * qteDindons) * 9
        
        # calcul de la moulee pour chaque volaille par semaine de croissance
        # doit etre separe en 2 valeurs pour la difference de prix entre les 2 nourritures de chaque volaille
        if i <= 4:
            mouleePoulet1 += (prixMoulee("poulet", i)[1] * qtePoulets)
            mouleeDindon1 += (prixMoulee("dindon", i)[1] * qteDindons)
        else:
            mouleeDindon2 += (prixMoulee("dindon", i)[1] * qteDindons)
            mouleePoulet2 += (prixMoulee("poulet", i)[1] * qtePoulets)
        # age de la poule n'est pas important pour la qte de moulee qu'elle consomme, mis a 19 puisqu'on les recoit a 19 semaines
        mouleePoule += (prixMoulee("poule", 19)[1] * qtePoules)
    
    # calculs pour le restant de l'annee, comprennant seulement les poules qui vont vivre 2 ans
    for i in range(19, 52):
        litierePoule += qteLitiere("poule") * qtePoules
        mouleePoule += (prixMoulee("poule", 19)[1] * qtePoules)
        
        
    # arrondissement a la hausse pour acheter des sacs complets. 
    grandTotal += (arrondirUP(25, mouleePoulet1) / 25 * prixMoulee("poulet", 1)[0])
    grandTotal += (arrondirUP(25, mouleePoulet2) / 25 * prixMoulee("poulet", 5)[0])
    grandTotal += (arrondirUP(25, mouleeDindon1) / 25 * prixMoulee("dindon", 1)[0])
    grandTotal += (arrondirUP(25, mouleeDindon2) / 25 * prixMoulee("dindon", 5)[0])
    grandTotal += (arrondirUP(25, mouleePoule) / 25 * prixMoulee("poule", 19)[0])
    grandTotal += (arrondirUP(1, litierePoule) * 9)
    grandTotal += (arrondirUP(1, litierePoulet) * 9)

    return grandTotal


# fonction qui retourne True si l'annee est bissextile
def bissextile(annee: int):
    if annee % 4 == 0:
        if (annee % 100 == 0) and (annee % 400 != 0):
            return False
        else:
            return True
    else:
        return False


# fonction pour calculer la qte d'oeufs sur 2 ans
def prodOeufs(qtePoules:int, anDepart:int):
    totalOeufs:int = 0
    # calcule pour la premiere annee utilisant la fct bissextile et tauxMortalite pour deteminer la qte d'oeufs
    # il a ete determine que le taux de mortalite arrivait a la fin de la periode donnee, donc a la fin de l'annee pour les poules
    if bissextile(anDepart) == True:
        totalOeufs = qtePoules * 366
    else:
        totalOeufs = qtePoules * 365

    # check pour la 2e annee, incluant le taux de mortalite de la 1ere annee
    if bissextile(anDepart + 1) == True:
        totalOeufs += tauxMortalite("poule", qtePoules) * 366
    else:
        totalOeufs += tauxMortalite("poule", qtePoules) * 365

    return totalOeufs


# fonction pour calculer la vente d'oeufs
def venteOeufs(qtePoules:int, net:bool, periodeTemps:str):
    revenus:float = 0
    # qte d'oeufs vendus
    qteVendus:int = 0
    # permets de calculer seulement les frais relies aux poules
    frais:float = fraisInitiaux(qtePoules, 0, 0)
    
    # calculs si on veut le revenu net
    if net == True:
        if periodeTemps == "semaine":
            # calcul est qtePoules * duree(en jours) * %vendu * prix
            qteVendus = qtePoules * 7 * 0.8
            revenus = arrondirUP(12, qteVendus) * 3.75 - (frais / 52)
        elif periodeTemps == "mois":
            # arrondi a 30 jours puisqu'on ne demande pas quel mois, pourrais etre amélioré
            qteVendus = qtePoules * 30 * 0.8
            revenus = arrondirUP(12, qteVendus) * 3.75 - (frais / 12)
        elif periodeTemps == "annee":
            # pas demande de check pour annee bissextile, pourrait etre implemente
            qteVendus = qtePoules * 365 * 0.8
            revenus = arrondirUP(12, qteVendus) * 3.75 - (frais)

    # calculs si on veut le revenu brut
    else:
        if periodeTemps == "semaine":
            # calcul est qtePoules * duree(en jours) * %vendu * prix
            qteVendus = qtePoules * 7 * 0.8
            revenus = arrondirUP(12, qteVendus) * 3.75
        elif periodeTemps == "mois":
            # arrondi a 30 jours puisqu'on ne demande pas quel mois, pourrais etre amélioré
            qteVendus = qtePoules * 30 * 0.8
            revenus = arrondirUP(12, qteVendus) * 3.75
        elif periodeTemps == "annee":
            # pas demande de check pour annee bissextile, pourrait etre implemente
            qteVendus = qtePoules * 365 * 0.8
            revenus = arrondirUP(12, qteVendus) * 3.75

    return revenus


# Calcul pour obtenir le dernier jour delevegae des Poulets et les Dindons
def derniereJournee(derniereSemainePoulets,derniereSemaineDindons):
    #Importation du module datetime pour faciliter la tache puisque nous avons deja lachat initiale des vollailles
    from datetime import datetime
    from datetime import timedelta
    dateDepart = datetime(2024,5,27)
    #Conversion de semaines en jours (7 jours/semaine)
    enJoursPoulets = derniereSemainePoulets*7
    dateFinPoulet = dateDepart + timedelta(days=enJoursPoulets)
    # cree un objet represente en Jours + dateDepart pour avoir la date en format y/m/d

    enJoursDindons = derniereSemaineDindons*7
    dateFinDindons = dateDepart + timedelta(days=enJoursDindons)
    return (dateFinDindons.strftime('%B %d, %Y'), dateFinPoulet.strftime('%B %d, %Y'))
    # %B donne le nom du mois, %d le jour, %Y l'an format XXXX


# Menu textuel pour montrer les calculs
execution=int(input("Programme de calculations pour aviculteurs\n"
      "Voici les calculs suivants dans l'ordre, pour commencer, veuillez taper '1'\n"
      "________________________________________________________________\n"
      "1- Calcul de frais initiales d'investissemet pour une Période de un an\n"
      "2- Calcul de la quantité d'œufs produite pour une période de deux ans\n"
      "3- Calcul de dernière journée d'élevage de Dindons et Poulets de chair\n"
      "Votre choix: "))
# POUR 5.1
match execution:
    case 1:
        qtePoules=int(input("\nVous avez choisi l'option 1"
                            "\nInvitez une réponse aux questions suivantes"
                            "\nQuantite de Poules: "))
        qtePoulets=int(input("Quantite de Poulets: "))
        qteDindons=int(input("Quantite de Dindons: "))
        print(fraisInitiaux(qtePoules, qtePoulets, qteDindons),"sera le coût d'investissement initial")
# POUR 5.2, 5.3.1 ET 5.3.2
    case 2:
        qtePoules = int(input("\nVous avez choisi l'option 2"
                              "\nInvitez une réponse aux questions suivantes"
                              "\nQuantite de Poules: "))
        anDepart = int(input("Quelle est l'an de depart: "))
        print(f"Vous produirez {prodOeufs(qtePoules, anDepart)} au cours des années {anDepart} et {anDepart + 1}")
        choix:int = int(input("Pour voir les revenus nets ou bruts au cours de la première année, entrez 1 pour brut et 2 pour net : "))
        if choix == 1:
            print(f"Vous générerez un revenu brut de \n{venteOeufs(qtePoules, False, "semaines")}$ par semaine,")
            print(f"{venteOeufs(qtePoules, False, "mois")}$ par mois et")
            print(f"{venteOeufs(qtePoules, False, "annee")}$ par année.")
        elif choix == 2:
            print(f"Vous générerez un revenu net de \n{venteOeufs(qtePoules, True, "semaines")}$ par semaine,") 
            print(f"{venteOeufs(qtePoules, True, "mois")}$ par mois et")
            print(f"{venteOeufs(qtePoules, True, "annee")}$ par année.")
            
# POUR 5.4 ET 5.5
    case 3:
        print("\nVous avez choisi l'option 3"
              "\nInvitez une réponse aux questions suivantes")
        derniereSemainePoulets = int(input("Quelle est la derniere semaine prevue pour les Poulets: "))
        derniereSemaineDindons = int(input("Quelle est la derniere semaine prevue pour les Poulets: "))
        dindons, poulets = derniereJournee(derniereSemainePoulets, derniereSemaineDindons)
        print(f"\nDate de fin des Dindons: {dindons}")
        print(f"Date de fin des Poulets: {poulets}")

