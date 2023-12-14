from ecouteurs import Ecouteurs
from distributeur import Distributeur

class Entreprise:
    def __init__(self, nom, gamme = 'HQ', is_a = True, valeur_filaire = [0, 0, 0], valeur_bluetooth = [0, 0, 0]):
        self.nom = nom
        self.ecouteurs = {True: Ecouteurs(valeur_filaire[0], valeur_filaire[1], valeur_filaire[2], True),
                          False: Ecouteurs(valeur_bluetooth[0], valeur_bluetooth[1], valeur_bluetooth[2], False, gamme)}
        self.distributeur = Distributeur(is_a)
        self.chiffre_affaire = 0

    def GetChiffreAffaire(self):
        self.chiffre_affaire = 0
        for type in self.ecouteurs:
            # self.chiffre_affaire += self.ecouteurs[type].GetPrix() * self.distributeur.coefficient_augmentation * (1 - self.distributeur.marge) - self.ecouteurs[type].GetPrix()[1]
            self.chiffre_affaire += self.ecouteurs[type].GetPrix()['argent'] - (self.ecouteurs[type].GetPrix()['budget'] + self.ecouteurs[type].GetPrix()['achat'] + self.ecouteurs[type].GetPrix()['argent'] * (self.distributeur.marge))
        self.chiffre_affaire -= self.distributeur.droits_entree + 360000
        self.chiffre_affaire = max(self.chiffre_affaire, -1)
        return self.chiffre_affaire

    def GetValeurs(self):
        self.GetChiffreAffaire()
        return {'nom': self.nom, 'ecouteurs': {True: self.ecouteurs[True].GetValeurs(), False: self.ecouteurs[False].GetValeurs()}, 'distributeur': self.distributeur.GetValeurs(), 'chiffre_affaire': self.chiffre_affaire}