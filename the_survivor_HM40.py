#Lancement du module pygame et importation des différents modules d'interface du jeu
import pygame

#Importation de packages essentiels à notre backend
import time
import re
import datetime
import types                    #Utile pour "SimpleNamespace"
from random import*
import os

#Import de nos class externes (traduction et outils d'interface (slider, boutton V2...) )
from fr import fr
from en import en
import button as BUTTON
import Slider


####################################Initialisation de nombreuses variables globales##############################################

vec = pygame.math.Vector2                  #initialisation du module vecteur
pygame.mixer.init(frequency=48000, size=-16, channels=1, buffer=1024)            #initialisation du module mixer de pygame

#initialisation de couleurs avec les valeurs RGB (250=max et 0=min)

black = (0,0,0)
white = (250,250,250)
rouge = (250,0,0)
bordeaux = (159,0,0)
vert = (183,253,233)
rouge_pale = (255,207,108)
bleu_ardoise = (104, 111, 140)
violet_fonce = (63,0,63)
violet_clair = (191,0,191)
rouge_fonce = (75,0,0)
rouge_clair= (175,0,0)
bleu_fonce = (0,0,75)
bleu_clair = (0,0,175)
marron_fonce = (117,55,0)
marron_clair = (255,165,0)
marron = (153,51,0)
orange_fonce = (255,90,0)
orange_clair = (255,165,0)
vert_fonce = (0,75,0)
vert_clair = (0,175,0)
jaune_fonce = (75,75,0)
jaune_clair = (175,175,0)
bleu_fonce2 = (17,72,69)
bleu_clair2 = (38,168,159)
vert_fonce2 = (37,72,17)
vert_clair2 = (88,154,44)
gris_fonce = (100,100,100)
gris_clair = (175,175,175)
vertpanneau = (60,138,116)
orange = (255,184,0)

#Création des variables global de backend du programme
fenetreL= 1000
fenetreH= 560
FPS = 40
ennemie_acc = 0.8
perso_acc = 2.5
perso_friction = -0.2
perso_gravite = 1.8
ennemie_gravite = 0.3

#Création des variables global de traduction du frontend de notre programme
text1 = ''
text2 = ''
text3 = ''
text4 = ''
regle1_2 = ''
regle1_3 = ''
regle1_4 = ''
regle1_5 = ''
regle1_6 = ''
regle1_7 = ''
regle1_8 = ''
regle1_9 = ''
regle1_10 = ''
regle1_11 = ''
regle1_12 = ''
regle1_13 = ''
regle1_14 = ''
regle1_15 = ''
regle1_16 = ''
regle1_17 = ''
regle2_2 = ''
regle2_3 = ''
regle2_4 = ''
regle2_5 = ''
regle2_6 = ''
regle2_7 = ''
regle2_8 = ''
regle2_9 = ''
regle3_1 = ''
espace = ''
t1 = ''
t1bis = ''
t2 = ''
t2bis = ''
t3 = ''
regle4_1 = ''
regle4_2 = ''
regle4_3 = ''
regle4_4 = ''
regle4_5 = ''
regle4_6 = ''
regle4_7 = ''
regle4_8 = ''
regle4_9 = ''
regle4_10 = ''
regle4_11 = ''
regle4_12 = ''
regle4_13 = ''
regle4_14 = ''
regle4_15 = ''
regle4_16 = ''
regle4_17 = ''
regle4_18 = ''
regle4_19 = ''
regle4_20 = ''
regle4_21 = ''
regle4_22 = ''
Regle = ''
Start = ''
Option = ''
Credits = ''
Facile = ''
Moyen = ''
Difficile = ''
Son = ''
Music = ''
Commandes = ''
Score1 = ''
Score2 = ''
Score3 = ''
Score4 = ''
Score5 = ''
Score6 = ''
Score7 = ''
Score8 = ''
credits1 = ''
credits2 = ''
credits3 = ''
credits4 = ''
credits5 = ''
credit6 = ''
credits7 = ''
credits8 = ''
GO = ''
com = ''
retour = ''
rejouer = ''
Reprendre = ''
Recommencer = ''
Retour_menu2 = ''
menu1 = ''
Rejouer2 = ''
win = ''
win1 = ''
win2 = ''
win3 = ''
win4 = ''
win5 = ''
win6 = ''
win7 = ''
win8 = ''
win9 = ''
win10 = ''
win11 = ''
win12 =''
jauge = ''
d_b1 = ''
d_b1bis = ''
d_b2 = ''
d_b2bis = ''
d_b3 = ''
d_b3bis = ''

##########################################début de création des class########################################################

#Class utile à la traduction de notre frontend
class NestedNamespace(types.SimpleNamespace):
    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__setattr__(key, NestedNamespace(value))
            else:
                self.__setattr__(key, value)

text = {}
text.update({"fr": NestedNamespace(fr)})
text.update({"en": NestedNamespace(en)})

