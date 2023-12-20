from marche import Marche, Entreprise


class Simulation:
    def __init__(self):
        pass

    def Begin(self, taille_marche_max: dict, nombre_entreprises: int, salaire: int) -> None:
        self.SetMarche(Marche())
        self.BeginMarche(taille_marche_max)
        self.SetNombreEntreprises(nombre_entreprises)
        self.SetSalaires(salaire)

    def SetMarche(self, marche: Marche) -> None:
        self.__marche = marche

    def GetMarche(self) -> Marche:
        return self.__marche

    def BeginMarche(self, taille_marche_max: dict) -> None:
        self.__marche.Begin(taille_marche_max)

    def SetNombreEntreprises(self, nombre_entreprises: int) -> None:
        self.__nombre_entreprises = nombre_entreprises

    def GetNombreEntreprises(self) -> int:
        return self.__nombre_entreprises

    def SetSalaires(self, salaire: int) -> None:
        self.__salaires = salaire

    def GetSalaires(self) -> int:
        return self.__salaires

    def Simuler(self) -> None:
        with open('data.csv', 'w') as f:
            f.write('nom;chiffre_affaire;salaires;distributeur;marge;coefficient_augmentation;droit_entree;produits\n')
            
        possibilites = 1
        for distributeur_variation in self.__distributeur_variation:
            possibilites *= max(1, len(distributeur_variation))
        for produit_variation in self.__produit_variation:
            if "informations" in produit_variation:
                for elem in produit_variation["informations"]:
                    possibilites *= max(1, len(produit_variation["informations"][elem]))
            if "prix_fournisseur" in produit_variation:
                possibilites *= max(1, len(produit_variation["prix_fournisseur"]))
            for elem in ["budget_publicitaire", "budget_publicitaire", "ventes_envisagees"]:
                if elem in produit_variation:
                    if type(produit_variation[elem]) == list and len(produit_variation[elem]) == 3:
                        possibilites *= max(1, abs(produit_variation[elem][1] - produit_variation[elem][0]) // max(produit_variation[elem][2], 1))
        print(possibilites, possibilites**self.GetNombreEntreprises())
            
        produits = [{"id": "",
                     "nom": "",
                     "informations": {},
                     "prix_fournisseur": 0,
                     "prix_de_vente": 0,
                     "budget_publicitaire": 0,
                     "ventes_envisagees": 0}
                    for i in range(min(len(self.__produit_variation), len(self.__produit_fixe)))]
        for distributeur_variation in self.__distributeur_variation:
            for i_produit_variation in range(min(len(self.__produit_variation), len(self.__produit_fixe))):
                pass
                while self.__marche.GetNombreEntreprises() > 0:
                    self.__marche.RemoveEntreprise(0)
                for i_entreprise in range(self.GetNombreEntreprises()):
                    self.__marche.AddEntreprise()
                    self.__marche.BeginEntreprise(-1, f'Entreprise {i_entreprise}', self.GetSalaires(), distributeur_variation)
                    for i_produit_fixe in range(min(len(self.__produit_variation), len(self.__produit_fixe))):
                        for elem in ["id",
                                     "nom",
                                     "informations",
                                     "prix_fournisseur",
                                     "prix_de_vente",
                                     "budget_publicitaire",
                                     "ventes_envisagees"]:
                            if elem in self.__produit_fixe[i_produit_fixe]:
                                produits[i_produit_fixe][elem] = self.__produit_fixe[i_produit_fixe][elem]
                        self.__marche.AddProduitEntreprise(-1,
                                                           produits[i_produit_fixe]["id"],
                                                           produits[i_produit_fixe]["nom"],
                                                           produits[i_produit_fixe]["informations"],
                                                           produits[i_produit_fixe]["prix_fournisseur"],
                                                           produits[i_produit_fixe]["prix_de_vente"],
                                                           produits[i_produit_fixe]["budget_publicitaire"],
                                                           produits[i_produit_fixe]["ventes_envisagees"])
                    if i_entreprise == self.GetNombreEntreprises() - 1:
                            self.__SaveGagnant(self.__marche.GetGagnant())

    def __SaveGagnant(self, gagnant) -> None:
        with open('data.csv', 'a') as f:
            f.write(f'{gagnant.GetNom()};'
                    f'{gagnant.GetChiffreAffaire()};'
                    f'{gagnant.GetSalaires()};'
                    f'{gagnant.GetDistributeur().GetNom()};'
                    f'{gagnant.GetDistributeur().GetMarge()};'
                    f'{gagnant.GetDistributeur().GetCoefficientAugmentation()};'
                    f'{gagnant.GetDistributeur().GetDroitEntree()};'
                    f'{gagnant.GetProduits()}\n')

    def BeginSimulation(self, distributeur_variation, produit_fixe, produit_variation) -> None:
        self.__distributeur_variation = distributeur_variation
        self.__produit_fixe = produit_fixe
        self.__produit_variation = produit_variation