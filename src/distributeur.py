class Distributeur:
    def __init__(self):
        """
        Initialise un objet Distributeur avec des valeurs par défaut.
        """
        self.__m_nom = ''
        self.__m_marge = 0
        self.__m_coefficient_augmentation = 0
        self.__m_droit_entree = 0

    def Begin(self, nom, marge, coefficient_augmentation, droit_entree):
        """
        Initialise les valeurs du distributeur.

        Parameters:
        - nom (str): Nom du distributeur.
        - marge (float): Marge du distributeur.
        - coefficient_augmentation (float): Coefficient d'augmentation du distributeur.
        - droit_entree (int): Droit d'entrée du distributeur.
        """
        self.SetNom(nom)
        self.SetMarge(marge)
        self.SetCoefficientAugmentation(coefficient_augmentation)
        self.SetDroitEntree(droit_entree)

    def SetNom(self, nom):
        """
        Modifie le nom du distributeur.

        Parameters:
        - nom (str): Nouveau nom du distributeur.
        """
        self.__m_nom = nom

    def SetMarge(self, marge):
        """
        Modifie la marge du distributeur.

        Parameters:
        - marge (float): Nouvelle marge du distributeur.
        """
        self.__m_marge = marge

    def SetCoefficientAugmentation(self, coefficient_augmentation):
        """
        Modifie le coefficient d'augmentation du distributeur.

        Parameters:
        - coefficient_augmentation (float): Nouveau coefficient d'augmentation du distributeur.
        """
        self.__m_coefficient_augmentation = coefficient_augmentation

    def SetDroitEntree(self, droit_entree):
        """
        Modifie le droit d'entrée du distributeur.

        Parameters:
        - droit_entree (int): Nouveau droit d'entrée du distributeur.
        """
        self.__m_droit_entree = droit_entree

    def GetNom(self):
        """
        Récupère le nom du distributeur.

        Returns:
        - str: Nom du distributeur.
        """
        return self.__m_nom

    def GetMarge(self):
        """
        Récupère la marge du distributeur.

        Returns:
        - float: Marge du distributeur.
        """
        return self.__m_marge

    def GetCoefficientAugmentation(self):
        """
        Récupère le coefficient d'augmentation du distributeur.

        Returns:
        - float: Coefficient d'augmentation du distributeur.
        """
        return self.__m_coefficient_augmentation

    def GetDroitEntree(self):
        """
        Récupère le droit d'entrée du distributeur.

        Returns:
        - int: Droit d'entrée du distributeur.
        """
        return self.__m_droit_entree

    def GetValeurs(self):
        """
        Récupère toutes les valeurs du distributeur.

        Returns:
        - dict: Dictionnaire contenant les valeurs du distributeur.
        """
        return {'nom': self.GetNom(),
                'marge': self.GetMarge(),
                'coefficient_augmentation': self.GetCoefficientAugmentation(),
                'droit_entree': self.GetDroitEntree()}
