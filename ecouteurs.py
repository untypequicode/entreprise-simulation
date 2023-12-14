gamme_prix = {True: {'HQ': 5},
         False: {'LQ': 31.5, 'MQ': 36, 'HQ': 40.5}}

class Ecouteurs:
    def __init__(self, budget_publicitaire, prix_de_vente, ventes_envisagees, is_filaire = True, gamme = 'HQ'):
        self.is_filaire = is_filaire # filaire ou bluetooth
        if gamme in gamme_prix[self.is_filaire]:
            if self.is_filaire and gamme == 'HQ':
                self.gamme = gamme
            elif not self.is_filaire:
                self.gamme = gamme
        self.prix_fournisseur = gamme_prix[is_filaire][gamme]
        self.budget_publicitaire = budget_publicitaire
        self.prix_de_vente = max(prix_de_vente, self.prix_fournisseur)
        self.ventes_envisagees = max(ventes_envisagees, self.budget_publicitaire // self.prix_de_vente)

    # def GetPrix(self):
    #     return self.ventes_envisagees * (self.prix_de_vente - self.prix_fournisseur

    def GetPrix(self):
        return {'budget': self.budget_publicitaire, 'achat': self.prix_fournisseur * self.ventes_envisagees, 'ventes': self.ventes_envisagees, 'argent': self.prix_de_vente * self.ventes_envisagees}

    def GetValeurs(self):
        return {'is_filaire': self.is_filaire, 'gamme': self.gamme, 'prix_fournisseur': self.prix_fournisseur, 'budget_publicitaire': self.budget_publicitaire, 'prix_de_vente': self.prix_de_vente, 'ventes_envisagees': self.ventes_envisagees}