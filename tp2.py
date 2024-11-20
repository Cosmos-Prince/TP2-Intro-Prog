# 2248321, Marcelo Coriat Hijar

# sous-programme / calculation du cout de l'ensemble d'achat des volailles
def cout_volailles(poussins,dindonneau,poules_pondeuses):
    cout=(poussins[0]*poussins[1])+(dindonneau[0]*dindonneau[1])+(poules_pondeuses[0]*poules_pondeuses[1])
    return cout
poussins=45,2.25
dindonneau=7,4.75
poules_pondeuses=23,15
print(cout_volailles(poussins,dindonneau,poules_pondeuses))

# sous programme / calculation des taux de mortalite par espece volaille
# suite a cette operation nous pouvons calculer respectivement les depenses des especes (espace m2,nourriture..etc)
def taux_mortalite(tm_poussins,tm_dindonneau,tm_poules_pondeuses):
    poussins_nv=round(45*(1-0.05))
    dindonneau_nv=round(7*(1-0.08))
    poules_pondeuses_nv=round(23*(1-0.01))
    return poussins_nv,dindonneau_nv,poules_pondeuses_nv
tm_poussins=0.05
tm_dindonneau=0.08
tm_poules_pondeuses=0.01
poussins_nv,dindonneau_nv,poules_pondeuses_nv = taux_mortalite(tm_poussins,tm_dindonneau, tm_poules_pondeuses)
print(poussins_nv,dindonneau_nv,poules_pondeuses_nv)


def calcul_dindon():
    total_semaine=19
    consommation_sm4=3
    consommation_sm10=5
    consommation_sm19=11
    # initialisation de nos variables concernant les dindons
    moulee_debut=22  # 1 sac de moulee = 25kg
    nb_moulee_debut=0
    moulee_croissance=23
    nb_moulee_croissance=0
    prix_sac_rip=9 # 1 sac couvre 1 m2 / 9$ (un dindon necessite 3 m2)
    reste_sac_rip=25
    reste_sac_rip_resultat=0

    for i in range(1, total_semaine + 1):
        if i <= 4:  # Semaines 1 à 4
            consommation = consommation_sm4 * dindonneau_nv
            if reste_sac_rip_resultat < consommation:
                nb_moulee_debut += 1
                reste_sac_rip_resultat += 25  # Ajouter un nouveau sac

            reste_sac_rip_resultat -= consommation  # Consommation hebdomadaire
            if i == 4:
                cout = nb_moulee_debut * moulee_debut
                reste_sac_rip_resultat = 0

    return cout

print(calcul_dindon())