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

class Produit:
    def __int__(self):
        self.__m_nom = ''
        self.__informations = {}
        self.__prix_de_vente = 0
        self.__prix_fournisseur = 0
        self.__m_budget_publicitaire = 0
        self.__m_ventes_envisagees = 0

    def Begin(self, nom, informations, prix_de_vente, prix_fournisseur, budget_publicitaire, ventes_envisagees):
        self.SetNom(nom)
        self.SetInformations(informations)
        self.SetPrixDeVente(prix_de_vente)
        self.SetPrixFournisseur(prix_fournisseur)
        self.SetBudgetPublicitaire(budget_publicitaire)
        self.SetVentesEnvisagees(ventes_envisagees)

    def SetNom(self, nom):
        self.__m_nom = nom

    def SetInformations(self, informations):
        self.__informations = informations

    def SetPrixDeVente(self, prix_de_vente):
        self.__prix_de_vente = prix_de_vente

    def SetPrixFournisseur(self, prix_fournisseur):
        self.__prix_fournisseur = prix_fournisseur

    def SetBudgetPublicitaire(self, budget_publicitaire):
        self.__m_budget_publicitaire = budget_publicitaire

    def SetVentesEnvisagees(self, ventes_envisagees):
        self.__m_ventes_envisagees = ventes_envisagees

    def GetNom(self):
        return self.__m_nom

    def GetInformations(self):
        return self.__informations

    def GetPrixDeVente(self):
        return self.__prix_de_vente

    def GetPrixFournisseur(self):
        return self.__prix_fournisseur

    def GetBudgetPublicitaire(self):
        return self.__m_budget_publicitaire

    def GetVentesEnvisagees(self):
        return self.__m_ventes_envisagees

    def GetValeurs(self):
        return {'nom': self.GetNom(),
                'informations': self.GetInformations(),
                'prix_de_vente': self.GetPrixDeVente(),
                'prix_fournisseur': self.GetPrixFournisseur(),
                'budget_publicitaire': self.GetBudgetPublicitaire(),
                'ventes_envisagees': self.GetVentesEnvisagees()}