#Class personnage (celui que nous allons jouer)
class personnage(pygame.sprite.Sprite):
    def __init__(self, jeu,x,y):                                                  #Fonction créatrice des propriétés du personnage et de sa représentation
        pygame.sprite.Sprite.__init__(self)                                       #On appelle le constructeur parent des entités nommées "sprites" (utile quand on a besoin de coller qq chose sur notre fenetre qui doit intéragir)
        self.jeu = jeu                                                            #on met ici le personnage au courant de ce que le jeu à, soit les entités qui l'entourent
        self.image= pygame.image.load("Sprite/Stand.png").convert_alpha()         #on charge une image dans une variable
        self.rect = pygame.Rect(x, y, 50, 58)                                     #on crée un rectangle autour de notre surface qui servira de hitbox
        self.pos_playeur = self.image.get_rect()
        self.persoL = 50                                                          #Création de deux variables, matérialisant longueur et hauteur du personnage (ses dimensions au besoin)
        self.persoH = 58
        self.pos = vec(fenetreL/2,fenetreH/2)                                     #vecteur position du personnage, dont les premières coordonnées sont le centre de l'écran
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.saut = False
        self.avancer = True
        self.sprint = False
        self.compteur_marche = 0                                                  #on crée un compteur qui va nous permettre de contrôler la rapidité d'enchaînement des images d'animation

        marcheD1 = pygame.image.load('Sprite/D1.png')
        marcheD2 = pygame.image.load('Sprite/D2.png')
        marcheD3 = pygame.image.load('Sprite/D3.png')
        marcheD4 = pygame.image.load('Sprite/D4.png')
        marcheD5 = pygame.image.load('Sprite/D5.png')
        marcheD6 = pygame.image.load('Sprite/D6.png')
        marcheD7 = pygame.image.load('Sprite/D7.png')
        marcheD8 = pygame.image.load('Sprite/D8.png')
        marcheD9 = pygame.image.load('Sprite/D9.png')
        self.marcheD=[marcheD1,marcheD2,marcheD3,marcheD4,marcheD5,marcheD6,marcheD7,marcheD8,marcheD9]
                                                                                 #on charge et stocke les images relatives à l'animation du personnage
        marcheG1 = pygame.image.load('Sprite/G1.png')
        marcheG2 = pygame.image.load('Sprite/G2.png')
        marcheG3 = pygame.image.load('Sprite/G3.png')
        marcheG4 = pygame.image.load('Sprite/G4.png')
        marcheG5 = pygame.image.load('Sprite/G5.png')
        marcheG6 = pygame.image.load('Sprite/G6.png')
        marcheG7 = pygame.image.load('Sprite/G7.png')
        marcheG8 = pygame.image.load('Sprite/G8.png')
        marcheG9 = pygame.image.load('Sprite/G9.png')
        self.marcheG=[marcheG1,marcheG2,marcheG3,marcheG4,marcheG5,marcheG6,marcheG7,marcheG8,marcheG9]

    def sauter (self):
        self.rect.x+=1
        collision1=pygame.sprite.spritecollide(self,self.jeu.platformes,False)    #on vérifie ici que le joueur ne va pas sauter dans le vide
        self.rect.x-=1
        if collision1 and not self.saut:
            self.saut = True
            self.vel.y = -28                                                      #cette partie de la fonction donne la vitesse nécessaire au saut

    def saut_court(self):
        if self.saut :                                                            #on enclenche le saut court lorsque le personnage a au moins sauté 5 pixels
            if self.vel.y <-5:
                self.vel.y = -5


    #on initialise ses mouvements et on les mets à jour
    def update(self):
        self.acc = vec(0,perso_gravite)                                          #création du vecteur accélération du personnage, sans accélération en x, mais subissant la gravité en y (d'où ici o.5)

        if Jeu.ZQSD :
            A=pygame.K_d
            B=pygame.K_q
        else:
            A=pygame.K_RIGHT
            B=pygame.K_LEFT

        keys = pygame.key.get_pressed()                                          #une variable prend en son sein toutes les touches pressées, ici keys

        if not self.sprint :
            if keys[A]:                                                #on fait avancer ou reculer notre personnage en fonction de la touche pressées, en modifiant son accélération en x

                self.acc.x= perso_acc
                self.image = self.marcheD[self.compteur_marche//3]
                self.compteur_marche+=1
                self.jeu.fond_x-= 1
                self.jeu.fond2_x-= 1
                self.jeu.fond3_x-= 1
                                                                                    #pour chaque direction, on modifie l'allure du personnage (compteur) et fait avancer les fonds dans le sens inverse
            elif keys[B]:

                self.acc.x= -perso_acc
                self.image = self.marcheG[self.compteur_marche//3]
                self.compteur_marche+=1
                self.jeu.fond_x-= -1
                self.jeu.fond2_x-= -1
                self.jeu.fond3_x-= -1

            else:
                if self.avancer :
                    self.image= pygame.image.load("Sprite/Stand.png")
                    self.compteur_marche=0
                    self.jeu.fond_x-= 0
                    self.jeu.fond2_x-= 0
                    self.jeu.fond3_x-= 0

        else :
            self.acc.x+=3.5
            self.image = self.marcheD[self.compteur_marche//3]
            self.compteur_marche+=1
                                                                                 #formules physiques, permettant le calcul de la nouvelle position en fonction de la modification des paramètres accélération et vitesse (acc et vel)
        self.acc.x+=self.vel.x*perso_friction                                    #l'ajout de ses formules permet d'accroitre le réalisme des mouvements, notamment avec l'intégration de frixions
        self.vel += self.acc
        if self.avancer :
            self.pos+=self.vel+0.5*self.acc

        self.rect.midbottom = self.pos                                           #placement des pieds du personnage, au niveau de ce que l'on a définit comme son vecteur position, et que l'on a précédemment modifié

        if self.compteur_marche+1 >=27:                                          #on donne au compteur un maximum de 27 : chacune des 9 images reste 3 ms avant de changer
            self.compteur_marche = 0

#Class des ennemies du jeux (les marcheurs noir)
class ennemie(pygame.sprite.Sprite):
    def __init__(self,jeu,personnage,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.jeu = jeu
        self.personnage = personnage                                             #on met ici le personnage au courant de ce que le jeu à, soit les entités qui l'entourent
        self.image= pygame.image.load("Sprite/Ennemiestart.png").convert_alpha()    #on charge une image dans une variable
        self.rect = pygame.Rect(x, y, 90, 90)                                    #on crée un rectangle autour de notre surface qui servira de hitbox
        self.gravite = ennemie_gravite
        self.pos_ennemie = self.image.get_rect()
        self.persoL = 50                                                          #Création de deux varibales, matérialisant longueur et hauteur du personnage (ses dimensions)
        self.persoH = 60
        self.pos = vec(x,y)                                                       #vecteur position du personnage
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.tempdespawnH = randint(5,10)
        self.tempdespawnR = 0
        self.tempsreel = 0
        self.Rsens = self.jeu.Rsens
        self.mort = False
        self.spawn = True
        self.sol = False
        self.compteur_despawn = 0
        self.compteur_marche = 0
        self.compteur_spawn = 0
        self.tempdespawnR = 0

        self.spawnG=[pygame.image.load('Sprite/EnnemieG1.png'),pygame.image.load('Sprite/EnnemieG2.png'),pygame.image.load('Sprite/EnnemieG3.png'),pygame.image.load('Sprite/EnnemieG4.png'),pygame.image.load('Sprite/EnnemieG5.png'),pygame.image.load('Sprite/EnnemieG6.png'),pygame.image.load('Sprite/EnnemieG7.png'),pygame.image.load('Sprite/EnnemieG8.png'),pygame.image.load('Sprite/EnnemieG9.png'),pygame.image.load('Sprite/EnnemieG10.png'),
                      pygame.image.load('Sprite/EnnemieG11.png'),pygame.image.load('Sprite/EnnemieG12.png'),pygame.image.load('Sprite/EnnemieG13.png'),pygame.image.load('Sprite/EnnemieG14.png'),pygame.image.load('Sprite/EnnemieG15.png'),pygame.image.load('Sprite/EnnemieG16.png'),pygame.image.load('Sprite/EnnemieG17.png'),pygame.image.load('Sprite/EnnemieG18.png'),pygame.image.load('Sprite/EnnemieG19.png'),pygame.image.load('Sprite/EnnemieG20.png'),]
        self.marcheG=[pygame.image.load('Sprite/EnnemieG21.png'),pygame.image.load('Sprite/EnnemieG22.png'),pygame.image.load('Sprite/EnnemieG23.png'),pygame.image.load('Sprite/EnnemieG24.png'),pygame.image.load('Sprite/EnnemieG25.png'),pygame.image.load('Sprite/EnnemieG26.png'),pygame.image.load('Sprite/EnnemieG27.png'),pygame.image.load('Sprite/EnnemieG28.png'),pygame.image.load('Sprite/EnnemieG29.png'),pygame.image.load('Sprite/EnnemieG30.png'),
                      pygame.image.load('Sprite/EnnemieG31.png'),pygame.image.load('Sprite/EnnemieG32.png'),pygame.image.load('Sprite/EnnemieG33.png'),pygame.image.load('Sprite/EnnemieG34.png'),pygame.image.load('Sprite/EnnemieG35.png'),pygame.image.load('Sprite/EnnemieG36.png'),pygame.image.load('Sprite/EnnemieG37.png'),pygame.image.load('Sprite/EnnemieG38.png'),pygame.image.load('Sprite/EnnemieG39.png'),pygame.image.load('Sprite/EnnemieG40.png'),
                      pygame.image.load('Sprite/EnnemieG41.png'),pygame.image.load('Sprite/EnnemieG42.png'),pygame.image.load('Sprite/EnnemieG43.png'),pygame.image.load('Sprite/EnnemieG44.png')]
        self.despawnG=[pygame.image.load('Sprite/EnnemieG17.png'),pygame.image.load('Sprite/EnnemieG16.png'),pygame.image.load('Sprite/EnnemieG15.png'),pygame.image.load('Sprite/EnnemieG14.png'),pygame.image.load('Sprite/EnnemieG13.png'),pygame.image.load('Sprite/EnnemieG12.png'),pygame.image.load('Sprite/EnnemieG11.png'),pygame.image.load('Sprite/EnnemieG10.png'),pygame.image.load('Sprite/EnnemieG9.png'),pygame.image.load('Sprite/EnnemieG8.png'),
                      pygame.image.load('Sprite/EnnemieG7.png'),pygame.image.load('Sprite/EnnemieG6.png'),pygame.image.load('Sprite/EnnemieG5.png'),pygame.image.load('Sprite/EnnemieG4.png'),pygame.image.load('Sprite/EnnemieG3.png'),pygame.image.load('Sprite/EnnemieG2.png'),pygame.image.load('Sprite/EnnemieG1.png')]
        self.spawnD=[pygame.image.load('Sprite/EnnemieD1.png'),pygame.image.load('Sprite/EnnemieD2.png'),pygame.image.load('Sprite/EnnemieD3.png'),pygame.image.load('Sprite/EnnemieD4.png'),pygame.image.load('Sprite/EnnemieD5.png'),pygame.image.load('Sprite/EnnemieD6.png'),pygame.image.load('Sprite/EnnemieD7.png'),pygame.image.load('Sprite/EnnemieD8.png'),pygame.image.load('Sprite/EnnemieD9.png'),pygame.image.load('Sprite/EnnemieD10.png'),
                      pygame.image.load('Sprite/EnnemieD11.png'),pygame.image.load('Sprite/EnnemieD12.png'),pygame.image.load('Sprite/EnnemieD13.png'),pygame.image.load('Sprite/EnnemieD14.png'),pygame.image.load('Sprite/EnnemieD15.png'),pygame.image.load('Sprite/EnnemieD16.png'),pygame.image.load('Sprite/EnnemieD17.png'),pygame.image.load('Sprite/EnnemieD18.png'),pygame.image.load('Sprite/EnnemieD19.png'),pygame.image.load('Sprite/EnnemieD20.png'),]
        self.marcheD=[pygame.image.load('Sprite/EnnemieD21.png'),pygame.image.load('Sprite/EnnemieD22.png'),pygame.image.load('Sprite/EnnemieD23.png'),pygame.image.load('Sprite/EnnemieD24.png'),pygame.image.load('Sprite/EnnemieD25.png'),pygame.image.load('Sprite/EnnemieD26.png'),pygame.image.load('Sprite/EnnemieD27.png'),pygame.image.load('Sprite/EnnemieD28.png'),pygame.image.load('Sprite/EnnemieD29.png'),pygame.image.load('Sprite/EnnemieD30.png'),
                      pygame.image.load('Sprite/EnnemieD31.png'),pygame.image.load('Sprite/EnnemieD32.png'),pygame.image.load('Sprite/EnnemieD33.png'),pygame.image.load('Sprite/EnnemieD34.png'),pygame.image.load('Sprite/EnnemieD35.png'),pygame.image.load('Sprite/EnnemieD36.png'),pygame.image.load('Sprite/EnnemieD37.png'),pygame.image.load('Sprite/EnnemieD38.png'),pygame.image.load('Sprite/EnnemieD39.png'),pygame.image.load('Sprite/EnnemieD40.png'),
                      pygame.image.load('Sprite/EnnemieD41.png'),pygame.image.load('Sprite/EnnemieD42.png'),pygame.image.load('Sprite/EnnemieD43.png'),pygame.image.load('Sprite/EnnemieD44.png')]
        self.despawnD=[pygame.image.load('Sprite/EnnemieD17.png'),pygame.image.load('Sprite/EnnemieD16.png'),pygame.image.load('Sprite/EnnemieD15.png'),pygame.image.load('Sprite/EnnemieD14.png'),pygame.image.load('Sprite/EnnemieD13.png'),pygame.image.load('Sprite/EnnemieD12.png'),pygame.image.load('Sprite/EnnemieD11.png'),pygame.image.load('Sprite/EnnemieD10.png'),pygame.image.load('Sprite/EnnemieD9.png'),pygame.image.load('Sprite/EnnemieD8.png'),
                      pygame.image.load('Sprite/EnnemieD7.png'),pygame.image.load('Sprite/EnnemieD6.png'),pygame.image.load('Sprite/EnnemieD5.png'),pygame.image.load('Sprite/EnnemieD4.png'),pygame.image.load('Sprite/EnnemieD3.png'),pygame.image.load('Sprite/EnnemieD2.png'),pygame.image.load('Sprite/EnnemieD1.png')]


    def update(self):
            self.acc = vec(0,self.gravite)                                     #création du vecteur accélération du personnage, sans accélération en x, mais subissant la gravité en y (d'où ici o.5)
            if self.sol == True :
                #self.tempsreel= time.clock()
                self.tempsreel = time.time()
                if self.Rsens == 1 or self.Rsens == 4:                                               #si le hasard choisie 1, le personnage avancera vers la droite
                    if self.spawn == True :                                       #si la variable dit que le personnage vient d'apparaitre, alors on lance la séquence d'apparition
                        self.compteur_spawn +=1
                        self.image = self.spawnD[self.compteur_spawn//2]
                    else :                                                        #une fois fini, on permet au personnage de se déplacer pendant un temps définit au hasard
                        if self.tempdespawnR + self.tempdespawnH>self.tempsreel :
                            self.acc.x= ennemie_acc
                            self.image = self.marcheD[self.compteur_marche//2]
                            self.compteur_marche+=1

                        else :                                                    #une fois le temps dépassé, on lance la séquence de disparition du personnage
                            self.compteur_marche = 0
                            self.compteur_despawn+=1
                            self.image = self.despawnD[self.compteur_despawn]
                elif self.Rsens == 2 or self.Rsens== 5:                                             #si le hasard choisie 2, le personage avancera vers la gauche
                    if self.spawn == True :                                       #le principe de la boucle est ensuite la même que la précédente
                        self.compteur_spawn +=1
                        self.image = self.spawnG[self.compteur_spawn//2]
                    else :
                        if self.tempdespawnR + self.tempdespawnH>self.tempsreel:
                            self.acc.x= -ennemie_acc
                            self.image = self.marcheG[self.compteur_marche//2]
                            self.compteur_marche+=1

                        else :
                            self.compteur_despawn+=1
                            self.image = self.despawnG[self.compteur_despawn]


                elif self.Rsens == 3:                                             #si le hasard choisie 3, le personnage restera statique
                    if self.spawn == True :                                       #on amorce alors une séquence de spawn
                        self.compteur_spawn +=1
                        self.image = self.spawnG[self.compteur_spawn//2]
                    else :
                        self.image= pygame.image.load("Sprite/ennemieG17.png")    #puis tout est mis au point mort pendant un temps prédéfini au hasard
                        if self.tempdespawnR + self.tempdespawnH<self.tempsreel:
                            self.compteur_despawn+=1
                            self.image = self.despawnG[self.compteur_despawn]

                if self.compteur_spawn+1>=40:
                    self.compteur_spawn = 0
                    self.spawn = False
                   # self.tempdespawnR = time.clock()
                    self.tempdespawnR= time.time()
                if self.compteur_despawn+1>=17:
                    self.compteur_marche = 0
                    self.compteur_despawn = 0
                    self.Rsens = 1
                    #self.spawn=True
                    self.mort = True
                    #self.tempdespawnH = randint(5,10)
                if self.compteur_marche+1 >=46:
                    self.compteur_marche = 0

            self.rect.midbottom = self.pos                                        #placement des pieds du personnage, au niveau de ce que l'on a définit comme son vecteur position, et que l'on a précédemment modifié avec les formules physiques                                                                               #formules physique, permettant le calcul de la nouvelle position en fonction de la modification des paramètres accélération et vitesse (acc et vel)
            self.acc.x+=self.vel.x*perso_friction                                 #l'ajout de ses formules permet d'accroitre le réalisme des mouvements, notamment avec l'intégration de frixions
            self.vel += self.acc
            self.pos+=self.vel+0.5*self.acc

#Class du personnage non joueur (PNJ) que l'on croise au niveau 1
class Papy(pygame.sprite.Sprite):                                                 #cette class sert à l'affichage de notre mecène
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("Sprite/Papy.png").convert_alpha()
        self.rect = pygame.Rect(x, y, 70, 70)
        self.rect.x = x
        self.rect.y = y
        self.compteur_pop = 0
        self.compteur_don = 0
        self.don = False

        frame1 = pygame.image.load('Sprite/Papy.png')
        frame2 = pygame.image.load('Sprite/Papy2.png')
        frame3 = pygame.image.load('Sprite/Papy3.png')
        frame4 = pygame.image.load('Sprite/Papy4.png')
        frame5 = pygame.image.load('Sprite/Papy5.png')
        self.pop = [frame1,frame2]
        self.give = [frame1,frame3,frame4,frame5]

    def update (self):
        if not self.don :
            self.image = self.pop[self.compteur_pop//14]
            self.compteur_pop += 1

            if self.compteur_pop+1 >= 28:
                self.compteur_pop = 0

        if self.don :
            if not self.compteur_don+1 >= 30:
                self.image = self.don[self.compteur_don//10]
                self.compteur_don +=1

#############################Suite de class définissant les structure des niveaux du jeu (Plateforms, sol...)##########################################""""
class bloc(pygame.sprite.Sprite):                                                 #on matérialise désormait nos obstacles (du décor)
    def __init__(self,x,y,image):                                                       #on use d'autres variables pour l'initialiser, que sont sa position en x et y, ainsi que sa largeur et sa hauteur
        pygame.sprite.Sprite.__init__(self)                                       #il nous est ainsi possible d'avoir un même type d'objet (d'obstacle), mais dont les paramètres cités précédemment varient entre eux                                 
        self.rect = pygame.Rect(x, y,60,60)                                       #on crée un rectangle autour de notre surface, qui servira de hitbox pour les obstacles
        self.rect.y = y                                                           #les variables x et y de notre fonction, sont rendues utilisables en les associant aux coordonnées du rectangle
        self.rect.x = x
        self.image= pygame.image.load(image).convert_alpha()

class Sol(pygame.sprite.Sprite):                                                  #De la même façon que pour le personnage et les blocs, on matérialise notre sol
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60,80))                                      #dimension du sol
        self.imgsol= pygame.image.load(image).convert_alpha()
        self.image.blit(self.imgsol,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x                                                           #placement du sol
        self.rect.y = y


class mur(pygame.sprite.Sprite):                                                 #on place des murs transparents pour délimiter notre jeu
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60,60))
        self.image.set_alpha(0,0)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Nuage(pygame.sprite.Sprite):                                                #on matérialise notre nuage
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Nuage1.png").convert_alpha()
        self.rect = pygame.Rect(x, y,300,200)
        self.rect.x = x
        self.rect.y = y


class Nuage2(pygame.sprite.Sprite):                                               #on matérialise notre second nuage
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Nuage2.png").convert_alpha()
        self.rect = pygame.Rect(x, y,300,200)
        self.rect.x = x
        self.rect.y = y

class fabrique(pygame.sprite.Sprite):                                               
    def __init__(self,x,y,niveau,adresse):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(adresse).convert_alpha()
        self.rect = pygame.Rect(x, y,1000,500)
        self.rect.x = x
        self.rect.y = y
        self.niveau = niveau
        self.compteur_ovrt = 0
        p1 = pygame.image.load("Sprite/porteF.png").convert_alpha()
        p2 = pygame.image.load("Sprite/porteO.png").convert_alpha()
        p3 = pygame.image.load("Sprite/porteO2.png").convert_alpha()
        p4 = pygame.image.load("Sprite/porteO3.png").convert_alpha()
        self.ouverture = [p1,p2,p3,p4]
    
    def MAJ(self) :
        
        if self.niveau == 2 :
                if not self.compteur_ovrt+1 >= 20:
                    self.image = self.ouverture[self.compteur_ovrt//5]  #7 tours de boucle while par sprite
                    self.compteur_ovrt += 1


class Piège(pygame.sprite.Sprite):                                                #on matérialise nos pièges
    def __init__(self,x,y,niveau):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/traps1.png').convert_alpha()
        self.rect = pygame.Rect(x, y,60,60)
        self.rect.x = x
        self.rect.y = y
        self.compteur_dépl = 0
        self.compteur_retr = 0
        self.death = False
        self.niveau = niveau
        self.hasard = randint(1,2)
            
        p1 = pygame.image.load('Sprite/traps1.png').convert_alpha()
        p2 = pygame.image.load('Sprite/traps2.png').convert_alpha()
        p3 = pygame.image.load('Sprite/traps3.png').convert_alpha()
        p4 = pygame.image.load('Sprite/traps4.png').convert_alpha()
        self.déploiement = [p1,p1,p1,p1,p2,p3,p4]
        self.retranchement = [p4,p3,p2,p1,p1,p1,p1]

        p1_2 = pygame.image.load('Sprite/traps1_2.png').convert_alpha()
        p2_2 = pygame.image.load('Sprite/traps2_2.png').convert_alpha()
        p3_2 = pygame.image.load('Sprite/traps3_2.png').convert_alpha()
        p4_2 = pygame.image.load('Sprite/traps4_2.png').convert_alpha()
        self.déploiement2 = [p1_2,p2_2,p3_2,p4_2]

    def update (self):
        if self.niveau == 2 :
            if self.hasard == 1 :
                self.death = True
                if not self.compteur_dépl+1 >= 20:
                    self.image = self.déploiement2[self.compteur_dépl//5]
                    self.compteur_dépl += 1

                else:
                    self.compteur_dépl =0

            if self.hasard == 2 :
                self.image = pygame.image.load('Sprite/piege.png').convert_alpha()

        elif self.niveau == 1 :
            if self.hasard == 1 :
                if not self.compteur_dépl+1 >= 35:
                    if self.compteur_dépl <= 20 :
                        self.death = False
                    else :
                        self.death = True
                    self.image = self.déploiement[self.compteur_dépl//5]
                    self.compteur_dépl += 1

                else:
                    self.compteur_dépl +=0
                    if not self.compteur_retr+1 >= 35 :
                        if self.compteur_retr >= 20 :
                            self.death = False
                        else :
                            self.death = True
                        self.image = self.retranchement[self.compteur_retr//5]
                        self.compteur_retr += 1
                    else :
                        self.compteur_dépl = 0
                        self.compteur_retr = 0

            if self.hasard == 2 :
                self.image = pygame.image.load('Sprite/piege.png').convert_alpha()



class chest(pygame.sprite.Sprite):                                                #cette class sert à l'affichage de notre coffre
    def __init__(self,jeu,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.jeu = jeu
        self.feu = fire(jeu,x-60,y+15)
        self.image= pygame.image.load("Sprite/coffre1.png").convert_alpha()
        self.rect = pygame.Rect(x, y, 90, 104)
        self.rect_y = y
        self.rect_x = x
        self.compteur_coffre=0
        self.ouvert = False
        self.ouvert2 = False

        chest1 = pygame.image.load('Sprite/coffre1.png')
        chest2 = pygame.image.load('Sprite/coffre2.png')
        chest3 = pygame.image.load('Sprite/coffre3.png')
        chest4 = pygame.image.load('Sprite/coffre4.png')
        chest5 = pygame.image.load('Sprite/coffre5.png')
        chest6 = pygame.image.load('Sprite/coffre6.png')
        self.imgcoffre = [chest1,chest2,chest3,chest4,chest5,chest6]


    def update (self):
        if self.ouvert :
            if not self.compteur_coffre+1 >= 24:
                self.image = self.imgcoffre[self.compteur_coffre//4]
                self.compteur_coffre += 1

            else :
                self.compteur_coffre += 0
                self.feu.action = True


class fire(pygame.sprite.Sprite):                                                #cette class sert à l'affichage de notre coffre
    def __init__(self,jeu,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.jeu = jeu
        self.image= pygame.image.load("Sprite/feu0.png").convert_alpha()
        self.rect = pygame.Rect(x, y, 50, 50)
        self.rect_y = y
        self.rect_x = x
        self.compteur_flamme=0
        self.chance = randint(1,3)
        self.bonus = randint(1,2)
        self.action = False


        feu1 = pygame.image.load('Sprite/feu1.png')
        feu2 = pygame.image.load('Sprite/feu2.png')
        feu3 = pygame.image.load('Sprite/feu3.png')
        feu4 = pygame.image.load('Sprite/feu4.png')
        feu5 = pygame.image.load('Sprite/feu5.png')
        feu6 = pygame.image.load('Sprite/feu6.png')
        feu7 = pygame.image.load('Sprite/feu7.png')
        feu8 = pygame.image.load('Sprite/feu8.png')
        feu9 = pygame.image.load('Sprite/feu9.png')
        feu10 = pygame.image.load('Sprite/feu10.png')
        feu11 = pygame.image.load('Sprite/feu11.png')
        feu12 = pygame.image.load('Sprite/feu12.png')
        self.imgfeu = [feu1,feu2,feu3,feu4,feu5,feu6,feu7,feu8,feu9,feu10,feu11,feu12]

    def update (self):
        if self.action :                                                         #lorsque les flammes sont actionnées, leur animation s'active une fois
            if not self.compteur_flamme+1 >= 24:
                self.image = self.imgfeu[self.compteur_flamme//2]
                self.compteur_flamme += 1

            else :
                self.compteur_flamme += 0                                        #une fois terminée, un cadeau s'affiche au hasard à la place de la flamme

                if self.chance == 1 :
                    self.image = pygame.image.load('Sprite/Splanete.png')

                elif self.chance == 2 :
                    self.image = pygame.image.load('Sprite/Seringue.png')

                elif self.chance == 3 :
                    self.image = pygame.image.load('Sprite/Rubis.png')


class loot(pygame.sprite.Sprite):                                                #cette class sert à l'affichage des capsules de survie
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("Sprite/globe - 1.png").convert_alpha()
        self.rect = pygame.Rect(x, y, 50, 60)
        self.rect.y = y
        self.rect.x = x
        self.compteur_globe=0

        globe1 = pygame.image.load('Sprite/globe - 1.png')                       #tout comme le personnage, elles sont en mouvement mais continu
        globe2 = pygame.image.load('Sprite/globe - 2.png')
        globe3 = pygame.image.load('Sprite/globe - 3.png')
        globe4 = pygame.image.load('Sprite/globe - 4.png')
        globe5 = pygame.image.load('Sprite/globe - 5.png')
        globe6 = pygame.image.load('Sprite/globe - 6.png')
        globe7 = pygame.image.load('Sprite/globe - 7.png')
        globe8 = pygame.image.load('Sprite/globe - 8.png')
        globe9 = pygame.image.load('Sprite/globe - 9.png')
        globe10 = pygame.image.load('Sprite/globe - 10.png')
        globe11 = pygame.image.load('Sprite/globe - 11.png')
        globe12 = pygame.image.load('Sprite/globe - 12.png')
        self.imgglobe = [globe1,globe2,globe3,globe4,globe5,globe6,globe7,globe8,globe9,globe10,globe11,globe12]

    def update (self):
        self.image = self.imgglobe[self.compteur_globe//16]
        self.compteur_globe += 1

        if self.compteur_globe+1 >= 128:
            self.compteur_globe = 0

#Jauge de vie de notre personnage
class jauge_vie(object):                                                         #on crée les paramètres de notre jauge de vie
    def __init__(self,jeu,w):
        self.jeu = jeu
        self.w = w
        self.écoulement = True

    def update(self):
        if not self.w <= 1:                                                      #celle- ci se vide en continu
            if self.écoulement:
                self.w-= 0.1 #0.1
        elif self.w <= 2 :                                                       #lorsqu'elle est vide, le joueur a perdu
            self.jeu.Soundtrack_findevie.stop()
            self.findevie = True
            self.jeu.gameover = True
        if self.w >= 148:                                                        #par contre, elle ne peut pas se remplir plus que sa capacité maximale
            self.w = 148



#création de la caméra, indispensable au déroulé du platformer, permettant de suivre le personnage dans ses déplacements
class Camera:
    def __init__(self, longueur, hauteur):
        self.camera = pygame.Rect(0,0,longueur,hauteur)
        self.longueur = longueur
        self.hauteur = hauteur


    def apply(self, entité):
        return entité.rect.move(self.camera.topleft)                             #on défini l'entité en fonction de laquelle notre caméra se déplace

    def update(self, entité):
        x = -entité.pos.x + int(fenetreL / 2)                                    #on impose à la caméra de toujours être centrée sur sa cible
        y = -entité.pos.y                                                        #a contario, elle ne suit pas les déplacements verticaux du personnage

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.longueur - fenetreL), x)
        y = max(-(self.hauteur - fenetreH), y)
        self.camera = pygame.Rect(x, y, self.longueur, self.hauteur)

###############################################Création de la class utile pour nos 2 niveaux############################################
class Niveau:
    def __init__(self, fichier):
        self.data = []
        with open(fichier,'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * 60
        self.height = self.tileheight * 60




class jeu:
    """
    Fonction principale du jeu, qui initialise l'essentiel et rend le jeu possible 
    en implantant paramètres et conditions, tout en utilisant les classes précédemments crées.

    C'est dans cette class que nos menus, niveau...etc vont prendre forme.
    """
    def __init__(self):

        #initialisation du module pygame
        pygame.init()                                                            

        #initialisation et personalisation de la fenêtre
        self.fenetreL= 1000                                   
        self.fenetreH= 560

        #Chargement plateformes et fond d'écran
        self.fenetre = pygame.display.set_mode((self.fenetreL,self.fenetreH))
        self.fond= pygame.image.load('images/apocalypse.jpg').convert()
        self.fond2= pygame.image.load('images/apocalypse2.jpg').convert()
        self.fond3= pygame.image.load('images/apocalypse.jpg').convert()
        self.fond_langues = pygame.transform.scale(pygame.image.load('images/Fond_langues.jpg').convert(), (1100,560))
        self.mute = pygame.image.load('images/volume_off.png').convert_alpha()
        self.demute = pygame.image.load('images/volume_on.png').convert_alpha()
        #on crée les variables contenant le fond du menu
        self.fondintro= pygame.image.load('images/Fond_intro.jpg').convert()      
        self.fondintrobis = pygame.image.load('images/Fond_introBis.jpg').convert()
        self.Hard = pygame.image.load('Sprite/Hard.png')

        #Initialisation des variables chiffrées
        self.fond_x = -50
        self.fond2_x = 1230
        self.fond3_x = 2210
        self.Health = 10
        self.hit=4
        self.nbr_tentatives = 0             #Variable utile pour établir le score

        #Chargement musique et son
        self.son_piege = pygame.mixer.Sound("son/Son_piege.wav")
        self.Soundtrack_win = pygame.mixer.Sound("son/Soundtrack_win.wav")
        self.Soundtrack_usine = pygame.mixer.Sound("son/Soundtrack_usine.wav")
        self.Soundtrack_gameover = pygame.mixer.Sound("son/Soundtrack_gameover.wav")
        self.Soundtrack_findevie = pygame.mixer.Sound("son/Soundtrack_findevie.wav")
        self.Soundtrack_jeu = pygame.mixer.Sound("son/Soundtrack_jeu.wav")
        self.Soundtrack_jeu.set_volume(0.75)
        self.Sound_hit = pygame.mixer.Sound("son/Sound_hit.wav")
        self.Soundtrack_intro = pygame.mixer.Sound("son/Soundtrack_intro.wav")
        self.Soundtrack_intro.set_volume(0.75)
        self.Orage = pygame.mixer.Sound("son/Orage.wav")
        self.feu = pygame.mixer.Sound("son/Soundtrack_lootcoffre.wav")
        self.craque= pygame.mixer.Sound("son/OS.wav")

        #Création du nom de la fenêtre
        pygame.display.set_caption("The Survivor")

        #Ouverture du fichier contenant le meilleur score du jeu
        self.registre_score = open("HighScore.txt","r")
        self.registre_score_txt = self.registre_score.readlines()


################################ variables principales de la class jeu ###############################

        self.horloge = pygame.time.Clock()  #Permet d'établir le nombre d'image par seconde (FPS)
        self.realtime =time.time()          #Permet de connaitre le temps actuel (utile pour établir le record)

        self.min_t1 = 1 #7
        self.max_t1 = 20 #20
        self.Htime = randint(self.min_t1,self.max_t1)
        self.Rtime = 0

        #Bool d'état du jeu, distribuant de précieuses informations quant à l'état du jeu
        self.dead= True
        self.Win = False
        self.start = False
        self.musique = True
        self.niveau = 1
        self.Bruitage = True
        self.declick = True
        self.degat = True
        self.findevie = True
        self.END = False                                                         #end=false, car la partie n'est pas finie
        self.intro = True                                                        #par défaut, intro est vrai car le menu se lance automatiquement à l'ouverture du jeu
        self.gameover = False
        self.pause = False
        self.first = True
        self.globe_plus = False
        self.globe_moins = False
        self.anglais = False
        self.francais = False
        self.saisi = 1                                                      #détecte la saisie en cas de victoire
        self.active = False
        self.ZQSD = False                                                   #ZQSD faux par défaut, car les commandes par défauts sont les flèches directionnelles
        
        #Importation de nos niveaux
        self.niveau1 = Niveau(os.path.join(os.path.dirname(__file__), 'Niveau.txt'))
        self.niveau2 = Niveau(os.path.join(os.path.dirname(__file__), 'Niveau2.txt'))

    def fermeture(self):
        """
        fonction qui vérifie que l'on ne cherche pas à fermer le jeu.
        Le cas échéant, renvoie un booléen et modifie ceux ci-dessus, attribu de la class jeu,
        pour faire sortir le joueur de toutes les boucles et terminer le programme
        """
        for event in pygame.event.get() :                                        #on verifie que dans la liste des événements ne figure pas le fermeture de la fenêtre (event devient alors tous les évenements de la liste)
            if event.type == pygame.QUIT :                                       #si c'est le cas, on renvoie un booléen
                self.jouer = False
                self.intro = False
                self.END=True
                self.francais = True
                self.anglais = False
                self.first = False
                return(True)


    def nouveau(self):
        """
        fonction appelant nos classes et les réunissant par groupe. 
        Cette méthode permet de créer nos niveau (niveau 1 et 2) en fonction de la valeur de nos booléeans
        """
        self.personnage = personnage(self,7820,20)                                 #rajouter "self" en appelant la class personnage, permet de le munir des outils dont dispose la classe jeu (soit toutes les classes et sprites, dont les platformes)
        self.vie = jauge_vie(self,150)
        self.saisi = 1

        self.all_sprites = pygame.sprite.Group()                                 #on crée un premier groupe de sprite (classes utilisant le constructeur parent), qui réunira toutes nos entitées, nos sprites
        self.platformes = pygame.sprite.Group()                                  #on crée un second groupe qui contiendra uniquement les sprites (entitées) considérés comme des platformes ou obstacles
        self.récolte = pygame.sprite.Group()                                     #notre troisième groupe contient les capsules
        self.objetbonus = pygame.sprite.Group()
        self.kill = pygame.sprite.Group()
        self.ennemies_sprites=pygame.sprite.Group()                              #et le dernier nos ennemies
        
        if self.niveau == 1 :

            self.fabrique = fabrique(19500,-10,self.niveau,"images/Fabrique.png")
            self.fond= pygame.image.load('images/apocalypse.jpg').convert()
            self.fond2= pygame.image.load('images/apocalypse2.jpg').convert()
            self.fond3= pygame.image.load('images/apocalypse.jpg').convert()
            self.papy = Papy(5500,412)
            self.coffre = chest(self,7840,20)
            self.coffre2 = chest(self,14680,-40)
            self.fond_x = -50
            self.fond2_x = 1230
            self.fond3_x = 2210
            #self.flamme1 = fire(self,7780,35)
            #self.flamme2 = fire(self,14610,5)

            for j, ligne in enumerate(self.niveau1.data):                            #on identifie chaque ligne et case du niveau afin de lui attribuer une image
                for i, case in enumerate(ligne):                                     #on fait intervenir les class précédement crées
                    if case == "M":
                        m = mur(i*60,j*60)
                        self.all_sprites.add(m)
                        self.platformes.add(m)

                    if case == "B":
                        b = bloc(i*60,j*60,"images/brique.jpg")
                        self.all_sprites.add(b)
                        self.platformes.add(b)

                    if case == "S":
                        s = Sol(i*60,j*60,"images/sol-sable.jpg")
                        self.all_sprites.add(s)
                        self.platformes.add(s)

                    if case == "L":
                        l = loot(i*60,j*60)
                        self.all_sprites.add(l)
                        self.récolte.add(l)

                    if case == "P":
                        p = Piège(i*60,j*60,self.niveau)
                        self.all_sprites.add(p)
                        self.kill.add(p)

                    if case == "n":
                        n1 = Nuage(i*60,j*60)
                        self.all_sprites.add(n1)

                    if case == "N":
                        n2 = Nuage2(i*60,j*60)
                        self.all_sprites.add(n2)

            self.all_sprites.add(self.coffre)
            self.all_sprites.add(self.coffre2)
            self.all_sprites.add(self.personnage)                                    #on ajoute notre sprite/classe personnage uniquement au premier groupe
            self.all_sprites.add(self.papy)
            self.all_sprites.add(self.coffre.feu)
            self.all_sprites.add(self.coffre2.feu)
            self.objetbonus.add(self.coffre.feu)
            self.objetbonus.add(self.coffre2.feu)
            self.all_sprites.add(self.fabrique)

        elif self.niveau == 2 :

            self.fond_x = -50
            self.fond2_x = 1295
            self.fond3_x = 2340
            self.fabrique = fabrique(19600,230,self.niveau,"Sprite/porteF.png")
            self.fond= pygame.transform.scale(pygame.image.load('images/LVL2apocalypse.jpg').convert(), (1345,560))
            self.fond2= (pygame.image.load('images/LVL2apocalypse2.jpg').convert())   #(1045,560)
            self.fond3= pygame.transform.scale(pygame.image.load('images/LVL2apocalypse.jpg').convert(), (1345,560))
            self.papy = Papy(-100,-100)                                                                                 #on fait disparaitre le papy, technique sauvage pour ne plus l'avoir dans les pattes
            self.coffre = chest(self,9460,20)
            self.coffre2 = self.coffre #chest(self,9400,-40) 
            #self.flamme1 = fire(self,7850,35)
            #self.flamme2 = self.flamme1 #fire(self,14610,5)

            for j, ligne in enumerate(self.niveau2.data):                            #on applique la même chose à un second niveau
                for i, case in enumerate(ligne):
                    if case == "M":
                        m = mur(i*60,j*60)
                        self.all_sprites.add(m)
                        self.platformes.add(m)

                    if case == "Z":
                        b = bloc(i*60,j*60,"images/tuyaux1.png")
                        self.all_sprites.add(b)
                        self.platformes.add(b)
                    
                    if case == "Y":
                        b = bloc(i*60,j*60,"images/tuyaux2.png")
                        self.all_sprites.add(b)
                        self.platformes.add(b)

                    if case == "X":
                        b = bloc(i*60,j*60,"images/tuyaux4.png")
                        self.all_sprites.add(b)
                        self.platformes.add(b)

                    if case == "W":
                        b = bloc(i*60,j*60,"images/tuyaux3.png")
                        self.all_sprites.add(b)
                        self.platformes.add(b)

                    if case == "S":
                        s = Sol(i*60,j*60,"images/sol-metal.png")
                        self.all_sprites.add(s)
                        self.platformes.add(s)

                    if case == "L":
                        l = loot(i*60,j*60)
                        self.all_sprites.add(l)
                        self.récolte.add(l)

                    if case == "P":
                        p = Piège(i*60,j*60,self.niveau)
                        self.all_sprites.add(p)
                        self.kill.add(p)

                    if case == "n":
                        n1 = Nuage(i*60,j*60)
                        self.all_sprites.add(n1)

                    if case == "N":
                        n2 = Nuage2(i*60,j*60)
                        self.all_sprites.add(n2)

            self.all_sprites.add(self.coffre)
            self.all_sprites.add(self.coffre2)
            self.all_sprites.add(self.fabrique)
            self.all_sprites.add(self.personnage)                                    #on ajoute notre sprite/classe personnage uniquement au premier groupe
            self.all_sprites.add(self.papy)
            self.all_sprites.add(self.coffre.feu)
            self.all_sprites.add(self.coffre.feu)
            self.objetbonus.add(self.coffre.feu)
            self.objetbonus.add(self.coffre.feu)

        self.camera = Camera(self.niveau1.width, self.fenetreH)                      #on attribue des dimentions à notre caméra
        self.run()                                                               #et on lance le jeu


    def run(self):
        """
        fonction du jeu regroupant les fonctions essentielles au jeu, tout en vérifiant qu'on veuille toujours jouer.
        C'est cette méthode qui tourne en boucle (while) tant que l'on continu de jouer.
        """
        self.jouer=True                                                          #jouer=true, car nous jouons toujours
        
        while self.jouer :                                                       #boucle "tant que" indispensable au lancement en continu des action
            self.realtime = time.time()
            self.horloge.tick(FPS)                                               #on rafraichit l'écran et les actions 40 fois par seconde (40 FPS)...
            #puis on lance en boucle toutes les fonctions essentielles au jeu...
            
            if not self.pause and not self.Win and not self.gameover:            #lorsque le jeu est en pause, on interrompt la mise à jour de la page
                self.update()
                self.all_sprites.update()
                self.draw()                                                       #la page de jeu est dessinée seulement si le jeu n'est pas en pause et que le personnage n'a pas perdu
                self.temps_final = (self.realtime-self.started_time)

            elif self.gameover and not self.pause and not self.Win :             #si le personnage a perdu et que le jeu n'est pas pause alors : Game over !
                self.game_over()

            elif self.pause and not self.gameover and not self.Win :             #si la pause est actionné, lancement du menu pause 
                Debut_pause = time.time()
                self.put_pause()
                self.realtime = time.time()
                self.started_time = self.started_time + (self.realtime - Debut_pause)          #le temps passé dans les menus, ne compte pas pour le score

            elif self.Win and not self.pause and not self.gameover :
                self.win()

            self.events()   
        
        #penser à fermer le registre des score quand on ferme le jeu
        self.registre_score.close()


    def events(self):
        """
        fonction vérifiant que l'on ne clique par sur la croix rouge, pour fermer la fenêtre et donc le jeu.
        Elle est également et surtout sensible au touche relachées, pour connaitre les intentions du joueur pendant sa partie
        """
        
        for event in pygame.event.get():                                        #On vérifie que dans la liste des évènements (jusqu'à la fermeture du jeu),
            if self.Win :
                if float(re.sub("\n","",(self.registre_score_txt)[0])) > self.temps_final  and  self.hit >= int(re.sub("\n","",(self.registre_score_txt)[1]))  and  self.saisi == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.input_rect.collidepoint(event.pos):
                            self.active = True
                            if self.user_text == win11:
                                self.user_text = ''
                        else:
                            self.active = False
                            if self.user_text == '':
                                self.user_text = win11
            
                    if event.type == pygame.KEYDOWN:
            
                        # Check for backspace
                        if event.key == pygame.K_BACKSPACE:
            
                            # get text input from 0 to -1 i.e. end.
                            self.user_text = self.user_text[:-1]
            
                        elif event.key == pygame.K_RETURN :
                            if not self.user_text == win11 :
                                self.saisi = 2

                        # Unicode standard is used for string
                        # formation
                        else:
                            if not len(self.user_text) > 20 :
                                self.user_text += event.unicode
                
            else :
            

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.personnage.sauter()

                    if Jeu.ZQSD :
                        UP = pygame.K_z
                    else:
                        UP = pygame.K_UP

                    if event.key == UP:
                        if self.coffre.rect.x <self.personnage.pos.x< self.coffre.rect.x + 90 :
                            if self.coffre.rect.y + 110 > self.personnage.pos.y > self.coffre.rect.y:
                                self.coffre.ouvert = True
                                self.coffre.update()
                        if self.niveau == 1 :
                            if self.coffre2.rect.x <self.personnage.pos.x< self.coffre2.rect.x + 90 :
                                if self.coffre2.rect.y + 110 > self.personnage.pos.y > self.coffre2.rect.y:
                                    self.coffre2.ouvert = True
                                    self.coffre2.update()


                if event.type == pygame.KEYUP:                                       #on profite de la sensibilité du module event envers les touches relachées,
                    if event.key == pygame.K_SPACE:                                  #pour lancer notre saut ou notre saut court (n'aurait pas été possible avec la variable keys de la classe personnage)
                        self.personnage.saut_court()
            
            if event.type == pygame.QUIT :                                 
                if self.jouer:
                    self.jouer = False
                self.END=True

    def update(self):
        """
        fonction mettant à jour les groupes sprites et leurs informations (coordonnées...etc) (fait tourner la fonction update de TOUS les sprites)
        Cette méthode gère aussi les collisions, le spawn et despawn des ennemies, 
        ainsi que la position de tous nos sprites et les agissements en fonction de cette position
        """

        if self.personnage.pos.x < 19400 :
            self.camera.update(self.personnage)                                      #on met à jour la position de la caméra pas rapport au personnage

        collisions = pygame.sprite.spritecollide(self.personnage,self.platformes,False) #on définit la condition collision, qui renvoie un booléen

        if self.personnage.vel.y >= 0 :                                          #on vérifie que notre personnage n'aille SUR une platforme, que si il vient de dessus et qu'il tombe sur la platforme
            if collisions :                                                      #on vérifie la condition
                if self.personnage.pos.y<= collisions[0].rect.bottom-20 :
                    self.personnage.pos.y=collisions[0].rect.top                 #si il y a collision, on place les pied du personnage, sur le haut de la platforme touchée
                    self.personnage.vel.y = 0                                    #et on arrête de le faire tomber, en mettant sa vitesse en y à 0
                    self.personnage.saut = False

        if self.personnage.vel.y < 0 :                                           #au contraire : si le personnage saute
            if collisions :
                if self.personnage.pos.y >= collisions[0].rect.bottom+20 :
                    self.personnage.rect.top = collisions[0].rect.bottom         #on lui impose de se cogner à la platforme colidée
                    self.personnage.saut_court()                                 #et de retomber à l'image de si il avait réalisé un saut court

        if self.Htime+self.Rtime<self.realtime and self.start==True :           #création ennemies
                self.Htime = randint(self.min_t1,self.max_t1)
                #self.Rtime = time.clock()
                self.Rtime = time.time()
                self.R1 = randint(150,400)
                self.R2 = randint(300,800)
                self.Rsens = randint(1,5)
                if self.Rsens == 1 or self.Rsens==4:
                    self.X_ennemies = self.personnage.pos.x - self.R1
                else :
                    self.X_ennemies = self.personnage.pos.x + self.R2
                self.Y_ennemies = randint(0,400)
                self.ennemies = ennemie(self,self.personnage,self.X_ennemies,self.Y_ennemies)
                self.all_sprites.add(self.ennemies)
                self.ennemies_sprites.add(self.ennemies)
                #ennemie.tempdespawnR = time.clock()
                ennemie.tempdespawnR = time.time()

        collisionP = pygame.sprite.spritecollide(self.personnage,self.ennemies_sprites,False)

        for Ennemie in self.ennemies_sprites :                                  #gestion ennemies
            if collisionP and Ennemie.spawn == False:                                                          #sur le même principe, on impose des collisions aux ennemies
                self.vie.w -= self.hit
                if self.degat == True and self.Bruitage== True:
                    self.Sound_hit.play()
                    self.degat = False
                if self.degat == True and self.Bruitage== False:
                    self.degat = False
            if not collisionP :
                self.degat = True
            if Ennemie.Rsens == 3 and Ennemie.sol == True :
                Ennemie.gravite = 0
            if Ennemie.mort == True :
                pygame.sprite.Sprite.kill(Ennemie)
            if Ennemie.vel.y >= 0 :
                collisionE = pygame.sprite.spritecollide(Ennemie,self.platformes,False)
                if collisionE :
                    if Ennemie.pos.y<= collisionE[0].rect.bottom :
                        Ennemie.sol = True
                        Ennemie.pos.y=collisionE[0].rect.top
                        Ennemie.vel.y = 0
                        if Ennemie.Rsens == [1,2,4,5] and Ennemie.sol == True :
                            Ennemie.gravite = 0.1
            if Ennemie.pos.y > 530 : #560                                    #optimisation : Un ennemi qui tombe dans le vide est un ennemie qu'on arrête de charger
                if not Ennemie.spawn :                                       #si l'ennemi était apparu, alors on le fait joliement disparaitre en forçant la désaparition
                    Ennemie.tempdespawnH = 0
                    Ennemie.gravite = 0
                    Ennemie.vel.y = 0
                else :                                                       #si l'ennemi tombe dans le vide sans être apparu, on en fait apparaitre un nouveau et on le supprime
                    Ennemie.spawn = False
                    self.Htime = 0
                    pygame.sprite.Sprite.kill(Ennemie)
                    Ennemie.gravite = 0
                    Ennemie.vel.y = 0


        collisionT = pygame.sprite.spritecollide(self.personnage,self.kill,False)
        if collisionT :
            if collisionT[0].rect.top < self.personnage.pos.y < collisionT[0].rect.bottom+10 :  #-30 ; +10
                if collisionT[0].hasard == 1 :
                    if collisionT[0].death == True :
                        self.vie.w -= self.hit
                        if self.Bruitage== True :
                            if self.niveau == 1 and self.dead == True:
                                self.son_piege.play()
                                self.dead = False
                            elif self.niveau == 2 :
                                self.son_piege.play()


                    elif collisionT[0].death == False :
                        self.vie.w -= 0
                        if self.dead == False:
                            self.dead = True

                if collisionT[0].hasard == 2 :
                    self.vie.w -= self.hit
                    if self.Bruitage== True and self.dead == True:
                        self.son_piege.play()
                        self.dead = False

        if not collisionT :
            if self.dead == False:
                self.dead = True

        #boucle active que lorsqu'il existe un objet bonus sur la carte
        for glob in pygame.sprite.spritecollide(self.personnage,self.récolte,1): #on crée un sprite "dokill" : si collision il y a, l'objet collidé disparait
            if self.globe_plus :
                self.vie.w += self.Health*3
            elif self.globe_plus :
                self.vie.w += self.Health//3
            else :
                self.vie.w += self.Health                                            #et le personnage regagne de la vie
            if self.Bruitage == True :
               pygame.mixer.Sound("son/son_globe.wav").play()


        for flam in self.objetbonus :
            if flam.action:
                for flamme in pygame.sprite.spritecollide(self.personnage,self.objetbonus,1):
                    if flamme.chance == 1 :
                        for i in range (150):
                            self.vie.w += 1
                        if self.Bruitage == True :
                            self.feu.play()

                    elif flamme.chance == 2 :
                        if flamme.bonus == 1 :
                            self.globe_plus = True
                            if self.Bruitage == True :
                                self.feu.play()
                        if flamme.bonus == 2 :
                            self.globe_moins = True
                            if self.Bruitage == True :
                                self.feu.play()

                    elif flamme.chance == 3 :
                        while not self.vie.w >= 80 :
                            self.vie.w += 5
                        if self.Bruitage == True :
                            self.feu.play()


        if self.papy.rect.x >self.personnage.pos.x > self.papy.rect.x - 80 :
            if self.papy.rect.y < self.personnage.rect.top :
                if self.all_sprites.has(self.papy) :
                    self.personnage.avancer = False
                    self.vie.écoulement = False
                    self.dialogue()
                else:
                    self.vie.écoulement = True
                    self.personnage.avancer = True
                    self.start = True
        elif self.personnage.pos.x > self.papy.rect.x +100 :                     # même si le personnage n'a pas entamé le dialogue, les ennemis commencent à spawn
            self.start = True

        if self.personnage.rect.top > 560 :                                      #si le personnage tombe dans un trou
            self.Soundtrack_findevie.stop()
            self.gameover = True
            #self.game_over()

        if self.personnage.pos.x > 18700 :                                  #passage du niveau 1 au niveau 2, puis du niveau 2 à la victoire
            self.personnage.sprint = True
            self.vie.écoulement = False
            self.start = False
            if 19700 > self.personnage.pos.x > 19400 :
                self.fabrique.MAJ()
            elif self.personnage.pos.x >  19700:
                if self.niveau == 1 :
                    self.niveau = 2
                    self.fond_x = -50
                    self.fond2_x = 1230
                    self.fond3_x = 2275

                    #INSERER ICI TRANSITION DU LVL 1 VERS LVL 2

                    self.nouveau()
                elif self.niveau == 2 :
                    self.Win =True
                    #self.win()

        self.ennemies_sprites.update()
        self.platformes.update()
        self.récolte.update()
        self.vie.update()                                                        #ainsi que la jauge de vie

        pygame.display.update()                                                  #on remet autant que possible l'écran à jour pour afficher les événements avec le moins de délais

    def set_vol(self,val,List = []):
        volume = int(val) / 100
        for son in List :
            son.set_volume(volume)

    def draw(self):
        """
        fonction dessinant couche sur couche, l'interface pendant le jeu
        """

        self.fenetre.fill(black)                                                 #le fond noir...
        self.fenetre.blit(self.fond,(self.fond_x,0))                             #le fond d'écran du jeu...
        self.fenetre.blit(self.fond2,(self.fond2_x,0))
        self.fenetre.blit(self.fond3,(self.fond3_x,0))
        #self.fenetre.blit(pygame.image.load('images/carrcasse_voiture2.png').convert_alpha(),((self.fond_x +720),310))
        global jauge
        if self.francais == True:
            jauge = text['fr'].draw.jauge
        elif self.anglais == True:
            jauge = text['en'].draw.jauge

        for sprite in self.all_sprites:
            self.fenetre.blit(sprite.image, self.camera.apply(sprite))           #et tous nos sprites destinés à interagir (toutes nos entitées)

        pygame.draw.rect(self.fenetre, rouge,(12,12,self.vie.w-2,16),0)          #affichage de la jauge de vie
        pygame.draw.rect(self.fenetre, black,(10,10,150,20),2)                   #affichage du contour de la jauge
        if self.vie.w <= 30 :                                                    #lorsque la vie est trop faible : jauge en mode urgence
            pygame.draw.rect(self.fenetre, (187, 11, 11),(12,12,self.vie.w-2,18),0)
            pygame.draw.rect(self.fenetre, black,(10,10,150,20),2)
            self.txt(white,2,25,jauge,300,20)                                    #TXT blanc à coté de la jauge
            if self.findevie == True and self.Bruitage == True:
                self.Soundtrack_findevie.play(loops=-1)
                self.findevie = False
            else:
                self.findevie = False
        if self.vie.w >30 :
            self.findevie = True
            self.Soundtrack_findevie.stop()


        Pause = self.boutons(' ',950,10,40,40,gris_fonce,gris_clair)
        self.fenetre.blit(pygame.image.load('images/smallbouton_pause.png').convert_alpha(),(940,0))

        if self.hit >= int(re.sub("\n","",self.registre_score_txt[1])) :

            Chrono = self.txt(white,2,20,str(round(self.temps_final//60)) + " min " + str( round(self.temps_final) - round(self.temps_final//60)*60 ) + " s / " + str(round(float(re.sub("\n","",self.registre_score_txt[0]))//60)) + "min " + str(round(float(re.sub("\n","",self.registre_score_txt[0])) - (float(re.sub("\n","",self.registre_score_txt[0]))//60)*60,2)) + " s " ,120,50)

            if round(float(re.sub("\n","",self.registre_score_txt[0])),3) > self.temps_final :
                pygame.draw.rect(self.fenetre, vertpanneau,((120-Chrono.get_width()//2)-8,35,Chrono.get_width()+16,30),4)

            else :
                pygame.draw.rect(self.fenetre, rouge,((120-Chrono.get_width()//2)-8,35,Chrono.get_width()+16,30),4)

        if Pause :
            self.pause = True

        pygame.display.update()                                                 #ligne permettant la mise à jour des informations précédentes
        pygame.display.flip()                                                   #(principalement utile pour savoir où nouvellement dessiner les sprites qui bougent)

    def dialogue(self):
        """
        Méthode permettant le dialogue avec le PNJ du jeu au LVL1
        """
        global d_b1,d_b1bis,d_b2,d_b2bis,d_b3,d_b3bis
        if self.francais == True:
            d_b1 = text['fr'].dialoge.d_b1
            d_b1bis = text['fr'].dialoge.d_b1bis
            d_b2 = text['fr'].dialoge.d_b2
            d_b2bis = text['fr'].dialoge.d_b2bis
            d_b3 = text['fr'].dialoge.d_b3
            d_b3bis = text['fr'].dialoge.d_b3bis
        elif self.anglais == True:
            d_b1 = text['en'].dialoge.d_b1
            d_b1bis = text['en'].dialoge.d_b1bis
            d_b2 = text['en'].dialoge.d_b2
            d_b2bis = text['en'].dialoge.d_b2bis
            d_b3 = text['en'].dialoge.d_b3
            d_b3bis = text['en'].dialoge.d_b3bis

        if self.all_sprites.has(self.papy) :
            self.personnage.image= pygame.image.load("Sprite/D1.png")
            self.fenetre.blit(pygame.image.load('images/bulle1.png').convert_alpha(),(400,300))
            txt_b1 = self.txt(gris_fonce,1,13,d_b1,500,350)
            txt_b1bis = self.txt(gris_fonce,1,13, d_b1bis,500,370)
            pygame.display.update()
            pygame.time.wait(3000)
            self.fenetre.blit(pygame.image.load('images/bulle1.png').convert_alpha(),(400,300))
            txt_b2 = self.txt(gris_fonce,1,12,d_b2,500,350)
            txt_b2bis = self.txt(gris_fonce,1,12,d_b2bis,500,370)
            pygame.display.update()
            pygame.time.wait(2000)
            self.fenetre.blit(pygame.image.load('images/bulle1.png').convert_alpha(),(400,300))
            txt_b3 = self.txt(gris_fonce,1,13,d_b3,500,350)
            txt_b3bis = self.txt(gris_fonce,1,13, d_b3bis,500,370)
            pygame.display.update()
            pygame.time.wait(2000)
            self.all_sprites.remove(self.papy)

        else:
            self.vie.écoulement = True
            self.personnage.avancer = True
            self.start = True

        pygame.display.update()
        self.horloge.tick(FPS)


    def txt (self,color,police,taille,txt,centreX,centreY) :
            """
            fonction qui crée et affiche un texte de la taille, la police, la couleur et la position voulu : fonction d'optimisation
            """
            if police ==1 :
                TypeTXT= pygame.font.Font("freesansbold.ttf",taille)                 #on crée une variable contenant les caractéristiques du texte (Police et taille) (qu'on choisie en saisissant un chiffre pour choisir la police)
            elif police == 2 :
                TypeTXT= pygame.font.SysFont('berlinsansfb',taille)
            elif police == 3 :
                TypeTXT= pygame.font.Font("",taille)
            Txtsurface = TypeTXT.render(txt,True,color)                              #on crée la surface texte grâce à cette variable, tout en précisant la couleur (Le "True" permettant de valider l'affichage)
            Txtrect = Txtsurface.get_rect()                                          #on l'encadre dans un rectangle, pour mieux le placer, à l'aide des commandes pygame qui facilitent l'utilisation de rectangle
            Txtrect.center = (centreX,centreY)                                       #on définit le centre du bouton comme étant le centre du texte (tout du moins le centre du rectangle qui le contient)
            self.fenetre.blit(Txtsurface,Txtrect)                                    #et l'on projete le tout sur notre fenêtre
            return(Txtsurface)
    def boutons(self,msg,x,y,w,h,color1,color2):
        """
        fonction facilitant la création de bouton interactif (optimisation du code)
        Il existe une deuxième version de ce bouton, dans un fichier à part de celui-ci,
        destiné aux boutons du menu, mais qui nécessite d'être dessiné un par un sur photoshop
        """
        souris = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > souris[0] > x and y+h > souris[1] > y:                          #intervalle représentant la surface du bouton, permettant de regarder si notre souris s'y trouve
            pygame.draw.rect(self.fenetre, color2,(x,y,w,h))                     #si c'est le cas, on change la couleur de notre bouton, pour quelquechose de plus clair (autrement il reste le même)
            smallText = pygame.font.Font("freesansbold.ttf",20)                  #Création du texte sur le bouton (code identique à celui un peu plus bas dans la fonction)
            textSurf= smallText.render(msg,True,black)                           #et copié ici pour éviter que, quand on appuie sur le bouton, le texte "disparaisse" (tout du moins, n'est pas le temps de réapparaitre)
            textRect = textSurf.get_rect()
            textRect.center = ((x+(w//2)), (y+(h//2)))
            self.fenetre.blit(textSurf, textRect)
            if click[0] == 1 and self.declick == True:                           #si l'on est sur le bouton et que l'on fait un clic gauche dessus (bouton [0] de la souris pour pygame)*
                self.declick = False
                self.T=True                                                      #*alors on renvoie un boolén vrai, qui nous servira d'activateur dans une fonction usant de bouton(pour lancer le jeu par exemple)
                if self.Bruitage == True :
                    self.craque.play()
            elif click[0] == 0 :                                                 #cette ligne couplée à cette variable booléenne permet d'éviter d'enchainer deux boutons placer successivement au même endroit (en vérifiant qu'il s'agit bin d'un nouveau click)
                 self.declick = True
                 self.T=False
        else:
            pygame.draw.rect(self.fenetre, color1,(x,y,w,h))                     #ligne permettant de créer notre bouton de couleur "normale", quand la souris n'est pas dessus
            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf= smallText.render(msg,True,black)
            textRect = textSurf.get_rect()
            textRect.center = ((x+(w//2)), (y+(h//2)))
            self.fenetre.blit(textSurf, textRect)
            self.T=False
        return(self.T)




    def règles(self):
        """
        Code pour la page "règles" de notre menu.
        L'accès se fait depuis la page d'accueil du jeu (méthode menu)
        """


        click = pygame.mouse.get_pressed()
        lacher = True
        compteur_regles = 1
        rules1 = True                       #Cette condition permet d'alléger le programme et de "n'imprimer" qu'une fois sur la fenêtre de txt de chaque page de règles
        rules2 = True                       #Ainsi, les éléments qui profitent le plus de cette optimisation, sont ceux avec qui on intéragi (boutons...)
        rules3 = True
        rules4 = True

        global text1,text2,text3
        if self.francais == True:
            text1 = text['fr'].button.exit
            text2 = text['fr'].button.suivant
            text3 = text['fr'].button.precedant
        elif self.anglais == True:

            text1 = text['en'].button.exit
            text2 = text['en'].button.suivant
            text3 = text['en'].button.precedant


        exit = self.boutons(text1, (fenetreL - 60), (fenetreH - 60), 50, 50, marron_fonce, marron_clair)
        pygame.font.Font('freesansbold.ttf', 30)
        suivant = self.boutons(text2, fenetreL - (40 + 20), fenetreH // 2, 30, 30, orange_fonce, orange_clair)
        precedant = self.boutons(text3, 20, fenetreH // 2, 30, 30, orange_fonce, orange_clair)

        flecheD = pygame.image.load('images/fleche_droite.png')
        flecheG = pygame.image.load('images/fleche_gauche.png')
        global text4, regle1_2, regle1_3, regle1_4, regle1_5, regle1_6, regle1_7, regle1_8, regle1_9, regle1_10, regle1_11, regle1_12, regle1_13, regle1_14, regle1_15, regle1_16, regle1_17
        global regle2_2, regle2_3, regle2_4, regle2_5, regle2_6, regle2_7, regle2_8, regle2_9
        global regle3_1, espace, t1, t1bis, t2, t2bis, t3
        global regle4_1, regle4_2, regle4_3, regle4_4, regle4_5, regle4_6, regle4_7, regle4_8, regle4_9, regle4_10, regle4_11, regle4_12, regle4_13, regle4_14
        global regle4_15, regle4_16, regle4_17, regle4_18, regle4_19, regle4_20, regle4_21, regle4_22


        if self.anglais == True:
            text4 = text['en'].regle.txt_regle1
            regle1_2 = text['en'].regle.regle1_2
            regle1_3 = text['en'].regle.regle1_3
            regle1_4 = text['en'].regle.regle1_4
            regle1_5 = text['en'].regle.regle1_5
            regle1_6 = text['en'].regle.regle1_6
            regle1_7 = text['en'].regle.regle1_7
            regle1_8 = text['en'].regle.regle1_8
            regle1_9 = text['en'].regle.regle1_9
            regle1_10 = text['en'].regle.regle1_10
            regle1_11 = text['en'].regle.regle1_11
            regle1_12 = text['en'].regle.regle1_12
            regle1_13 = text['en'].regle.regle1_13
            regle1_14 = text['en'].regle.regle1_14
            regle1_15 = text['en'].regle.regle1_15
            regle1_16 = text['en'].regle.regle1_16
            regle1_17 = text['en'].regle.regle1_17
            regle2_2 = text['en'].regle.regle2_2
            regle2_3 = text['en'].regle.regle2_3
            regle2_4 = text['en'].regle.regle2_4
            regle2_5 = text['en'].regle.regle2_5
            regle2_6 = text['en'].regle.regle2_6
            regle2_7 = text['en'].regle.regle2_7
            regle2_8 = text['en'].regle.regle2_8
            regle2_9 = text['en'].regle.regle2_9
            regle3_1 = text['en'].regle.regle3_1
            espace = text['en'].regle.espace
            t1 = text['en'].regle.t1
            t1bis = text['en'].regle.t1bis
            t2 = text['en'].regle.t2
            t2bis = text['en'].regle.t2bis
            t3 = text['en'].regle.t3
            regle4_1 = text['en'].regle.regle3_1
            regle4_2 = text['en'].regle.regle4_2
            regle4_3 = text['en'].regle.regle4_3
            regle4_4 = text['en'].regle.regle4_4
            regle4_5 = text['en'].regle.regle4_5
            regle4_6 = text['en'].regle.regle4_6
            regle4_7 = text['en'].regle.regle4_7
            regle4_8 = text['en'].regle.regle4_8
            regle4_9 = text['en'].regle.regle4_9
            regle4_10 = text['en'].regle.regle4_10
            regle4_11 = text['en'].regle.regle4_11
            regle4_12 = text['en'].regle.regle4_12
            regle4_13 = text['en'].regle.regle4_13
            regle4_14 = text['en'].regle.regle4_14
            regle4_15 = text['en'].regle.regle4_15
            regle4_16 = text['en'].regle.regle4_16
            regle4_17 = text['en'].regle.regle4_17
            regle4_18 = text['en'].regle.regle4_18
            regle4_19 = text['en'].regle.regle4_19
            regle4_20 = text['en'].regle.regle4_20
            regle4_21 = text['en'].regle.regle4_21
            regle4_22 = text['en'].regle.regle4_22


        elif self.francais == True:
             text4 = text['fr'].regle.txt_regle1
             regle1_2 = text['fr'].regle.regle1_2
             regle1_3 = text['fr'].regle.regle1_3
             regle1_4 = text['fr'].regle.regle1_4
             regle1_5 = text['fr'].regle.regle1_5
             regle1_6 = text['fr'].regle.regle1_6
             regle1_7 = text['fr'].regle.regle1_7
             regle1_8 = text['fr'].regle.regle1_8
             regle1_9 = text['fr'].regle.regle1_9
             regle1_10 = text['fr'].regle.regle1_10
             regle1_11 = text['fr'].regle.regle1_11
             regle1_12 = text['fr'].regle.regle1_12
             regle1_13 = text['fr'].regle.regle1_13
             regle1_14 = text['fr'].regle.regle1_14
             regle1_15= text['fr'].regle.regle1_15
             regle1_16 = text['fr'].regle.regle1_16
             regle1_17 = text['fr'].regle.regle1_17
             regle2_2 = text['fr'].regle.regle2_2
             regle2_3 = text['fr'].regle.regle2_3
             regle2_4 = text['fr'].regle.regle2_4
             regle2_5 = text['fr'].regle.regle2_5
             regle2_6 = text['fr'].regle.regle2_6
             regle2_7 = text['fr'].regle.regle2_7
             regle2_8 = text['fr'].regle.regle2_8
             regle2_9 = text['fr'].regle.regle2_9
             regle3_1 = text['fr'].regle.regle3_1
             espace = text['fr'].regle.espace
             t1 = text['fr'].regle.t1
             t1bis = text['fr'].regle.t1bis
             t2 = text['fr'].regle.t2
             t2bis = text['fr'].regle.t2bis
             t3 = text['fr'].regle.t3
             regle4_1 = text['fr'].regle.regle3_1
             regle4_2 = text['fr'].regle.regle4_2
             regle4_3 = text['fr'].regle.regle4_3
             regle4_4 = text['fr'].regle.regle4_4
             regle4_5 = text['fr'].regle.regle4_5
             regle4_6 = text['fr'].regle.regle4_6
             regle4_7 = text['fr'].regle.regle4_7
             regle4_8 = text['fr'].regle.regle4_8
             regle4_9 = text['fr'].regle.regle4_9
             regle4_10 = text['fr'].regle.regle4_10
             regle4_11 = text['fr'].regle.regle4_11
             regle4_12 = text['fr'].regle.regle4_12
             regle4_13 = text['fr'].regle.regle4_13
             regle4_14 = text['fr'].regle.regle4_14
             regle4_15 = text['fr'].regle.regle4_15
             regle4_16 = text['fr'].regle.regle4_16
             regle4_17 = text['fr'].regle.regle4_17
             regle4_18 = text['fr'].regle.regle4_18
             regle4_19 = text['fr'].regle.regle4_19
             regle4_20 = text['fr'].regle.regle4_20
             regle4_21 = text['fr'].regle.regle4_21
             regle4_22 = text['fr'].regle.regle4_22

        ########################## Boucle des règles ###################################""

        while not exit == True:
            click = pygame.mouse.get_pressed()
            txt_regle1 = self.txt(white,1,40,text4,(fenetreL//2),75)
            exit = self.boutons('Exit',(fenetreL-60),(fenetreH-60),50,50,jaune_fonce,jaune_clair)
            if click[0] == 0:
                    lacher = True
            
            if compteur_regles == 3:                                                            #sous cette condition figure ce qui s'actualise en permence en fonction du numéro de page des règles choisit par l'utilisateur
                

                suivant = self.boutons(" ",fenetreL-35,fenetreH//2,30,60,orange_fonce, orange_clair)
                precedant = self.boutons(" ",5,fenetreH//2,30,60,orange_fonce, orange_clair)
                self.fenetre.blit(flecheD,(fenetreL-35,fenetreH//2))
                self.fenetre.blit(flecheG,(5,fenetreH//2))
                
                if rules1 == True :                                                             #sous cette condition figure ce qui ne s'actualise qu'une fois, dépendant du numéro de page des règles choisit par l'utilisateur
                    
                    rules2 = True

                    self.fenetre.blit(self.fondintro,(0,0))
                    txt_regle1_2 = self.txt(rouge_pale,1,21,regle1_2,(fenetreL//2),140)
                    txt_regle1_3 = self.txt(vert,1,20,regle1_3,(fenetreL//2),200)
                    txt_regle1_4 = self.txt(vert,1,20,regle1_4,(fenetreL//2),220)
                    txt_regle1_5 = self.txt(vert,1,20,regle1_5 ,(fenetreL//2),240)
                    txt_regle1_6 = self.txt(vert,1,20,regle1_6,(fenetreL//2),260)
                    txt_regle1_7 = self.txt(vert,1,20,regle1_7,(fenetreL//2),280)
                    txt_regle1_8 = self.txt(vert,1,20,regle1_8 ,(fenetreL//2),300)
                    txt_regle1_9 = self.txt(vert,1,20,regle1_9,(fenetreL//2),320)
                    txt_regle1_10 = self.txt(vert,1,20,regle1_10,(fenetreL//2),340)
                    txt_regle1_11 = self.txt(vert,1,20,regle1_11,(fenetreL//2),360)
                    txt_regle1_12 = self.txt(vert,1,20,regle1_12 ,(fenetreL//2),380)
                    txt_regle1_13 = self.txt(vert,1,20,regle1_13,(fenetreL//2),400)
                    txt_regle1_14 = self.txt(vert,1,20,regle1_14,(fenetreL//2),420)
                    txt_regle1_15 = self.txt(vert,1,20,regle1_15,(fenetreL//2),440)
                    txt_regle1_16 = self.txt(vert,1,20,regle1_16,(fenetreL//2),460)
                    txt_regle1_17 = self.txt(vert,1,20,regle1_17,(fenetreL//2),480)

                    rules1 = False

            if compteur_regles == 4:

                precedant = self.boutons(" ",5,fenetreH//2,30,60,orange_fonce, orange_clair)
                self.fenetre.blit(flecheG,(5,fenetreH//2))

                if rules2 == True :

                    rules1 = True
                    rules3 = True

                    self.fenetre.blit(self.fondintro,(0,0))
                    txt_regle2_2 = self.txt(vert,1,20,regle2_2,(fenetreL//2),205)
                    txt_regle2_3 = self.txt(vert,1,20,regle2_3,(fenetreL//2),230)
                    txt_regle2_4 = self.txt(vert,1,20,regle2_4,(fenetreL//2),255)
                    txt_regle2_5 = self.txt(vert,1,20,regle2_5,(fenetreL//2),280)
                    txt_regle2_6 = self.txt(vert,1,20,regle2_6,(fenetreL//2),305)
                    txt_regle2_7 = self.txt(vert,1,20,regle2_7,(fenetreL//2),330)
                    txt_regle2_8 = self.txt(vert,1,20,regle2_8,(fenetreL//2),355)
                    txt_regle2_9 = self.txt(vert,1,20,regle2_9,(fenetreL//2),380)

                    rules2 = False

            if compteur_regles == 2:

                suivant = self.boutons(" ",fenetreL-35,fenetreH//2,30,60,orange_fonce, orange_clair)
                precedant = self.boutons(" ",5,fenetreH//2,30,60,orange_fonce, orange_clair)
                self.fenetre.blit(flecheD,(fenetreL-35,fenetreH//2))
                self.fenetre.blit(flecheG,(5,fenetreH//2))

                if rules3 == True :

                    rules2 = True
                    rules4 = True

                    self.fenetre.blit(self.fondintro,(0,0))
                    txt_regle3_1 = self.txt(rouge_pale,1,20,regle3_1,(fenetreL//2),125)
                    self.fenetre.blit(pygame.image.load('images/Espace.png').convert_alpha(),(150,300))
                    txt_espace = self.txt(vert,1,23,espace,300,380)

                    if self.ZQSD :                                                                                  #L'explication des règles s'adapte au choix des commandes de l'utilisateur
                        self.fenetre.blit(pygame.image.load('images/ZQSD-droite.png').convert_alpha(),(600,230))
                    else :
                        self.fenetre.blit(pygame.image.load('images/fleches-droite.png').convert_alpha(),(600,230))

                    txt_t1 = self.txt(vert,1,20,t1,645,380)
                    txt_t1bis = self.txt(vert,1,20,t1bis ,645,405)
                    txt_t2 = self.txt(vert,1,20,t2,800,380)
                    txt_t2bis = self.txt(vert,1,20,t2bis,800,405)
                    txt_t3 = self.txt(vert,1,20,t3,720,210)

                    rules3 = False

            if compteur_regles == 1:

                suivant = self.boutons(" ",fenetreL-35,fenetreH//2,30,60,orange_fonce, orange_clair)
                self.fenetre.blit(flecheD,(fenetreL-35,fenetreH//2))


                if rules4 == True :

                    rules3 = True

                    self.fenetre.blit(self.fondintro,(0,0))
                    txt_regle3_1 = self.txt(rouge_pale,1,20,regle4_1,(fenetreL//2),120)
                    txt_0 = self.txt(vert,2,23,regle4_2,250,190)
                    txt_0 = self.txt(vert,2,23,regle4_3,250,220)
                    txt_0 = self.txt(vert,2,23,regle4_4,250,250)
                    self.fenetre.blit(pygame.image.load('Sprite/globe - 1.png').convert_alpha(),(230,270))
                    txt_1 = self.txt(vert,2,23,regle4_5,700,160)
                    txt_2 = self.txt(vert,2,23,regle4_6,700,190)
                    txt_3 = self.txt(vert,2,23,regle4_7,700,220)
                    txt_4 = self.txt(vert,2,23,regle4_8,700,250)
                    txt_5 = self.txt(vert,2,23,regle4_9,700,280)
                    txt_5 = self.txt(vert,2,23,regle4_10,700,310)
                    self.fenetre.blit(pygame.image.load('Sprite/EnnemieD20.png').convert_alpha(),(880,150))
                    self.fenetre.blit(pygame.image.load('Sprite/traps3.png').convert_alpha(),(890,230))
                    self.fenetre.blit(pygame.image.load('Sprite/piege.png').convert_alpha(),(890,270))
                    txt_6 = self.txt(vert,2,23,regle4_11,500,355)
                    txt_6 = self.txt(vert,2,23,regle4_12,500,385)
                    txt_6 = self.txt(vert,2,23,regle4_13,500,415)
                    self.fenetre.blit(pygame.image.load('Sprite/coffre1.png').convert_alpha(),(80,410))
                    self.fenetre.blit(pygame.image.load('Sprite/Splanete.png').convert_alpha(),(300,453))
                    self.fenetre.blit(pygame.image.load('Sprite/Seringue.png').convert_alpha(),(550,453))
                    self.fenetre.blit(pygame.image.load('Sprite/Rubis.png').convert_alpha(),(800,453))
                    txt_7 = self.txt(violet_clair,2,18,regle4_14,320,440)
                    txt_7 = self.txt(violet_clair,2,18,regle4_15,570,440)
                    txt_7 = self.txt(violet_clair,2,18,regle4_16,820,440)
                    txt_8 = self.txt(violet_clair,2,20,regle4_17,320,520)
                    txt_8 = self.txt(violet_clair,2,20,regle4_18,320,540)
                    txt_8 = self.txt(violet_clair,2,20,regle4_19,570,520)
                    txt_8 = self.txt(violet_clair,2,20,regle4_20,570,540)
                    txt_8 = self.txt(violet_clair,2,20,regle4_21,820,520)
                    txt_8 = self.txt(violet_clair,2,20,regle4_22,820,540)

                    rules4 = False

            if suivant==True and lacher==True :

                if compteur_regles < 4 :

                    lacher = False
                    compteur_regles +=1

            if precedant==True and lacher==True :

                if compteur_regles > 1 :

                    lacher = False
                    compteur_regles = compteur_regles -1
            
            if self.fermeture() :
                exit = True

            pygame.display.update()
            self.horloge.tick(FPS)

    def option(self, choix_difficulté):
        """
        Code pour la page "règles" de notre menu.
        L'accès se fait depuis la page d'accueil du jeu (méthode menu)
        """

        self.fenetre.blit(self.fondintro,(0,0))
        #exit_img = pygame.image.load('images/exit.png').convert_alpha()
        exit = self.boutons('Exit',(fenetreL-60),(fenetreH-60),50,50,jaune_fonce,jaune_clair)
        #exit_button = BUTTON.button((fenetreL - 60), (fenetreH - 60), exit_img,exit_img, 0.7)

        self.slider1 = Slider.Slider((fenetreL//2 + 200, 250),100,self.Sound_hit.get_volume()*200)
        self.slider2 = Slider.Slider((fenetreL // 2 + 200, 325),100,self.Soundtrack_jeu.get_volume()*200)

        # while not exit_button == True :
        while not exit == True:

            if self.francais == True:
                Facile = text['fr'].menu.Facile
                Moyen = text['fr'].menu.Moyen
                Difficile = text['fr'].menu.Difficile
                Son = text['fr'].menu.Son
                Music = text['fr'].menu.Music
                Commandes = text['fr'].menu.Commandes
                Indisponible = text['fr'].menu.Indisponible


            elif self.anglais == True:
                Facile = text['en'].menu.Facile
                Moyen = text['en'].menu.Moyen
                Difficile = text['en'].menu.Difficile
                Son = text['en'].menu.Son
                Music = text['en'].menu.Music
                Commandes = text['en'].menu.Commandes
                Indisponible = text['en'].menu.Indisponible


            ### Affichage des boutons d'option ###
            self.fenetre.blit(self.fondintro,(0,0))

            if choix_difficulté :
                self.facile = self.boutons(Facile,fenetreL//2+75,130,100,50,vert_fonce2,vert_clair2)
                self.moyen = self.boutons(Moyen,fenetreL//2-50,100,100,50,marron_fonce,marron_clair)
                self.difficile = self.boutons(Difficile,fenetreL//2-175,130,100,50,rouge_fonce,rouge_clair)

            else :
                pygame.draw.rect(self.fenetre, rouge_pale,(fenetreL//2-175,100,350,50))
                self.txt(black,1,20,Indisponible,fenetreL//2,125)
                pygame.mixer.pause()                                                    #car si l'on ne peut choisir la difficulté, c'est que l'on est dans le menu pause et donc que la musique ne doit pas se relancer avant d'en être sortie

            exit = self.boutons('Exit',(fenetreL-60),(fenetreH-60),50,50,jaune_fonce,jaune_clair)
            #exit_button = BUTTON.button((fenetreL - 60), (fenetreH - 60), exit_img,exit_img, 0.7)
            self.son = self.boutons(Son,fenetreL//2-50,250,100,50,gris_fonce,gris_clair)
            self.music = self.boutons(Music,fenetreL//2-50,325,100,50,gris_fonce,gris_clair)

            self.commandes = self.boutons(Commandes,fenetreL//2-125,400,250,50,gris_fonce,gris_clair)
            FR = self.boutons('Français',(fenetreL//2)-102,475,100,50,gris_fonce,gris_clair)
            EN = self.boutons('Anglais',(fenetreL//2)+2,475,100,50,gris_fonce,gris_clair)
            
            ### Modification des paramètres en fonction des appuis sur les boutons ###
            if self.fermeture() == True:
                exit = True

            if self.son == True:

                if self.Bruitage == True:
                    self.craque.stop()
                    self.Bruitage = False

                elif self.Bruitage == False:
                    self.craque.play()
                    self.Bruitage =True


            if self.music == True:

                if self.musique == True:
                    self.musique = False
                    if choix_difficulté :                           #Si accès aux paramètres de difficulté, c'est que c'est la musique d'intro qui est à lancer
                        self.Soundtrack_intro.stop()     
                    else :
                        self.Soundtrack_jeu.stop()           #Sinon on active l'autre musique et on attend d'être sorti du menu pause pour relancer la musique


                elif self.musique == False:
                    self.musique =True
                    if choix_difficulté :                           #Si accès aux paramètres de difficulté, c'est que c'est la musique d'intro qui est à lancer
                        self.Soundtrack_intro.play(loops=-1)     
                    else :
                        self.Soundtrack_jeu.play(loops=-1)           #Sinon on active l'autre musique et on attend d'être sorti du menu pause pour relancer la musique

            if choix_difficulté :
                if self.facile == True :

                    if self.start == True:
                        self.start = False

                    #self.start=False
                    self.Health = 10
                    self.hit=4
                    self.min_t1 =7
                    self.max_t1 =20

                if self.moyen == True:
                    if self.start == True:
                        self.start = False

                    self.Health = 8
                    self.hit=5
                    self.min_t1 =6
                    self.max_t1 =15

                if self.difficile == True:
                    self.start = True
                    self.Health= 7
                    self.hit=6
                    self.min_t1 =5
                    self.max_t1 =10

            if self.commandes == True:
                if self.ZQSD == True:
                    self.ZQSD = False
                else:
                    self.ZQSD = True

            if FR :
                self.francais = True
                self.anglais = False
            
            if EN :
                self.anglais = True
                self.francais = False

            ### Affichage des illustrations à coté des boutons ##
            if self.Bruitage == True:
                self.fenetre.blit(self.demute,(fenetreL//2+75,263))
                self.slider1.changeValue()
                self.slider1.render(self.fenetre)

                self.set_vol(self.slider1.getValue(),List=[self.son_piege,self.craque,self.feu,self.Sound_hit,self.Soundtrack_findevie,self.Soundtrack_usine])

            elif self.Bruitage == False:
                self.fenetre.blit(self.mute,(fenetreL//2+75,263))

            if self.musique == True:
                self.fenetre.blit(self.demute,(fenetreL//2+75,338))
                self.slider2.changeValue()
                self.slider2.render(self.fenetre)
                
                self.set_vol(self.slider2.getValue(),List=[self.Orage,self.Soundtrack_intro,self.Soundtrack_win,self.Soundtrack_gameover,self.Soundtrack_jeu])

            elif self.musique == False :
                self.fenetre.blit(self.mute,(fenetreL//2+75,338))

            if self.hit==4 and choix_difficulté:
                pygame.draw.rect(self.fenetre, vert_clair2,(fenetreL//2+75,130,100,50))
                self.txt(black,1,20,Facile,fenetreL//2+125,155)
            
            if self.hit == 5 and choix_difficulté:
                pygame.draw.rect(self.fenetre, marron_clair,(fenetreL//2-50,100,100,50))
                self.txt(black,1,20,Moyen,fenetreL//2,125)
            
            if self.hit == 6 and choix_difficulté:
                self.fenetre.blit(self.Hard,(fenetreL//2-217,132))
                pygame.draw.rect(self.fenetre, rouge_clair,(fenetreL//2-175,130,100,50))
                self.txt(black,1,20,Difficile,fenetreL//2-125,155)

            if self.ZQSD :
                self.fenetre.blit(pygame.transform.scale(pygame.image.load('images/ZQSD-droite.png').convert_alpha(), (92,48)),(fenetreL//2+130,400))

            elif not self.ZQSD :
                self.fenetre.blit(pygame.transform.scale(pygame.image.load('images/fleches-droite.png').convert_alpha(), (92,48)),(fenetreL//2+130,400))
            
            if self.francais :
                pygame.draw.rect(self.fenetre, gris_clair,((fenetreL//2)-102,475,100,50))
                self.txt(black,1,20,"Français",(fenetreL//2)-52,500)

            elif self.anglais :
                pygame.draw.rect(self.fenetre, gris_clair,((fenetreL//2)+2,475,100,50))
                self.txt(black,1,20,"Anglais",(fenetreL//2)+52,500)

            pygame.display.update()

    def delais(self,temps) :
        """
        Fonction d'optimisation : remplace "pygame.time.delay(X ms)"
        Permet de mettre un délais à l'affichage, tout en 
        """
        temps_depart = time.time()                                #On travaille avec des millisecondes pour plus de précision
        temps_final = 0
        exit = False

        while exit == False :
            temps_final = (time.time() - temps_depart) *1000           #temps mis à jour jusqu'a atteindre le délais voulu
            if temps < temps_final:
                exit = True
            if self.END == True :
                exit = True
                
            self.fermeture()                                            #on continu de vérifier que le joueur ne souhaite pas fermer la fenêtre de jeu
        


    def menu(self):
        """
        Méthode renfermant la boucle de menu du jeu.
        Elle donne accès également aux méthodes option et règles
        """

        self.niveau = 1     #Chaque retour au menu nous ramène au début du jeu, niveau 1
        start_img = pygame.image.load('images/start_btn.png').convert_alpha()
        rules_img = pygame.image.load('images/rules_btn.png').convert_alpha()
        options_img = pygame.image.load('images/options_btn.png').convert_alpha()
        credits_img = pygame.image.load('images/credits_btn.png').convert_alpha()
        st = pygame.image.load('images/st.png').convert_alpha()
        ru = pygame.image.load('images/ru.png').convert_alpha()
        op = pygame.image.load('images/op.png').convert_alpha()
        cr = pygame.image.load('images/cr.png').convert_alpha()

##################################################Primo boucle du jeu (animation d'intro et choix de la langue)#########################
        if self.musique == True :
          self.Soundtrack_intro.play(loops=-1)

        if self.first == True :
            self.delais(4000)
            ###########################Choix langue#################
            ChoixLangue = False
            while not ChoixLangue :
                self.fenetre.fill(black)                                                 #le fond noir...
                self.fenetre.blit(self.fond_langues,(0,0))   
                self.francais = self.boutons('Français',(fenetreL//2)-15,275,100,50,violet_fonce,violet_clair)#on appelle notre fonction bouton(ici bouton des langues), dont les booléens seront stockés dans les variables choisies
                self.anglais = self.boutons('Anglais',(fenetreL//2)-15,200,100,50,vert_fonce,vert_clair)
                #on vérifie que l'utilisateur ne ferme pas la fenêtre
                self.fermeture()
                              
                if self.francais or self.anglais or self.END :                                      #Variable nous permettant de sortir de la boucle une fois notre choix effectué
                    ChoixLangue = True
                pygame.display.update()

            if self.first == True :                                              #on vérifie que la condition est toujours vrai et que l'utilisateur ne souhaite pas quitter le jeu
                ########################### mise en scène d'intro et animation de début de jeu #################
                if self.francais :
                    self.fenetre.fill(black)                                                 #le fond noir...
                    self.fenetre.blit(self.fond_langues,(0,0))   
                    self.boutons('Français',(fenetreL//2)-15,275,100,50,violet_clair,violet_clair)
                    pygame.display.update()
                    self.delais(500)

                if self.anglais:
                    self.fenetre.fill(black)                                                 #le fond noir...
                    self.fenetre.blit(self.fond_langues,(0,0))   
                    self.boutons('Anglais',(fenetreL//2)-15,200,100,50,vert_clair,vert_clair)
                    pygame.display.update()
                    self.delais(500)

                self.fenetre.blit(self.fondintro,(0,0))
                pygame.display.update()
                self.delais(1000)
                self.txt(rouge_fonce,1,100,"The Survivor",fenetreL//2,75)
                pygame.display.update()
                self.delais(1000)
                BStart = BUTTON.button((fenetreL // 2 -50 ), 265, start_img, st,0.8,self.Bruitage,self.craque.get_volume())
                BStart.draw(self.fenetre)
                pygame.display.update()
                self.delais(1000)

                self.first = False
                
        global Regle,Start,Option,Credits,Facile,Moyen,Difficile,Son,Music,Commandes,credits1,credits2,credits3,credits4,credits5,credit6,credits7, credits8, Score1, Score2, Score3, Score4, Score5, Score6, Score7, Score8

        NOM = self.txt(rouge_clair,1,17,re.sub("\n","",(self.registre_score_txt)[3]),fenetreL//2+30,fenetreH//5+80)

####################################### Début de la boucle du menu #####################################################################
        while self.intro == True :                                               #on crée une boucle faisant tourner en boucle la page du menu et qui permet la mise à jour de son fond et ses boutons(le tout ne s'arrêtant que si l'on quitte ou l'on joue)
            
            self.fenetre.blit(self.fondintro,(0,0))                              #on projette le fond sur la fenêtre aux coordonnées (point en haut à gauche de l'image) 0,0, de sorte que les bords de l'image et de notre fenêtre soient confondus
            self.txt(rouge_fonce,1,100,"The Survivor",fenetreL//2,75)

            #on appelle notre fonction bouton(ici bouton des règles), dont les booléens seront stockés dans les variables choisies
            BScore = self.boutons("",(fenetreL//2)-20-(max(NOM.get_width()+10,120)-100)//2,fenetreH//5+40,max(NOM.get_width()+10,120),60,vertpanneau,marron_clair)
            self.txt(black,1,19,"High score :",fenetreL//2+32,fenetreH//5+58)
            NOM = self.txt(rouge_clair,1,17,re.sub("\n","",(self.registre_score_txt)[3]),fenetreL//2+30,fenetreH//5+80)
           #on appelle notre fonction bouton(ici bouton démarrage du jeu), dont les booléens seront stockés dans les variables choisies
            #Bniveau = self.boutons("LVL %s" % self.niveau,fenetreL // 2 -20,215,100,50,marron_fonce,marron_clair)
            BStart = BUTTON.button((fenetreL // 2 -50 ), 265, start_img, st,0.8,self.Bruitage,self.craque.get_volume())
            BRegle = BUTTON.button((fenetreL // 2 -50 ) , 340, rules_img,ru, 0.8,self.Bruitage,self.craque.get_volume())
            BOption = BUTTON.button((fenetreL // 2 -50 ) , 415, options_img,op, 0.8,self.Bruitage,self.craque.get_volume())
            BCredits = BUTTON.button(fenetreL // 2 -50 , 490, credits_img,cr, 0.8,self.Bruitage,self.craque.get_volume())
            if self.francais == True:
                Regle = text['fr'].menu.Regle
                Start = text['fr'].menu.Start
                Option = text['fr'].menu.Option
                Credits = text['fr'].menu.Credits
                credits1 = text['fr'].credit.credits1
                credits2 = text['fr'].credit.credits2
                credits3 = text['fr'].credit.credits3
                credits4 = text['fr'].credit.credits4
                credits5 = text['fr'].credit.credits5
                credits6 = text['fr'].credit.credits6
                credits7 = text['fr'].credit.credits7
                credits8 = text['fr'].credit.credits8
                Facile = text['fr'].menu.Facile
                Moyen = text['fr'].menu.Moyen
                Difficile = text['fr'].menu.Difficile
                Score1 = text['fr'].menu.Score1
                Score2 = text['fr'].menu.Score2
                Score3 = text['fr'].menu.Score3
                Score4 = text['fr'].menu.Score4
                Score5 = text['fr'].menu.Score5
                Score6 = text['fr'].menu.Score6
                Score7 = text['fr'].menu.Score7
                Score8 = text['fr'].menu.Score8         
                
            elif self.anglais == True:
                Regle = text['en'].menu.Regle
                Start = text['en'].menu.Start
                Option = text['en'].menu.Option
                Credits = text['en'].menu.Credits
                credits1 = text['en'].credit.credits1
                credits2 = text['en'].credit.credits2
                credits3 = text['en'].credit.credits3
                credits4 = text['en'].credit.credits4
                credits5 = text['en'].credit.credits5
                credits6 = text['en'].credit.credits6
                credits7 = text['en'].credit.credits7
                credits8 = text['en'].credit.credits8
                Facile = text['en'].menu.Facile
                Moyen = text['en'].menu.Moyen
                Difficile = text['en'].menu.Difficile
                Score1 = text['en'].menu.Score1
                Score2 = text['en'].menu.Score2
                Score3 = text['en'].menu.Score3
                Score4 = text['en'].menu.Score4
                Score5 = text['en'].menu.Score5
                Score6 = text['en'].menu.Score6
                Score7 = text['en'].menu.Score7
                Score8 = text['en'].menu.Score8
            
            self.fermeture()                                             #et la boucle qui suit, celle du jeu
            
            if BRegle.draw(self.fenetre):                                                  #et on vérifie que l'on ne clique pas dessus, autrement ils activent l'action (désigné par la focntion) a laquelle ils sont rattachés
                self.règles()
            
            if BScore == True :
                self.fenetre.blit(self.fondintro,(0,0))
                
                if re.sub("\n","",(self.registre_score_txt)[1]) == "4":
                    difficulte = Facile
                elif re.sub("\n","",(self.registre_score_txt)[1]) == "5":
                    difficulte = Moyen
                elif re.sub("\n","",(self.registre_score_txt)[1]) == "6":
                    difficulte = Difficile

                self.txt(orange, 1, 35, Score1 ,(fenetreL // 2), 100)
                self.txt(jaune_clair, 1, 45, re.sub("\n","",(self.registre_score_txt)[3]),(fenetreL // 2), 160)
                self.txt(orange, 1, 28, Score2 + str(round(float(re.sub("\n","",self.registre_score_txt[0]))//60)) + Score6 + str(round(float(re.sub("\n","",self.registre_score_txt[0])) - (float(re.sub("\n","",self.registre_score_txt[0]))//60)*60,2)) + Score7 + difficulte + Score8, (fenetreL // 2), 255)
                self.txt(orange, 1, 28, Score3 + re.sub("\n","",(self.registre_score_txt)[2]) + Score4 + re.sub("\n","",(self.registre_score_txt)[4]) + Score5, (fenetreL // 2), 330)
                exit = False
                while not exit == True :
                    exit = self.boutons('Exit',(fenetreL-60),(fenetreH-60),50,50,jaune_fonce,jaune_clair)
                    if self.fermeture() :
                        exit = True

                    pygame.display.update()


            if BOption.draw(self.fenetre):
                self.option(True)

            if BCredits.draw(self.fenetre):
                self.fenetre.blit(self.fondintro,(0,0))
                
                self.txt(orange, 1, 25, credits1,(fenetreL // 2), 130)
                self.txt(orange, 1, 20, credits2,(fenetreL // 2), 180)
                self.txt(orange, 1, 20, credits3, (fenetreL // 2), 205)
                self.txt(orange, 1, 20, credits4,(fenetreL // 2), 230)
                self.txt(orange, 1, 20, credits5, (fenetreL // 2), 255)
                self.txt(orange, 1, 20, credits6, (fenetreL // 2), 280)
                self.txt(orange, 1, 20, credits7, (fenetreL // 2), 305)
                self.txt(orange, 1, 20, credits8, (fenetreL // 2), 330)
                exit = False

                while not exit == True :
                    exit = self.boutons('Exit',(fenetreL-60),(fenetreH-60),50,50,jaune_fonce,jaune_clair)
                    if self.fermeture() :
                        exit = True

                    pygame.display.update()

            if BStart.draw(self.fenetre):

                self.temps_final = 0
                self.nbr_tentatives = self.nbr_tentatives +1
                
                self.Soundtrack_intro.stop()
                if self.Bruitage == True:
                    self.Orage.play()
                self.fenetre.fill(white)
                pygame.display.update()
                self.delais(250)
                self.txt(rouge_fonce,1,100,"The Survivor",fenetreL//2,fenetreH//5)
                self.fenetre.blit(self.fondintrobis,(0,0))
                # BStart = self.boutons(Start,(fenetreL//2)-40,250,150,75,vert_fonce,vert_clair)
                BStart = BUTTON.button((fenetreL // 2 -50 ), 265, start_img, st,0.8,self.Bruitage,self.craque.get_volume())
                BStart.draw(self.fenetre)
                pygame.display.update()
                self.delais(3250)
                self.fenetre.fill(black)
                pygame.display.update()
                self.delais(1500)
                if self.musique == True:
                    self.Soundtrack_jeu.play(loops=-1)
                self.first = True
                self.intro = False                                               #et on met fin à l'intro pour enchainer sur la boucle suivante, le jeu
                self.started_time = time.time()
            
            pygame.display.update()                                              #on met le tout à jour
            self.horloge.tick(FPS)                                               #avec un temps de rafraichissement définit

    def game_over (self):
        """
        fonction qui affiche notre page game over et propose plusieurs issues au joueur
        """

        self.Soundtrack_jeu.stop()
        global GO,com,retour,rejouer
        if self.francais == True:
            GO = text['fr'].gameover.GO
            com = text['fr'].gameover.com
            retour = text['fr'].gameover.retour
            rejouer = text['fr'].gameover.rejouer
        elif self.anglais == True:
            GO = text['en'].gameover.GO
            com = text['en'].gameover.com
            retour = text['en'].gameover.retour
            rejouer = text['en'].gameover.rejouer
        if self.first==True:
            self.first = False
            if self.Bruitage == True:
                self.Soundtrack_gameover.play()
        self.degat = False                                                          #permet de garantir l'abscence de bruits parasites dû au jeu en arrière plan
        self.fenetre.blit(pygame.image.load('images/fond-flammes.jpg').convert(),(0,0))
        self.fenetre.blit(pygame.image.load('images/Earth - Copie.png').convert_alpha(),(300,170))
        self.txt(white,2,60,GO,500,40)
        self.txt(white,2,25,com,500,90)

        if self.hit == 6 :                                                          #si l'on est en mode difficile, alors chaque mort nous renvoi au tout début du jeu
            self.niveau = 1

        retour_menu = self.boutons(retour,40,400,200,50,bleu_fonce2,bleu_clair2)
        rejouer = self.boutons(rejouer,750,400,200,50,vert_fonce2,vert_clair2)


        if retour_menu :
            self.Soundtrack_gameover.stop()
            self.degat = True
            self.first = False
            self.intro = True
            self.gameover = False
            self.Start()

        if rejouer :
            if self.musique == True :
                self.Soundtrack_jeu.play(loops=-1)
            if not self.hit == 6 :
                self.start = False
            self.Soundtrack_gameover.stop()
            self.degat = True
            self.first = True
            self.intro = True
            self.gameover = False
            self.nbr_tentatives = self.nbr_tentatives +1
            
            self.nouveau()


        pygame.display.update()
        self.horloge.tick(60)
        pygame.display.flip()


    def put_pause(self):
        """
        fonction qui affiche notre menu pause et renvoie plusieurs issues au joueur
        """
        pygame.mixer.pause()
        self.fenetre.blit(pygame.image.load('images/Fond_intro.jpg').convert(),(0,0))
        pause_txt= self.txt(white,2,90,"Pause",500,70)
        global Reprendre,Recommencer,Retour_menu2
        if self.francais == True:
            Reprendre = text['fr'].putpause.Reprendre
            Option = text['fr'].menu.Option
            Recommencer = text['fr'].putpause.Recommencer
            Retour_menu2 = text['fr'].putpause.Retour_menu2
        elif self.anglais == True:
            Reprendre = text['en'].putpause.Reprendre
            Option = text['en'].menu.Option
            Recommencer = text['en'].putpause.Recommencer
            Retour_menu2 = text['en'].putpause.Retour_menu2

        reprendre = self.boutons(Reprendre,400,200,200,50,bleu_fonce,bleu_clair)
        recommencer = self.boutons(Recommencer,400,275,200,50,vert_fonce2,vert_clair2)
        retour_menu2 = self.boutons(Retour_menu2,400,350,200,50,bleu_fonce2,bleu_clair2)
        BOption = self.boutons(Option,400,425,200,50,violet_fonce,violet_clair)

        if reprendre :
            if self.musique :
                pygame.mixer.unpause()
            self.pause = False

        if BOption == True:
            self.option(False)

        if recommencer :
            self.Soundtrack_jeu.stop()
            self.Soundtrack_findevie.stop()
            if self.musique == True :
                self.Soundtrack_jeu.play(loops=-1)
            if not self.hit == 6 :
                self.start = False
            self.degat = True
            self.first=True
            self.pause = False
            self.intro = True
            self.fond_x = -50
            self.fond2_x = 1230
            self.fond3_x = 2210
            self.nbr_tentatives = self.nbr_tentatives +1
            
            self.nouveau()

        if retour_menu2 :
            self.Soundtrack_jeu.stop()
            self.Soundtrack_findevie.stop()
            self.degat = True
            self.first = False
            self.pause = False
            self.intro = True
            self.fond_x = -50
            self.fond2_x = 1230
            self.fond3_x = 2210
            exit = True
            self.Start()

        pygame.display.update()
        self.horloge.tick(60)

    def win(self):
        """
        Méthode qui affiche la victoire du joueur et lui permet de l'enregistrer dans le cas où le record est battu.
        Elle lui renvoie également plusieurs issues.
        """
        self.Soundtrack_jeu.stop()
        self.Soundtrack_findevie.stop()
        if self.first == True :
            self.fondwin = pygame.image.load("images/HappyEarth.jpg")
            self.Usine = pygame.image.load("images/EndUsine.png")
            self.fenetre.fill(black)
            if self.Bruitage == True :
                self.Soundtrack_usine.play()
            pygame.display.update()
            self.delais(3000)
            self.fenetre.blit(self.Usine,(0,0))
            pygame.display.update()
            self.delais(5000)
            self.fenetre.fill(black)
            pygame.display.update()
            if self.Bruitage == True :
                self.Soundtrack_win.play()

            self.delais(2500)


            global win11
            if self.francais :
                win11 = text['fr'].win.win11
            elif self.anglais :
                win11 = text['en'].win.win11

            self.user_text = win11
            
            self.first = False


        global menu1,Rejouer2,win,win1,win2,win3,win4,win5,win6,win7,win8,win9,win10,win12
        if self.francais == True:
            menu1 = text['fr'].win.menu
            Rejouer2 = text['fr'].win.Rejouer2
            win = text['fr'].win.win
            win1 = text['fr'].win.win1
            win2 = text['fr'].win.win2
            win3 = text['fr'].win.win3
            win4 = text['fr'].win.win4
            win5 = text['fr'].win.win5
            win6 = text['fr'].win.win6
            win7 = text['fr'].win.win7
            win8 = text['fr'].win.win8
            win9 = text['fr'].win.win9
            win10 = text['fr'].win.win10
            win12 = text['fr'].win.win12

        elif self.anglais == True:
            menu1 = text['en'].win.menu
            Rejouer2 = text['en'].win.Rejouer2
            win = text['en'].win.win
            win1 = text['en'].win.win1
            win2 = text['en'].win.win2
            win3 = text['en'].win.win3
            win4 = text['en'].win.win4
            win5 = text['en'].win.win5
            win6 = text['en'].win.win6
            win7 = text['en'].win.win7
            win8 = text['en'].win.win8
            win9 = text['en'].win.win9
            win10 = text['en'].win.win10
            win12 = text['en'].win.win12

        self.fenetre.blit(self.fondwin,(0,0))

        self.txt(black, 1, 40, win, fenetreL // 2, 130)
        self.txt(black, 1, 18, win1, fenetreL // 6, 200)
        self.txt(black, 1, 18, win2, fenetreL // 6, 225)
        self.txt(black, 1, 18, win3 , fenetreL // 6, 250)
        self.txt(black, 1, 18, win4, fenetreL // 6, 275)
        self.txt(black, 1, 18, win5, 5*fenetreL // 6, 200)
        self.txt(black, 1, 18, win6 , 5*fenetreL // 6, 225)
        self.txt(black, 1, 18, win7, 5*fenetreL // 6, 250)
        self.txt(black, 1, 18, win8, 5*fenetreL // 6, 275)
        
        # Format enregistrement meilleur score : Score-Temps, difficulté, Date, Nom, nbr tentative
        
        if self.hit >= int(re.sub("\n","",(self.registre_score_txt)[1])) :
            if float(re.sub("\n","",(self.registre_score_txt)[0])) > self.temps_final :
                if self.saisi == 2 :
                    self.registre_score = open("HighScore.txt","w")
                    List_resultat = [str(self.temps_final)+"\n", str(self.hit)+"\n", str(datetime.date.today().strftime("%d/%m/%Y"))+"\n", self.user_text+"\n",str(self.nbr_tentatives)+"\n"]
                    self.registre_score.writelines(List_resultat)
                    self.registre_score.close()
                    self.saisi = 3
                    self.registre_score = open("HighScore.txt","r") 
                    self.registre_score_txt = self.registre_score.readlines()

                elif self.saisi == 3 :
                    Menu = self.boutons(menu1,fenetreL//2-100,500,200,50,violet_fonce,violet_clair)

                    rejouer2 = self.boutons(Rejouer2,fenetreL-125,500,100,50,vert_fonce,vert_clair)
                
                    if rejouer2 :
                        if not self.hit == 6 :
                            self.start = False
                        if self.musique== True :
                            self.Soundtrack_jeu.play(loops=-1)
                        self.niveau = 1
                        self.degat = True
                        self.first = True
                        self.intro = True
                        self.Win = False
                        self.nbr_tentatives = self.nbr_tentatives +1
                        
                        self.started_time = time.time()
                        self.nouveau()

                    elif Menu :
                        self.degat = True
                        self.first = False
                        self.Win = False
                        self.intro = True
                        self.Start()
                else:
                    self.txt(bleu_clair2,1,22,win9,fenetreL//2,50)
                    if len(self.user_text)>20 and not self.user_text == win11 :
                        self.txt(rouge,2,15,win12,fenetreL//2,fenetreH//2)
                    else :
                        self.txt(black,2,15,win10,fenetreL//2,fenetreH//2)

                    #création de variable local pour la zone de saisie txt
                    # basic font for user typed
                    base_font = pygame.font.Font(None, 30)
                    
                    text_surface = base_font.render(self.user_text, True, (255, 255, 255))
                    
                    # create rectangle
                    # set width of textfield so that text cannot get
                    # outside of user's text input
                    self.input_rect = pygame.Rect(fenetreL//2-max(100, text_surface.get_width()+10)//2, fenetreH//2-40, max(100, text_surface.get_width()+10), 32)
                    
                    if self.active:
                        color = jaune_clair
                    else:
                        color = jaune_fonce
                        
                    # draw rectangle and argument passed which should
                    # be on screen
                    pygame.draw.rect(self.fenetre, color, self.input_rect)
                    
                    # render at position stated in arguments
                    self.fenetre.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))

            else :
                Menu = self.boutons(menu1,fenetreL//2-100,500,200,50,violet_fonce,violet_clair)

                rejouer2 = self.boutons(Rejouer2,fenetreL-125,500,100,50,vert_fonce,vert_clair)
            
                if rejouer2 :
                    if not self.hit == 6 :
                        self.start = False
                    if self.musique== True :
                        self.Soundtrack_jeu.play(loops=-1)
                    self.niveau = 1
                    self.degat = True
                    self.first = True
                    self.intro = True
                    self.Win = False
                    self.nbr_tentatives = self.nbr_tentatives +1
                    
                    self.started_time = time.time()
                    self.nouveau()

                elif Menu :
                    self.degat = True
                    self.first = False
                    self.Win = False
                    self.intro = True
                    self.Start()
        else :
            Menu = self.boutons(menu1,fenetreL//2-100,500,200,50,violet_fonce,violet_clair)

            rejouer2 = self.boutons(Rejouer2,fenetreL-125,500,100,50,vert_fonce,vert_clair)
        
            if rejouer2 :
                if not self.hit == 6 :
                    self.start = False
                if self.musique== True :
                    self.Soundtrack_jeu.play(loops=-1)
                self.niveau = 1
                self.degat = True
                self.first = True
                self.intro = True
                self.Win = False
                self.nbr_tentatives = self.nbr_tentatives +1
                
                self.started_time = time.time()
                self.nouveau()

            elif Menu :
                self.degat = True
                self.first = False
                self.Win = False
                self.intro = True
                self.Start()
        
        pygame.display.update()


    def Start(self) :
        """
        fonction qui lance le menu, puis le jeu une fois celui- ci fini, et enfin ferme le tout une fois le jeu terminé
        """
        self.menu()
        while not self.END:
            self.nouveau()
        pygame.quit()
        quit()

Jeu = jeu()
Jeu.Start()