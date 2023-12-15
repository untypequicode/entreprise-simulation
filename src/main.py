from groupe import Groupe, Entreprise
import time


# groupes_gagnants = []
#
# def AddTest(valeur_filaire2, valeur_bluetooth2):
#     index = 0
#     valeur_filaire0 = 0
#     valeur_bluetooth0 = 0
#     for gamme in ['HQ', 'MQ', 'LQ']:
#         for distributeur in [True, False]:
#             # for valeur_filaire0 in range(0, 1000000, 100000):
#             for valeur_filaire1 in range(0, 300, 10):
#                         # for valeur_bluetooth0 in range(0, 1000000, 100000):
#                     for valeur_bluetooth1 in range(0, 300, 10):
#                         cas_possible = {'gamme': gamme, 'distributeur': distributeur, 'valeur_filaire': [valeur_filaire0, valeur_filaire1, valeur_filaire2], 'valeur_bluetooth': [valeur_bluetooth0, valeur_bluetooth1, valeur_bluetooth2]}
#                         groupes[index].AjouterEntreprise(Entreprise('test', cas_possible['gamme'], cas_possible['distributeur'], cas_possible['valeur_filaire'], cas_possible['valeur_bluetooth']))
#                         # if index % 100 == 0:
#                         # print(index)
#                         index += 1
#
# index = 0
# start = time.time()
# for a_valeur_filaire2 in range(0, min(800000, 800000//4), 5000):
#     for a_valeur_bluetooth2 in range(0, min(300000, 300000//4), 5000):
#         for b_valeur_filaire2 in range(0, min(800000 - a_valeur_filaire2, 800000//4), 5000):
#             for b_valeur_bluetooth2 in range(0, min(300000 - a_valeur_bluetooth2, 300000//4), 5000):
#                 for c_valeur_filaire2 in range(0, min(800000 - a_valeur_filaire2 - b_valeur_filaire2, 800000//4), 5000):
#                     for c_valeur_bluetooth2 in range(0, min(300000 - a_valeur_bluetooth2 - b_valeur_bluetooth2, 300000//4), 5000):
#                         for d_valeur_filaire2 in range(0, min(800000 - a_valeur_filaire2 - b_valeur_filaire2 - c_valeur_filaire2, 800000//4), 5000):
#                             for d_valeur_bluetooth2 in range(0, min(300000 - a_valeur_bluetooth2 - b_valeur_bluetooth2 - c_valeur_bluetooth2, 300000//4), 5000):
#                                 for e_valeur_filaire2 in range(0, min(800000 - a_valeur_filaire2 - b_valeur_filaire2 - c_valeur_filaire2 - d_valeur_filaire2, 800000//4), 5000):
#                                     for e_valeur_bluetooth2 in range(0, min(300000 - a_valeur_bluetooth2 - b_valeur_bluetooth2 - c_valeur_bluetooth2 - d_valeur_bluetooth2, 300000//4), 5000):
#                                         for f_valeur_filaire2 in range(0, min(800000 - a_valeur_filaire2 - b_valeur_filaire2 - c_valeur_filaire2 - d_valeur_filaire2 - e_valeur_filaire2, 800000//4), 5000):
#                                             for f_valeur_bluetooth2 in range(0, min(300000 - a_valeur_bluetooth2 - b_valeur_bluetooth2 - c_valeur_bluetooth2 - d_valeur_bluetooth2 - e_valeur_bluetooth2, 300000//4), 5000):
#                                                 for g_valeur_filaire2 in range(0, min(800000 - a_valeur_filaire2 - b_valeur_filaire2 - c_valeur_filaire2 - d_valeur_filaire2 - e_valeur_filaire2 - f_valeur_filaire2, 800000//4), 5000):
#                                                     for g_valeur_bluetooth2 in range(0, min(300000 - a_valeur_bluetooth2 - b_valeur_bluetooth2 - c_valeur_bluetooth2 - d_valeur_bluetooth2 - e_valeur_bluetooth2 - f_valeur_bluetooth2, 300000//4), 5000):
#                                                         for h_valeur_filaire2 in range(0, min(800000 - a_valeur_filaire2 - b_valeur_filaire2 - c_valeur_filaire2 - d_valeur_filaire2 - e_valeur_filaire2 - f_valeur_filaire2 - g_valeur_filaire2, 800000//4), 5000):
#                                                             for h_valeur_bluetooth2 in range(0, min(300000 - a_valeur_bluetooth2 - b_valeur_bluetooth2 - c_valeur_bluetooth2 - d_valeur_bluetooth2 - e_valeur_bluetooth2 - f_valeur_bluetooth2 - g_valeur_bluetooth2, 300000//4), 5000):
#                                                                 groupes = []
#                                                                 for i in range(3*2*30*30):
#                                                                     groupes.append(Groupe())
#                                                                 AddTest(a_valeur_filaire2, a_valeur_bluetooth2)
#                                                                 AddTest(b_valeur_filaire2, b_valeur_bluetooth2)
#                                                                 AddTest(c_valeur_filaire2, c_valeur_bluetooth2)
#                                                                 AddTest(d_valeur_filaire2, d_valeur_bluetooth2)
#                                                                 AddTest(e_valeur_filaire2, e_valeur_bluetooth2)
#                                                                 AddTest(f_valeur_filaire2, f_valeur_bluetooth2)
#                                                                 AddTest(g_valeur_filaire2, g_valeur_bluetooth2)
#                                                                 AddTest(h_valeur_filaire2, h_valeur_bluetooth2)
#                                                                 for i in range(3*2*30*30):
#                                                                     gagnant = groupes[i].GetGagnant()
#                                                                     if gagnant['chiffre_affaire'] >= 0:
#                                                                         groupes_gagnants.append(groupes[i].GetGagnant())
#                                                                         # print(groupes_gagnants[-1])
#                                                                 print(a_valeur_filaire2, a_valeur_bluetooth2, b_valeur_filaire2, b_valeur_bluetooth2, c_valeur_filaire2, c_valeur_bluetooth2, d_valeur_filaire2, d_valeur_bluetooth2, e_valeur_filaire2, e_valeur_bluetooth2, f_valeur_filaire2, f_valeur_bluetooth2, g_valeur_filaire2, g_valeur_bluetooth2, h_valeur_filaire2, h_valeur_bluetooth2, time.time() - start, len(groupes_gagnants), len(groupes_gagnants)*3*2*30*30)
#                                                                 index +=1
#
# print(index*3*2*30*30)
# print(time.time() - start)
#
# for gagnant_ref in groupes_gagnants:
#     print(gagnant_ref)

# Initialisation des valeurs pour les distributeurs et les gammes de prix
distrib_a = ['A', 0.2, 1, 1000]
distrib_b = ['B', 0.2, 1.2, 5000000]

gamme_prix = {True: {'HQ': 5},
              False: {'LQ': 31.5, 'MQ': 36, 'HQ': 40.5}}

# Création d'une entreprise et ajout de produits
a = Entreprise()
a.Begin("AeroBeats", distrib_a, 360000)
a.AddProduit("ecouteurs",
             "Ecouteurs filaires",
             {'is_filaire': True, 'gamme': 'MQ'},
             7.5, gamme_prix[True]['HQ'],
             30000,
             120000)
a.AddProduit("ecouteurs",
             "Ecouteurs bluetooth",
             {'is_filaire': False, 'gamme': 'MQ'},
             75, gamme_prix[False]['MQ'],
             100000,
             38000)

# Affichage du chiffre d'affaires total de l'entreprise
print(a.GetChiffreAffaire())