class Produit:
    def __init__(self) -> None:
        """
        Initialise un objet Produit avec des valeurs par défaut.
        """
        self.SetNom('')
        self.SetInformations({})
        self.SetPrixDeVente(0)
        self.SetPrixFournisseur(0)
        self.SetBudgetPublicitaire(0)
        self.SetVentesEnvisagees(0)

    def Begin(self, nom: str, informations: dict, prix_de_vente: float, prix_fournisseur: float, budget_publicitaire: float, ventes_envisagees: int) -> None:
        """
        Initialise les valeurs du produit.

        Parameters :
        - nom (str) : Nom du produit.
        - informations (dict) : Informations sur le produit.
        - prix_de_vente (float) : Prix de vente du produit.
        - prix_fournisseur (float) : Prix d'achat du produit.
        - budget_publicitaire (float) : Budget publicitaire du produit.
        - ventes_envisagees (int) : Nombre de ventes envisagées du produit.
        """
        self.SetNom(nom)
        self.SetInformations(informations)
        self.SetPrixFournisseur(prix_fournisseur)
        self.SetPrixDeVente(max(self.GetPrixFournisseur(), prix_de_vente))
        self.SetBudgetPublicitaire(budget_publicitaire)
        self.SetVentesEnvisagees(max(self.GetBudgetPublicitaire() // self.GetPrixDeVente(), ventes_envisagees))

    def SetNom(self, nom: str) -> None:
        """
        Modifie le nom du produit.

        Parameters :
        - nom (str) : Nouveau nom du produit.
        """
        self.__m_nom = nom

    def SetInformations(self, informations: dict) -> None:
        """
        Modifie les informations du produit.

        Parameters :
        - informations (dict) : Nouvelles informations du produit.
        """
        self.__informations = informations

    def SetPrixDeVente(self, prix_de_vente: float) -> None:
        """
        Modifie le prix de vente du produit.

        Parameters :
        - prix_de_vente (float) : Nouveau prix de vente du produit.
        """
        self.__prix_de_vente = prix_de_vente

    def SetPrixFournisseur(self, prix_fournisseur: float) -> None:
        """
        Modifie le prix d'achat du produit.

        Parameters :
        - prix_fournisseur (float) : Nouveau prix d'achat du produit.
        """
        self.__prix_fournisseur = prix_fournisseur

    def SetBudgetPublicitaire(self, budget_publicitaire: float) -> None:
        """
        Modifie le budget publicitaire du produit.

        Parameters :
        - budget_publicitaire (float) : Nouveau budget publicitaire du produit.
        """
        self.__m_budget_publicitaire = budget_publicitaire

    def SetVentesEnvisagees(self, ventes_envisagees: int) -> None:
        """
        Modifie le nombre de ventes envisagées du produit.

        Parameters :
        - ventes_envisagees (int) : Nouveau nombre de ventes envisagées du produit.
        """
        self.__m_ventes_envisagees = ventes_envisagees

    def GetNom(self) -> str:
        """
        Récupère le nom du produit.

        Returns :
        - str : Nom du produit.
        """
        return self.__m_nom

    def GetInformations(self) -> dict:
        """
        Récupère les informations du produit.

        Returns :
        - dict : Informations du produit.
        """
        return self.__informations

    def GetPrixDeVente(self) -> float:
        """
        Récupère le prix de vente du produit.

        Returns :
        - float : Prix de vente du produit.
        """
        return self.__prix_de_vente

    def GetPrixFournisseur(self) -> float:
        """
        Récupère le prix d'achat du produit.

        Returns :
        - float : Prix d'achat du produit.
        """
        return self.__prix_fournisseur

    def GetBudgetPublicitaire(self) -> float:
        """
        Récupère le budget publicitaire du produit.

        Returns :
        - float : Budget publicitaire du produit.
        """
        return self.__m_budget_publicitaire

    def GetVentesEnvisagees(self) -> int:
        """
        Récupère le nombre de ventes envisagées du produit.

        Returns :
        - int : Nombre de ventes envisagées du produit.
        """
        return self.__m_ventes_envisagees

    def GetValeurs(self) -> dict:
        """
        Récupère toutes les valeurs du produit.

        Returns :
        - dict : Dictionnaire contenant les valeurs du produit.
        """
        return {'nom': self.GetNom(),
                'informations': self.GetInformations(),
                'prix_de_vente': self.GetPrixDeVente(),
                'prix_fournisseur': self.GetPrixFournisseur(),
                'budget_publicitaire': self.GetBudgetPublicitaire(),
                'ventes_envisagees': self.GetVentesEnvisagees()}

    def GetAchat(self) -> float:
        """
        Calcule le coût d'achat total du produit.

        Returns :
        - float : Coût d'achat total du produit.
        """
        return self.GetPrixFournisseur() * self.GetVentesEnvisagees()

    def GetVentes(self) -> float:
        """
        Calcule le chiffre d'affaires total généré par les ventes du produit.

        Returns :
        - float : Chiffre d'affaires total généré par les ventes du produit.
        """
        return self.GetVentesEnvisagees() * self.GetPrixDeVente()
