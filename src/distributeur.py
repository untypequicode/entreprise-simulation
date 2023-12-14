class Distributeur:
    def __init__(self):
        self.__m_nom = ''
        self.__m_marge = 0
        self.__m_coefficient_augmentation = 0
        self.__m_droit_entree = 0

    def Begin(self, nom, marge, coefficient_augmentation, droit_entree):
        self.SetNom(nom)
        self.SetMarge(marge)
        self.SetCoefficientAugmentation(coefficient_augmentation)
        self.SetDroitEntree(droit_entree)

    def SetNom(self, nom):
        self.__m_nom = nom

    def SetMarge(self, marge):
        self.__m_marge = marge

    def SetCoefficientAugmentation(self, coefficient_augmentation):
        self.__m_coefficient_augmentation = coefficient_augmentation

    def SetDroitEntree(self, droit_entree):
        self.__m_droit_entree = droit_entree

    def GetNom(self):
        return self.__m_nom

    def GetMarge(self):
        return self.__m_marge

    def GetCoefficientAugmentation(self):
        return self.__m_coefficient_augmentation

    def GetDroitEntree(self):
        return self.__m_droit_entree

    def GetValeurs(self):
        return {'nom': self.GetNom(),
                'marge': self.GetMarge(),
                'coefficient_augmentation': self.GetCoefficientAugmentation(),
                'droit_entree': self.GetDroitEntree()}
