# -*- coding: utf-8 -*-
import socket, sys, threading
from tkinter import *
from tkinter.messagebox import *
from threading import Timer
import tkinter.font as font

host = 'Localhost'
port = 20000

lancement = False

right = False
left = False
up = False
left = False

sendpacman = False
sendfantome1 = False
sendfantome2 = False
sendfantome3 = False

fantome_dead = 0

fichier = open("log.txt", "w")

class bcolors:
    AUCLIENT = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    SERVEUR = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class Tableau:
    """gestion du level"""

    def __init__(self):
        self.level = 'level.txt'
        self.tableau = []

    def open(self):
        """ouverte d'un fichier"""

        file = open(self.level, "r")
        read = file.read()
        self.tableau = list(read.split("\n"))

    def place(self):
        for i_ligne in range(len(self.tableau)):
            ligne = self.tableau[i_ligne]
            for i_colonne in range(len(ligne)):
                if ligne[i_colonne] == '2':
                    canvas.create_oval(i_colonne * 20 + 3, i_ligne * 20 + 3, i_colonne * 20 + 16, i_ligne * 20 + 16, fill='#F16446', outline='#F16446')
                if ligne[i_colonne] == '1':
                    canvas.create_rectangle(i_colonne * 20, i_ligne * 20, i_colonne * 20 + 20, i_ligne * 20 + 20, fill='#000', outline='#000')
                if ligne[i_colonne] == '0':
                    canvas.create_oval(i_colonne * 20 + 7, i_ligne * 20 + 7, i_colonne * 20 + 13, i_ligne * 20 + 13, fill='#fff')

