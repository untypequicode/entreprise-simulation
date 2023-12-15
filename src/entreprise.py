from produit import Produit
from distributeur import Distributeur

class Entreprise:
    def __init__(self):
        """
        Initialise un objet Entreprise avec des valeurs par défaut.
        """
        self.__m_nom = ''
        self.__m_produits = {}
        self.__m_distributeur = Distributeur()
        self.__m_chiffre_affaire = 0
        self.__m_salaires = 0

    def Begin(self, nom, distributeur, salaire, produits=None):
        """
        Initialise les valeurs de l'entreprise.

        Parameters:
        - nom (str): Nom de l'entreprise.
        - distributeur (list): Informations sur le distributeur [nom, marge, coefficient_augmentation, droit_entree].
        - salaire (int): Coût des salaires de l'entreprise.
        - produits (dict): Produits de l'entreprise (facultatif).
        """
        self.SetNom(nom)
        self.SetDistributeur(distributeur)
        self.SetSalaires(salaire)
        if produits is not None:
            self.SetProduits(produits)

    def SetNom(self, nom):
        """
        Modifie le nom de l'entreprise.

        Parameters:
        - nom (str): Nouveau nom de l'entreprise.
        """
        self.__m_nom = nom

    def SetProduits(self, produits):
        """
        Modifie la liste des produits de l'entreprise.

        Parameters:
        - produits (dict): Nouvelle liste des produits de l'entreprise.
        """
        self.__m_produits = produits

    def SetDistributeur(self, distributeur):
        """
        Initialise les valeurs du distributeur de l'entreprise.

        Parameters:
        - distributeur (list): Informations sur le distributeur [nom, marge, coefficient_augmentation, droit_entree].
        """
        self.__m_distributeur.Begin(distributeur[0], distributeur[1], distributeur[2], distributeur[3])

    def SetSalaires(self, salaires):
        """
        Modifie le coût des salaires de l'entreprise.

        Parameters:
        - salaires (int): Nouveau coût des salaires de l'entreprise.
        """
        self.__m_salaires = salaires

    def GetNom(self):
        """
        Récupère le nom de l'entreprise.

        Returns:
        - str: Nom de l'entreprise.
        """
        return self.__m_nom

    def GetProduits(self):
        """
        Récupère la liste des produits de l'entreprise.

        Returns:
        - dict: Liste des produits de l'entreprise.
        """
        return self.__m_produits

    def GetDistributeur(self):
        """
        Récupère les informations sur le distributeur de l'entreprise.

        Returns:
        - Distributeur: Objet Distributeur associé à l'entreprise.
        """
        return self.__m_distributeur

    def GetSalaires(self):
        """
        Récupère le coût des salaires de l'entreprise.

        Returns:
        - int: Coût des salaires de l'entreprise.
        """
        return self.__m_salaires

    def AddProduit(self, id, nom, informations, prix_de_vente, prix_fournisseur, budget_publicitaire, ventes_envisagees):
        """
        Ajoute un produit à la liste des produits de l'entreprise.

        Parameters:
        - id (str): Identifiant du produit.
        - nom (str): Nom du produit.
        - informations (dict): Informations sur le produit.
        - prix_de_vente (float): Prix de vente du produit.
        - prix_fournisseur (float): Prix d'achat du produit.
        - budget_publicitaire (int): Budget publicitaire du produit.
        - ventes_envisagees (int): Nombre de ventes envisagées du produit.
        """
        if id not in self.__m_produits:
            self.__m_produits[id] = []
        produit_temp = Produit()
        produit_temp.Begin(nom, informations, prix_de_vente, prix_fournisseur, budget_publicitaire, ventes_envisagees)
        if produit_temp not in self.__m_produits[id]:
            self.__m_produits[id].append(produit_temp)

    def RemoveProduit(self, id, produit):
        """
        Supprime un produit de la liste des produits de l'entreprise.

        Parameters:
        - id (str): Identifiant du produit.
        - produit (Produit): Objet Produit à supprimer.
        """
        if id in self.__m_produits:
            if produit in self.__m_produits[id]:
                self.__m_produits[id].remove(produit)

    def GetChiffreAffaire(self):
        """
        Récupère le chiffre d'affaires de l'entreprise.

        Returns:
        - float: Chiffre d'affaires de l'entreprise.
        """
        self.SetChiffreAffaire()
        return self.__m_chiffre_affaire

    def SetChiffreAffaire(self):
        """
        Calcule et met à jour le chiffre d'affaires de l'entreprise.
        """
        self.__m_chiffre_affaire = 0
        for id in self.__m_produits:
            for produit in self.__m_produits[id]:
                self.__m_chiffre_affaire += produit.GetVentesEnvisagees() * produit.GetPrixDeVente() - (produit.GetBudgetPublicitaire() + produit.GetPrixFournisseur() * produit.GetVentesEnvisagees() + produit.GetVentesEnvisagees() * produit.GetPrixDeVente() * self.__m_distributeur.GetMarge())
        self.__m_chiffre_affaire -= self.__m_distributeur.GetDroitEntree() + self.GetSalaires()
        self.__m_chiffre_affaire = max(self.__m_chiffre_affaire, -1)
        self.__m_chiffre_affaire -= self.__m_distributeur.GetDroitEntree()
