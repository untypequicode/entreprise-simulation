from entreprise import Entreprise

class Groupe:
    def __init__(self):
        self.entreprises = []

    def AjouterEntreprise(self, entreprise):
        self.entreprises.append(entreprise)

    def GetGagnant(self):
        gagnant = self.entreprises[0]
        for entreprise in self.entreprises[1:]:
            if entreprise.GetChiffreAffaire() > gagnant.GetChiffreAffaire():
                gagnant = entreprise
        return gagnant.GetValeurs()

    def GetEntreprises(self):
        return self.entreprises