class Pacman:
    """gestion du perso"""

    def __init__(self, x, y):
        self.pacman = canvas.create_oval(x, y, x + 18, y + 18, fill='yellow')
        self.x = 0
        self.y = 0
        self.connexion = connexion
        self.score = 0
        self.vie = 3
        self.compteur_vie = Label(text='Vie = 3', bg='black', fg='white')
        #self.compteur_vie.grid(row=0, column=1, columnspan=1)
        self.compteur = Label(text='Score = 0', bg='black', fg='white')
        #self.compteur.grid(row=0, column=1, columnspan=3)
        self.attente_connexion = Label(text='Joueur co : 0/4', bg='black', fg='white')
        self.attente_connexion.grid(row=0, column=3, columnspan=3)
        self.eat_fant = False
    
    def win(self):
        if self.score == 176:
            showinfo("Pacman", "Vous avez gagné!")
            fen.destroy()

    def timeout(self):
        self.eat_fant = False
        canvas.itemconfig(self.pacman, fill='yellow')


    def deplace_r(self):
        if lancement:
            self.x = int(canvas.coords(self.pacman)[0] // 20)
            self.y = int(canvas.coords(self.pacman)[1] // 20)
            if (self.x, self.y) == (18, 9):
                self.x, self.y = 0, 9
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.y][self.x + 1] != '1':
                    self.x += 1
                    if sendpacman == True:
                        message = "deplace:right"
                        self.connexion.send(message.encode("Utf8"))
                        if self.x == joueurf1.x and self.y == joueurf1.y - 1 or self.x == joueurf2.x and self.y == joueurf2.y - 1 or self.x == joueurf3.x and self.y == joueurf3.y - 1 :
                            if self.eat_fant:
                                if self.x == joueurf1.x and self.y == joueurf1.y - 1:
                                    message = "Fin:P-F1"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F1")
                                elif self.x == joueurf2.x and self.y == joueurf2.y - 1:
                                    message = "Fin:P-F2"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F2")
                                else:
                                    message = "Fin:P-F3"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F3")
                            else:
                                message = "Fin:F-P"
                                self.connexion.send(message.encode("Utf8"))
                                fin("F-P")
                    bille = canvas.find_enclosed(self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)
                    if len(bille) != 0:
                        for element in bille:
                            if element == 282 or element == 296 or element == 60 or element == 74:
                                canvas.itemconfig(self.pacman, fill='red')
                                self.eat_fant = True
                                t = Timer(8.0, self.timeout)
                                t.start()
                            canvas.delete(bille[0])
                            self.score += 1
                            self.compteur.configure(text='score = ' + str(self.score))
            canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)
            self.win()

    def deplace_l(self):
        if lancement:
            self.x = int(canvas.coords(self.pacman)[0] // 20)
            self.y = int(canvas.coords(self.pacman)[1] // 20)
            if (self.x, self.y) == (0, 9):
                self.x, self.y = 18, 9
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.y][self.x - 1] != '1':
                    self.x -= 1
                    if sendpacman == True:
                        message = "deplace:left"
                        self.connexion.send(message.encode("Utf8"))
                        if self.x == joueurf1.x and self.y == joueurf1.y - 1 or self.x == joueurf2.x and self.y == joueurf2.y - 1 or self.x == joueurf3.x and self.y == joueurf3.y - 1 :
                            if self.eat_fant:
                                if self.x == joueurf1.x and self.y == joueurf1.y - 1:
                                    message = "Fin:P-F1"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F1")
                                elif self.x == joueurf2.x and self.y == joueurf2.y - 1:
                                    message = "Fin:P-F2"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F2")
                                else:
                                    message = "Fin:P-F3"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F3")
                            else:
                                message = "Fin:F-P"
                                self.connexion.send(message.encode("Utf8"))
                                fin("F-P")
                    bille = canvas.find_enclosed(self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)
                    if len(bille) != 0:
                        for element in bille:
                            if element == 282 or element == 296 or element == 60 or element == 74:
                                canvas.itemconfig(self.pacman, fill='red')
                                self.eat_fant = True
                                t = Timer(8.0, self.timeout)
                                t.start()
                            canvas.delete(bille[0])
                            self.score += 1
                            self.compteur.configure(text='score = ' + str(self.score))
            canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)
            self.win()

    def deplace_u(self):
        if lancement:
            self.x = int(canvas.coords(self.pacman)[0] // 20)
            self.y = int(canvas.coords(self.pacman)[1] // 20)
            if self.x < len(tab.tableau[0]):
                if tab.tableau[self.y - 1][self.x] != '1':
                    self.y -= 1
                    if sendpacman == True:
                        message = "deplace:up"
                        self.connexion.send(message.encode("Utf8"))
                        if self.x == joueurf1.x and self.y == joueurf1.y - 1 or self.x == joueurf2.x and self.y == joueurf2.y - 1 or self.x == joueurf3.x and self.y == joueurf3.y - 1 :
                            if self.eat_fant:
                                if self.x == joueurf1.x and self.y == joueurf1.y - 1:
                                    message = "Fin:P-F1"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F1")
                                elif self.x == joueurf2.x and self.y == joueurf2.y - 1:
                                    message = "Fin:P-F2"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F2")
                                else:
                                    message = "Fin:P-F3"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F3")
                            else:
                                message = "Fin:F-P"
                                self.connexion.send(message.encode("Utf8"))
                                fin("F-P")
                    bille = canvas.find_enclosed(self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)
                    if len(bille) != 0:
                        for element in bille:
                            if element == 282 or element == 296 or element == 60 or element == 74:
                                canvas.itemconfig(self.pacman, fill='red')
                                self.eat_fant = True
                                t = Timer(8.0, self.timeout)
                                t.start()
                            canvas.delete(bille[0])
                            self.score += 1
                            self.compteur.configure(text='score = ' + str(self.score))
            canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)
            self.win()

    def deplace_d(self):
        if lancement:
            self.x = int(canvas.coords(self.pacman)[0] // 20)
            self.y = int(canvas.coords(self.pacman)[1] // 20)
            if self.x < len(tab.tableau[0]):
                if tab.tableau[self.y + 1][self.x] != '1':
                    self.y += 1
                    if sendpacman == True:
                        message = "deplace:down"
                        self.connexion.send(message.encode("Utf8"))
                        if self.x == joueurf1.x and self.y == joueurf1.y - 1 or self.x == joueurf2.x and self.y == joueurf2.y - 1 or self.x == joueurf3.x and self.y == joueurf3.y - 1 :
                            if self.eat_fant:
                                if self.x == joueurf1.x and self.y == joueurf1.y - 1:
                                    message = "Fin:P-F1"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F1")
                                elif self.x == joueurf2.x and self.y == joueurf2.y - 1:
                                    message = "Fin:P-F2"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F2")
                                else:
                                    message = "Fin:P-F3"
                                    self.connexion.send(message.encode("Utf8"))
                                    fin("P-F3")
                            else:
                                message = "Fin:F-P"
                                self.connexion.send(message.encode("Utf8"))
                                fin("F-P")
                    bille = canvas.find_enclosed(self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)  
                    if len(bille) != 0:
                        for element in bille:
                            if element == 282 or element == 296 or element == 60 or element == 74:
                                canvas.itemconfig(self.pacman, fill='red')
                                self.eat_fant = True
                                t = Timer(8.0, self.timeout)
                                t.start()
                            canvas.delete(bille[0])
                            self.score += 1
                            self.compteur.configure(text='score = ' + str(self.score))
            canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)
            self.win()


class Fantome:
    """gestion du perso"""

    def __init__(self, x, y, couleur, numero): 
        self.player = canvas.create_polygon(x, y, x + 10, y -20, x + 20, y, fill=couleur)
        self.x = 0
        self.y = 0
        self.connexion = connexion
        if numero == 1:
            self.sendfantome = 1
        else:
            self.sendfantome = 0

    
    def deplace_r(self):
        if lancement:
            self.x = int(canvas.coords(self.player)[0] // 20)
            self.y = int(canvas.coords(self.player)[1] // 20)
            if (self.x, self.y) == (18, 10):
                self.x, self.y = 0, 10
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.y - 1][self.x + 1] != '1':
                    self.x += 1
                    if self.sendfantome == 1: 
                        message = "deplace:right"
                        self.connexion.send(message.encode("Utf8"))
                        if self.x == joueurP.x and self.y - 1 == joueurP.y:
                            message = "Fin:F-P"
                            self.connexion.send(message.encode("Utf8"))
                            fin("F-P")     
            canvas.coords(self.player, self.x * 20, self.y * 20, self.x * 20 + 10, self.y * 20 - 20, self.x * 20 + 20, self.y * 20)

    def deplace_l(self):
        if lancement:
            self.x = int(canvas.coords(self.player)[0] // 20)
            self.y = int(canvas.coords(self.player)[1] // 20)
            if (self.x, self.y) == (0, 10):
                self.x, self.y = 18, 10
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.y - 1][self.x - 1] != '1':
                    self.x -= 1
                    if self.sendfantome == 1: 
                        message = "deplace:left"
                        self.connexion.send(message.encode("Utf8"))
                        if self.x == joueurP.x and self.y - 1 == joueurP.y:
                            message = "Fin:F-P"
                            self.connexion.send(message.encode("Utf8"))
                            fin("F-P")
            canvas.coords(self.player, self.x * 20, self.y * 20, self.x * 20 + 10, self.y * 20 - 20, self.x * 20 + 20, self.y * 20)

    def deplace_u(self):
        if lancement:
            self.x = int(canvas.coords(self.player)[0] // 20)
            self.y = int(canvas.coords(self.player)[1] // 20)
            if self.x < len(tab.tableau[0]):
                if tab.tableau[self.y - 2][self.x] != '1':
                    self.y -= 1
                    if self.sendfantome == 1: 
                        message = "deplace:up"
                        self.connexion.send(message.encode("Utf8"))
                        if self.x == joueurP.x and self.y - 1 == joueurP.y:
                            message = "Fin:F-P"
                            self.connexion.send(message.encode("Utf8"))
                            fin("F-P")
            canvas.coords(self.player, self.x * 20, self.y * 20, self.x * 20 + 10, self.y * 20 - 20, self.x * 20 + 20, self.y * 20)

    def deplace_d(self):
        if lancement:
            self.x = int(canvas.coords(self.player)[0] // 20)
            self.y = int(canvas.coords(self.player)[1] // 20)
            if self.x < len(tab.tableau[0]):
                if tab.tableau[self.y][self.x] != '1':
                    self.y += 1
                    if self.sendfantome == 1: 
                        message = "deplace:down"
                        self.connexion.send(message.encode("Utf8"))
                        if self.x == joueurP.x and self.y - 1 == joueurP.y:
                            message = "Fin:F-P"
                            self.connexion.send(message.encode("Utf8"))
                            fin("F-P")
            canvas.coords(self.player, self.x * 20, self.y * 20, self.x * 20 + 10, self.y * 20 - 20, self.x * 20 + 20, self.y * 20)      


class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn     # réf. du socket de connexion
        self.compteur = Label(text='En attente de joueur ...', bg='black', fg='white')
        self.compteur.grid(row=0, column=1, columnspan=3)

    def run(self):

        global lancement

        while 1:

            message_recu = self.connexion.recv(1024).decode("Utf8")
            demande = message_recu.rsplit()
            try:
                coordoné = demande[1].split(':')
            except:
                pass

            self.create_player(demande)

            if demande[0] == "rebours":
                self.compte_rebours(demande[1])
            
            if message_recu == "START":
                lancement = True
                self.restitution_affichage()

            if demande[0] == "nbr_joueur":
                if sendpacman:
                    Joueurj.attente_connexion.configure(text='Joueur co : ' + str(demande[1]))
                else:
                    joueurP.attente_connexion.configure(text='Joueur co : ' + str(demande[1]))

            if lancement:
                self.recu_mouv(demande, coordoné)

            print(f"{bcolors.AUCLIENT}* {message_recu} *{bcolors.RESET}")
            if not message_recu or message_recu.upper() =="FIN":
                print("fini")
                print("Client arrêté. Connexion interrompue.")
                self.connexion.close()

    def restitution_affichage(self):
        self.compteur.grid_forget()
        if sendpacman:
            Joueurj.compteur_vie.grid(row=0, column=1, columnspan=1)
            Joueurj.compteur.grid(row=0, column=1, columnspan=3)
        else:
            joueurP.compteur_vie.grid(row=0, column=1, columnspan=1)
            joueurP.compteur.grid(row=0, column=1, columnspan=3)

    def compte_rebours(self, demande):
        self.compteur.configure(text='Lancement dans ' + str(demande))


    def create_player(self, demande):
        global Joueurj, joueurf1, joueurf2, joueurf3, joueurP
        global sendpacman,sendfantome1,sendfantome2,sendfantome3

        if demande[0] == "def" and demande[1] == "Thread-1":
            Joueurj = Pacman(181, 181)
            joueurf1 = Fantome(20, 40, 'blue', 0)
            joueurf2 = Fantome(20, 360, 'red', 0)
            joueurf3 = Fantome(340, 360, 'green', 0)
            sendpacman = True
            attente_connexion = Label(text='Rôle : Pacman', bg='black', fg='white')
            attente_connexion.grid(row=20, column=1, columnspan=3)

        elif demande[0] == "def" and demande[1] == "Thread-2":
            joueurP = Pacman(181, 181)
            Joueurj = Fantome(20, 40, 'blue', 1)
            joueurf2 = Fantome(20, 360, 'red', 0)
            joueurf3 = Fantome(340, 360, 'green', 0)
            sendfantome1 = True
            attente_connexion = Label(text='Rôle : Fantome bleue', bg='black', fg='white')
            attente_connexion.grid(row=20, column=1, columnspan=3)

        elif demande[0] == "def" and demande[1] == "Thread-3":
            joueurP = Pacman(181, 181)
            joueurf1 = Fantome(20, 40, 'blue', 0)
            Joueurj = Fantome(20, 360, 'red', 1)
            joueurf3 = Fantome(340, 360, 'green', 0)
            sendfantome2 = True
            attente_connexion = Label(text='Rôle : Fantome rouge', bg='black', fg='white')
            attente_connexion.grid(row=20, column=1, columnspan=3)

        elif demande[0] == "def" and demande[1] == "Thread-4":
            joueurP = Pacman(181, 181)
            joueurf1 = Fantome(20, 40, 'blue', 0)
            joueurf2 = Fantome(20, 360, 'red', 0)
            Joueurj = Fantome(340, 360, 'green', 1)
            sendfantome3 = True
            attente_connexion = Label(text='Rôle : Fantome vert', bg='black', fg='white')
            attente_connexion.grid(row=20, column=1, columnspan=3)


    def recu_mouv(self, demande, infos):

        if demande[0] == "Pacman":
            if infos[0] == "Fin":
                fin(infos[1])
            elif infos[0] == "deplace":

                if infos[1] == "right":
                    joueurP.deplace_r()

                if infos[1] == "left":
                    joueurP.deplace_l()
                if infos[1] == "up":
                    joueurP.deplace_u()

                if infos[1] == "down":
                    joueurP.deplace_d()

        elif demande[0] == "Fant1":
            if infos[0] == "Fin":
                fin(infos[1])
            elif infos[0] == "deplace":

                if infos[1] == "right":
                    joueurf1.deplace_r()

                if infos[1] == "left":
                    joueurf1.deplace_l()

                if infos[1] == "up":
                    joueurf1.deplace_u()

                if infos[1] == "down":
                    joueurf1.deplace_d()

        elif demande[0] == "Fant2":
            if infos[0] == "Fin":
                fin(infos[1])
            elif infos[0] == "deplace":

                if infos[1] == "right":
                    joueurf2.deplace_r()

                if infos[1] == "left":
                    joueurf2.deplace_l()

                if infos[1] == "up":
                    joueurf2.deplace_u()

                if infos[1] == "down":
                    joueurf2.deplace_d()

        elif demande[0] == "Fant3":
            if infos[0] == "Fin":
                fin(infos[1])
            elif infos[0] == "deplace":

                if infos[1] == "right":
                    joueurf3.deplace_r()

                if infos[1] == "left":
                    joueurf3.deplace_l()

                if infos[1] == "up":
                    joueurf3.deplace_u()

                if infos[1] == "down":
                    joueurf3.deplace_d()


class ThreadEmission(threading.Thread):
    """objet thread gérant l'émission des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn        # réf. du socket de connexion

    def run(self):
        while 1:
            message_emis = input()
            self.connexion.send(message_emis.encode("Utf8"))


############## mort de joueur ####################

def fin(infos):
    global fantome_dead
    if sendpacman:
        if infos == "F-P":
            if Joueurj.vie == 1:
                showinfo("Partie terminé", "Le Pacman n'a plus de vie")
                th_R.connexion.close()
                fen.destroy()
            else:
                Joueurj.vie -= 1
                Joueurj.compteur_vie.configure(text='Vie = ' + str(Joueurj.vie))
                canvas.coords(Joueurj.pacman, 181, 181, 199,199)
        elif infos == "P-F1":
            canvas.delete(joueurf1.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1
        elif infos == "P-F2":
            canvas.delete(joueurf2.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1
        elif infos == "P-F3":
            canvas.delete(joueurf3.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1
    elif sendfantome1:
        if infos == "F-P":
            if joueurP.vie == 1:
                showinfo("Partie terminé", "Le Pacman n'a plus de vie")
                th_R.connexion.close()
                fen.destroy()
            else:
                joueurP.vie -= 1
                joueurP.compteur_vie.configure(text='Vie = ' + str(joueurP.vie))
                canvas.coords(joueurP.pacman, 181, 181, 199,199)
        elif infos == "P-F1":
            canvas.delete(Joueurj.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1
        elif infos == "P-F2":
            canvas.delete(joueurf2.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1
        elif infos == "P-F3":
            canvas.delete(joueurf3.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1
    elif sendfantome2:
        if infos == "F-P":
            if joueurP.vie == 1:
                showinfo("Partie terminé", "Le Pacman n'a plus de vie")
                th_R.connexion.close()
                fen.destroy()
            else:
                joueurP.vie -= 1
                joueurP.compteur_vie.configure(text='Vie = ' + str(joueurP.vie))
                canvas.coords(joueurP.pacman, 181, 181, 199,199)
        elif infos == "P-F1":
            canvas.delete(joueurf1.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1
        elif infos == "P-F2":
            canvas.delete(Joueurj.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                self.connexion.close()
                fen.destroy()
            fantome_dead += 1
        elif infos == "P-F3":
            canvas.delete(joueurf3.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1
    else:
        if infos == "F-P":
            if joueurP.vie == 1:
                showinfo("Partie terminé", "Le Pacman n'a plus de vie")
                th_R.connexion.close()
                fen.destroy()
            else:
                joueurP.vie -= 1
                joueurP.compteur_vie.configure(text='Vie = ' + str(joueurP.vie))
                canvas.coords(joueurP.pacman, 181, 181, 199,199)
        elif infos == "P-F1":
            canvas.delete(joueurf1.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1
        elif infos == "P-F2":
            canvas.delete(joueurf2.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1
        elif infos == "P-F3":
            canvas.delete(Joueurj.player)
            if fantome_dead == 2:
                showinfo("Partie terminé", "Le Pacman a manger tout les fantomes")
                th_R.connexion.close()
                fen.destroy()
            fantome_dead += 1



# Programme principal - Établissement de la connexion :

def connexion_func():
    global connexion
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connexion.connect((HOST.get(), PORT.get()))
    except socket.error:
        print("La connexion a échoué.")
        sys.exit()
    print("\n\nConnexion établie avec le serveur.\n\n")
    fenetre.destroy()

    # Dialogue avec le serveur : on lance deux threads pour gérer
    # indépendamment l'émission et la réception des messages :




########## fenetre temporaire de menu ######################


fenetre = Tk()

fenetre.title('Mise en réseau - Serveur')

fenetre.geometry("385x425")

fenetre.configure(bg='#EFE9E9')
# Cadre1 : paramètres serveur
#cadre1 = Frame(fenetre,borderwidth=2,relief=GROOVE)
#cadre1.grid(row=1,column=1,sticky=W+E)

titre = Label(fenetre, text="Pacman", font=("Courier", 30), bg='#EFE9E9')
titre.pack(pady=40)

Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(pady=30)

HOST = StringVar()
HOST.set('Localhost')
Entry(Frame1, textvariable= HOST).grid(row=0,column=1,padx=10,pady=10)

PORT = IntVar()
PORT.set(20000)
Entry(Frame1, textvariable= PORT).grid(row=1,column=1,padx=10,pady=10)

ButtonConnexion = Button(Frame1, text ='Play',command=connexion_func)
ButtonConnexion.grid(row=0,column=2,rowspan=2,padx=5,pady=5)

f = font.Font(size=12)

Buttonquit = Button(fenetre, text ='Quit',command=fenetre.destroy)
Buttonquit.config(height=1, width=10)
Buttonquit.pack(pady=40)


fenetre.mainloop()



####################fentere de jeu #############################


fen = Tk()

fen.title("Pacman")
tab = Tableau()
tab.open()

canvas = Canvas(fen, width=len(tab.tableau[0]) * 20, height=len(tab.tableau) * 20, background='#C7DCF1')

canvas.grid(row=1, column=1, columnspan=3)  # méthode qui permet de placer la zone de dessin dans la fenêtre
tab.place()


th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()

fen.bind("<z>", lambda event: Joueurj.deplace_u())
fen.bind("<s>", lambda event: Joueurj.deplace_d())
fen.bind("<q>", lambda event: Joueurj.deplace_l())
fen.bind("<d>", lambda event: Joueurj.deplace_r())
fen.bind("<a>", lambda event: Joueurj.object_case())

fen.mainloop()