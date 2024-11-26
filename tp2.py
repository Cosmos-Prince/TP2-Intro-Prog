# 2248321, Marcelo Coriat Hijar

execution=int(input("options de gestion automatisé d'élevage de volailles:"
                    "\nInitier Un Calcul De Vos Investissements Initiaux Tapez '1' : "))

if execution==1:
    def dindon():
        print("stocker les information pour les dindons de chair: ")
        dindon=int(input("quantite achete: "))
        prix_dindon=float(input("prix dun dindon $ : "))
        cout_achat=(dindon*prix_dindon)

        # cout depense rip
        m2_dindon=float(input("l'espacement en metre carre d'un dindon: "))
        prix_rip=float(input("le prix de la rip: (Nous utiliserons ce prix pour toutes les autres espèces) "))
        abattage_dindon=int(input("a quelle semaine est prevue l'abatagge: "))
        cout_rip=(m2_dindon*prix_rip*abattage_dindon*dindon)

        # cout depense moulee
        moulee_deb_dindon=float(input("prix de la moulee de debutant: (cette moulee est utilisee entre les semaines 0 a 4) "))
        moulee_croi_dindon=float(input("prix de la moulee de croissance: (cette moulee est utilisee apartir de la semaine 5 "))
        tm_dindon= float(input("quelle est le taux mortalite en %: "))
        # semaine 0 a 4
        semaine0a4=round((4*3*dindon)/25)
        semaine0a4_quantite=(4*3*dindon)
        while (semaine0a4*25)<(4*3*dindon):
            semaine0a4 +=1
        cout_moulee=(semaine0a4*moulee_deb_dindon)

        # CONSOM CROISSANCE
        # semaine 4 a 8
        semaine4a8=round((4*5*dindon)/25)
        semaine4a8_quantite=(4*5*dindon)
        while (semaine4a8*25)<(semaine4a8_quantite):
            semaine4a8 +=1
        else:
            restant=(semaine4a8*25)-(semaine4a8_quantite)
        cout_moulee=cout_moulee+(semaine4a8*moulee_croi_dindon)
        # semaine 8 a 10
        semaine8a10=round((2*5*dindon)/25)
        semaine8a10_quantite=(2*5*dindon)
        if restant > 0:
            semaine8a10_quantite - restant
        while (semaine8a10*25)<(semaine8a10_quantite):
           if restant>0:
               semaine8a10_quantite-restant
           else:
               semaine4a8 +=1
        cout_moulee=cout_moulee+(semaine8a10*moulee_croi_dindon)
        # semaine 10 a 19
        semaine10a19 = round((9 * 11 * dindon) / 25)
        semaine10a19_quantite = (9 * 11 * dindon)
        if restant > 0:
            semaine10a19_quantite - restant
        while (semaine10a19 * 25) < (9 * 11 * dindon):
             semaine10a19 += 1
        cout_moulee=cout_moulee+(semaine10a19*moulee_croi_dindon)
        total_dindon=cout_moulee+cout_achat+cout_rip
        total_dindon=total_dindon*(1-(tm_dindon/100))
        return total_dindon
    print("le prix",dindon())



