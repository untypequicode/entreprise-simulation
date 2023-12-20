from entreprise import Entreprise, Produit


class Marche:
    def __init__(self) -> None:
        """
        Initialise un objet Marche avec des valeurs par défaut.
        """
        self.SetTailleMarcheMax({})
        self.SetTailleMarche({})
        self.SetEntreprises([])

    def Begin(self, taille_marche_max: dict) -> None:
        """
        Initialise la taille maximale du marché.

        Parameters :
        - taille_marche_max (dict) : Taille maximale du marché pour chaque entreprise.
        """
        self.SetTailleMarcheMax(taille_marche_max)

    def SetTailleMarcheMax(self, taille_marche_max: dict or float, id: int = None) -> None:
        """
        Modifie la taille maximale du marché pour une entreprise spécifique ou pour l'ensemble du marché.

        Parameters :
        - taille_marche_max (dict or float) : Nouvelle taille maximale du marché.
        Si un dictionnaire est fourni, il doit contenir les tailles maximales pour chaque entreprise.
        - id (int or None) : Identifiant de l'entreprise pour laquelle la taille maximale doit être modifiée.
        Si None, la modification s'applique à l'ensemble du marché.
        """
        if id is not None:
            if id not in self.__m_taille_marche:
                self.__m_taille_marche[id] = 0
            self.__m_taille_marche_max = taille_marche_max[id]
        else:
            self.__m_taille_marche_max = taille_marche_max

    def GetTailleMarcheMax(self, id: int = None) -> float or dict:
        """
        Récupère la taille maximale du marché pour une entreprise spécifique ou pour l'ensemble du marché.

        Parameters :
        - id (int or None) : Identifiant de l'entreprise. Si None, la récupération s'applique à l'ensemble du marché.

        Returns :
        - float : Taille maximale du marché.
        """
        if id is not None:
            if id not in self.__m_taille_marche_max:
                self.__m_taille_marche_max[id] = 0
            return self.__m_taille_marche_max[id]
        else:
            return self.__m_taille_marche_max

    def SetTailleMarche(self, taille_marche: dict or float, id: int = None) -> None:
        """
        Modifie la taille actuelle du marché pour une entreprise spécifique ou pour l'ensemble du marché.

        Parameters :
        - taille_marche (dict or float) : Nouvelle taille du marché.
        Si un dictionnaire est fourni, il doit contenir les tailles pour chaque entreprise.
        - id (int or None) : Identifiant de l'entreprise pour laquelle la taille doit être modifiée.
        Si None, la modification s'applique à l'ensemble du marché.
        """
        if id is not None:
            if id not in self.__m_taille_marche_max:
                self.__m_taille_marche_max[id] = 0
            self.__m_taille_marche[id] = taille_marche
        else:
            self.__m_taille_marche = taille_marche

    def GetTailleMarche(self, id: int = None) -> float or dict:
        """
        Récupère la taille actuelle du marché pour une entreprise spécifique ou pour l'ensemble du marché.

        Parameters :
        - id (int or None) : Identifiant de l'entreprise. Si None, la récupération s'applique à l'ensemble du marché.

        Returns :
        - float : Taille actuelle du marché.
        """
        if id is not None:
            if id not in self.__m_taille_marche:
                self.__m_taille_marche[id] = 0
            return self.__m_taille_marche[id]
        else:
            return self.__m_taille_marche

    def SetEntreprises(self, entreprises: list) -> None:
        """
        Modifie la liste des entreprises sur le marché.

        Parameters :
        - entreprises (list) : Liste des entreprises.
        """
        self.__m_entreprises = entreprises

    def GetEntreprises(self) -> list:
        """
        Récupère la liste des entreprises sur le marché.

        Returns :
        - list : Liste des entreprises.
        """
        return self.__m_entreprises

    def GetNombreEntreprises(self) -> int:
        """
        Récupère le nombre d'entreprises sur le marché.

        Returns :
        - int : Nombre d'entreprises sur le marché.
        """
        return len(self.GetEntreprises())

    def GetEntreprise(self, index: int) -> Entreprise or None:
        """
        Récupère une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.

        Returns :
        - Entreprise : Entreprise spécifique.
        """
        return self.__m_entreprises[index]

    def AddEntreprise(self) -> None:
        """
        Ajoute une nouvelle entreprise au marché.
        """
        self.__m_entreprises.append(Entreprise())

    def RemoveEntreprise(self, index: int) -> None:
        """
        Supprime une entreprise spécifique du marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.
        """
        self.__m_entreprises.pop(index)

    def BeginEntreprise(self, index: int, nom: str, salaire: float, distributeur: list = None, produits: dict = None) -> None:
        """
        Initialise les valeurs d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.
        - nom (str) : Nom de l'entreprise.
        - distributeur (list) : Informations sur le distributeur de l'entreprise.
        - salaire (float) : Salaire de l'entreprise.
        - produits (dict or None) : Produits de l'entreprise. Si None, l'entreprise est créée sans produits.
        """
        self.GetEntreprise(index).Begin(nom, salaire, distributeur, produits)

    def SetNomEntreprise(self, index: int, nom: str) -> None:
        """
        Modifie le nom d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.
        - nom (str) : Nouveau nom de l'entreprise.
        """
        self.GetEntreprise(index).SetNom(nom)

    def SetProduitsEntreprise(self, index: int, produits: dict) -> None:
        """
        Modifie les produits d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.
        - produits (dict) : Nouveaux produits de l'entreprise.
        """
        self.GetEntreprise(index).SetProduits(produits)

    def SetDistributeurEntreprise(self, index: int, distributeur: list) -> None:
        """
        Modifie le distributeur d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.
        - distributeur (list) : Nouvelles informations sur le distributeur de l'entreprise.
        """
        self.GetEntreprise(index).SetDistributeur(distributeur)

    def SetSalairesEntreprise(self, index: int, salaires: float) -> None:
        """
        Modifie les salaires d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.
        - salaires (float) : Nouveaux salaires de l'entreprise.
        """
        self.GetEntreprise(index).SetSalaires(salaires)

    def GetNomEntreprise(self, index: int) -> str or None:
        """
        Récupère le nom d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.

        Returns :
        - str : Nom de l'entreprise.
        """
        return self.GetEntreprise(index).GetNom()

    def GetProduitsEntreprise(self, index: int) -> dict or None:
        """
        Récupère les produits d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.

        Returns :
        - dict : Produits de l'entreprise.
        """
        return self.GetEntreprise(index).GetProduits()

    def GetDistributeurEntreprise(self, index: int) -> list or None:
        """
        Récupère le distributeur d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.

        Returns :
        - Distributeur : Distributeur de l'entreprise.
        """
        return self.GetEntreprise(index).GetDistributeur()

    def GetSalairesEntreprise(self, index: int) -> float or None:
        """
        Récupère les salaires d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.

        Returns :
        - float : Salaires de l'entreprise.
        """
        return self.GetEntreprise(index).GetSalaires()

    def AddProduitEntreprise(self,
                             index: int,
                             id: str,
                             nom: str,
                             informations: dict,
                             prix_fournisseur: float,
                             prix_de_vente: float,
                             budget_publicitaire: int,
                             ventes_envisagees: int) -> None:
        """
        Ajoute un produit à une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.
        - id (int) : Identifiant du produit.
        - nom (str) : Nom du produit.
        - informations (dict) : Informations sur le produit.
        - prix_de_vente (float) : Prix de vente du produit.
        - prix_fournisseur (float) : Prix d'achat du produit.
        - budget_publicitaire (float) : Budget publicitaire du produit.
        - ventes_envisagees (int) : Nombre de ventes envisagées du produit.
        """
        ventes_envisagees = min(ventes_envisagees, self.GetTailleMarcheMax(nom) - self.GetTailleMarche(nom))
        self.SetTailleMarche(self.GetTailleMarche(nom) + ventes_envisagees, nom)
        self.GetEntreprise(index).AddProduit(id,
                                             nom,
                                             informations,
                                             prix_fournisseur,
                                             prix_de_vente,
                                             budget_publicitaire,
                                             ventes_envisagees)

    def RemoveProduitEntreprise(self, index: int, id: int, produit: Produit) -> None:
        """
        Supprime un produit d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.
        - id (int) : Identifiant du produit.
        - produit (Produit) : Produit à supprimer.
        """
        self.GetEntreprise(index).RemoveProduit(id, produit)

    def GetChiffreAffaireEntreprise(self, index: int) -> float or None:
        """
        Récupère le chiffre d'affaires d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.

        Returns :
        - float : Chiffre d'affaires de l'entreprise.
        """
        return self.GetEntreprise(index).GetChiffreAffaire()

    def SetChiffreAffaireEntreprise(self, index: int, chiffre_affaire: float) -> None:
        """
        Modifie le chiffre d'affaires d'une entreprise spécifique sur le marché.

        Parameters :
        - index (int) : Index de l'entreprise dans la liste.
        - chiffre_affaire (float) : Nouveau chiffre d'affaires de l'entreprise.
        """
        self.GetEntreprise(index).SetChiffreAffaire(chiffre_affaire)

    def GetGagnant(self) -> Entreprise or None:
        """
        Récupère l'entreprise ayant le plus grand chiffre d'affaires sur le marché.

        Returns :
        - Entreprise or None : Entreprise gagnante. Si aucune entreprise, renvoie None.
        """
        if self.GetNombreEntreprises() == 0:
            return None
        elif self.GetNombreEntreprises() == 1:
            return self.GetEntreprise(0)
        else:
            gagnant = self.GetEntreprise(0)
            for entreprise in self.GetEntreprises()[1:]:
                if entreprise.GetChiffreAffaire() > gagnant.GetChiffreAffaire():
                    gagnant = entreprise
            return gagnant
