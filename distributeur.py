class Distributeur:
    def __init__(self, isA = True):
        self.Set(isA)

    def Set(self, isA):
        self.isA = isA
        if self.isA:
            self.nom = 'A'
            self.marge = 0.2
            self.coefficient_augmentation = 1
            self.droits_entree = 1000
        else:
            self.nom = 'B'
            self.marge = 0.2
            self.coefficient_augmentation = 1.2
            self.droits_entree = 5000000

    def GetValeurs(self):
        return {'nom': self.nom, 'isA': self.isA, 'marge': self.marge, 'coefficient_augmentation': self.coefficient_augmentation, 'droits_entree': self.droits_entree}