# -*- coding: utf-8 -*-
import socket, sys, threading
from tkinter import *
from tkinter.messagebox import *


host = '192.168.1.124'
port = 40000

lancement = False

right = False
left = False
up = False
left = False

PacMan = False
fantome2 = False
fantome3 = False
fantome4 = False

class bcolors:
    AUCLIENT = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    SERVEUR = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class Tableau:
    """gestion du level"""

    def __init__(self):
        self.level = 'level_1.txt'
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
                if ligne[i_colonne] == '1':
                    canvas.create_rectangle(i_colonne * 20, i_ligne * 20, i_colonne * 20 + 20, i_ligne * 20 + 20, fill='#000', outline='#000')

class Pacman:
    """gestion du perso"""

    def __init__(self):
        self.pacman = canvas.create_oval(481, 1, 499, 19, fill='yellow')
        self.x = 0
        self.y = 0
        self.connexion = connexion

    def deplace(self, direction):
        # Déplacement vers la droite
        self.x = int(canvas.coords(self.pacman)[0] // 20)
        self.y = int(canvas.coords(self.pacman)[1] // 20)
        if direction == 'r':
            if (self.x, self.y) == (18, 9):
                self.x, self.y = 0, 9
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.y][self.x + 1] != '1':
                    self.x += 1
                    if PM == True:
                        message = "deplace:right"
                        self.connexion.send(message.encode("Utf8"))
        # Déplacement vers la gauche
        if direction == 'l':
            if (self.x, self.y) == (0, 9):
                self.x, self.y = 18, 9
            elif self.x > 0:
                if tab.tableau[self.y][self.x - 1] != '1':
                    self.x -= 1
                    if PM == True:
                        message = "deplace:left"
                        self.connexion.send(message.encode("Utf8"))
        # Déplacement vers le haut
        if direction == 'u':
            if self.y > 0:
                if tab.tableau[self.y - 1][self.x] != '1':
                    self.y -= 1
                    if PM == True:
                        message = "deplace:up"
                        self.connexion.send(message.encode("Utf8"))
        # Déplacement vers le bas
        if direction == 'd':
            if self.y < len(tab.tableau):
                if tab.tableau[self.y + 1][self.x] != '1':
                    self.y += 1
                    if PM == True:
                        message = "deplace:down"
                        self.connexion.send(message.encode("Utf8"))
        canvas.coords(self.pacman, self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)


class Fantome1:
    """gestion du perso"""

    def __init__(self):
        self.player = canvas.create_polygon(0, 20, 10, 0, 20, 20, fill='blue')
        self.x = 0
        self.y = 0
        self.z = 0
        self.z_bis = 0
        self.connexion = connexion


    def deplace(self, direction):
        self.x = int(canvas.coords(self.player)[0] // 20)
        self.y = int(canvas.coords(self.player)[1] // 20)
        self.z = canvas.coords(self.player)[2] / 20
        self.z_bis = int(canvas.coords(self.player)[3] // 20)
        # Déplacement vers la droite
        if direction == 'r':
            if (self.x, self.y, self.z, self.z_bis) == (18, 10, 18.5, 9):
                self.x, self.y, self.z, self.z_bis = 0, 10, 0.5, 9
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.z_bis][self.x + 1] != '1':
                    self.x += 1
                    self.z += 1
        # Déplacement vers la gauche
        if direction == 'l':
            if (self.x, self.y, self.z, self.z_bis) == (0, 10, 0.5, 9):
                self.x, self.y, self.z, self.z_bis = 18, 10, 18.5, 9
            elif self.x > 0:
                if tab.tableau[self.z_bis][self.x - 1] != '1':
                    self.x -= 1
                    self.z -= 1
        # Déplacement vers le haut
        if direction == 'u':
            if self.y > 0:
                if tab.tableau[self.z_bis - 1][self.x] != '1':
                    self.y -= 1
                    self.z_bis -= 1
        # Déplacement vers le bas
        if direction == 'd':
            if self.y < len(tab.tableau):
                if tab.tableau[self.z_bis + 1][self.x] != '1':
                    self.y += 1
                    self.z_bis += 1
        canvas.coords(self.player, self.x * 20, self.y * 20, self.z * 20, self.z_bis * 20, self.x * 20 + 20, self.y * 20)

class Fantome2:
    """gestion du perso"""

    def __init__(self):
        self.player = canvas.create_polygon(0, 400, 10, 380, 20, 400, fill='red')
        self.x = 0
        self.y = 0
        self.z = 0
        self.z_bis = 0


    def deplace(self, direction):
        self.x = int(canvas.coords(self.player)[0] // 20)
        self.y = int(canvas.coords(self.player)[1] // 20)
        self.z = canvas.coords(self.player)[2] / 20
        self.z_bis = int(canvas.coords(self.player)[3] // 20)
        # Déplacement vers la droite
        if direction == 'r':
            if (self.x, self.y, self.z, self.z_bis) == (18, 10, 18.5, 9):
                self.x, self.y, self.z, self.z_bis = 0, 10, 0.5, 9
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.z_bis][self.x + 1] != '1':
                    self.x += 1
                    self.z += 1
        # Déplacement vers la gauche
        if direction == 'l':
            if (self.x, self.y, self.z, self.z_bis) == (0, 10, 0.5, 9):
                self.x, self.y, self.z, self.z_bis = 18, 10, 18.5, 9
            elif self.x > 0:
                if tab.tableau[self.z_bis][self.x - 1] != '1':
                    self.x -= 1
                    self.z -= 1
        # Déplacement vers le haut
        if direction == 'u':
            if self.y > 0:
                if tab.tableau[self.z_bis - 1][self.x] != '1':
                    self.y -= 1
                    self.z_bis -= 1
        # Déplacement vers le bas
        if direction == 'd':
            if self.y < len(tab.tableau):
                if tab.tableau[self.z_bis + 1][self.x] != '1':
                    self.y += 1
                    self.z_bis += 1
        canvas.coords(self.player, self.x * 20, self.y * 20, self.z * 20, self.z_bis * 20, self.x * 20 + 20, self.y * 20)


class Fantome3:
    """gestion du perso"""

    def __init__(self):
        self.player = canvas.create_polygon(480, 400, 490, 380, 500, 400, fill='green')
        self.x = 0
        self.y = 0
        self.z = 0
        self.z_bis = 0


    def deplace(self, direction):
        self.x = int(canvas.coords(self.player)[0] // 20)
        self.y = int(canvas.coords(self.player)[1] // 20)
        self.z = canvas.coords(self.player)[2] / 20
        self.z_bis = int(canvas.coords(self.player)[3] // 20)
        # Déplacement vers la droite
        if direction == 'r':
            if (self.x, self.y, self.z, self.z_bis) == (18, 10, 18.5, 9):
                self.x, self.y, self.z, self.z_bis = 0, 10, 0.5, 9
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.z_bis][self.x + 1] != '1':
                    self.x += 1
                    self.z += 1
        # Déplacement vers la gauche
        if direction == 'l':
            if (self.x, self.y, self.z, self.z_bis) == (0, 10, 0.5, 9):
                self.x, self.y, self.z, self.z_bis = 18, 10, 18.5, 9
            elif self.x > 0:
                if tab.tableau[self.z_bis][self.x - 1] != '1':
                    self.x -= 1
                    self.z -= 1
        # Déplacement vers le haut
        if direction == 'u':
            if self.y > 0:
                if tab.tableau[self.z_bis - 1][self.x] != '1':
                    self.y -= 1
                    self.z_bis -= 1
        # Déplacement vers le bas
        if direction == 'd':
            if self.y < len(tab.tableau):
                if tab.tableau[self.z_bis + 1][self.x] != '1':
                    self.y += 1
                    self.z_bis += 1
        canvas.coords(self.player, self.x * 20, self.y * 20, self.z * 20, self.z_bis * 20, self.x * 20 + 20, self.y * 20)


class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn     # réf. du socket de connexion


    def run(self):
        global Joueurj,Joueur2,Joueur3,Joueur4
        global PM,FT1,FT2,FT3
        while 1:
            message_recu = self.connexion.recv(1024).decode("Utf8")
            demande = message_recu.rsplit()
            coordoné = demande[1].split(':')

            if demande[0] == "def" and demande[1] == "Thread-1":
                print("player = Pacman")
                Joueurj = Pacman()
                Joueur2 = Fantome1()
                Joueur3 = Fantome2()
                Joueur4 = Fantome3()
                PM = True

            elif demande[0] == "def" and demande[1] == "Thread-2":
                print("player = Fantome1")
                Joueurj = Fantome1()
                Joueur2 = Pacman()
                Joueur3 = Fantome2()
                Joueur4 = Fantome3()
                FT1 = True

            elif demande[0] == "def" and demande[1] == "Thread-3":
                print("player = Fantome2")
                Joueurj = Fantome2()
                Joueur2 = Fantome1()
                Joueur3 = Pacman()
                Joueur4 = Fantome3()
                FT2 = True

            elif demande[0] == "def" and demande[1] == "Thread-4":
                print("player = Fantome3")
                Joueurj = Fantome3()
                Joueur2 = Fantome2()
                Joueur3 = Fantome1()
                Joueur4 = Pacman()
                FT3 = True

            elif demande[0] == "Thread-1>":
                if coordoné[0] == "deplace":
                    print(f"\n\nfantome deplacement 2 {coordoné[1]}\n\n")
                    if coordoné[1] == "right":
                        Pacman.deplace('r')
                        print("RIGHT")

                    if coordoné[1] == "left":
                        Pacman.deplace('l')
                        print("LEFT")

                    if coordoné[1] == "up":
                        Pacman.deplace('u')
                        print("UP")

                    if coordoné[1] == "down":
                        Pacman.deplace('d')
                        print("DOWN")

            elif demande[0] == "Thread-2>":
                if coordoné[0] == "deplace":
                    print(f"\n\nfantome deplacement 2 {coordoné[1]}\n\n")

                    if coordoné[1] == "right":
                        Fantome1.deplace('r')
                        print("RIGHT")

                    if coordoné[1] == "left":
                        Fantome1.deplace('l')
                        print("LEFT")

                    if coordoné[1] == "up":
                        Fantome1.deplace('u')
                        print("UP")

                    if coordoné[1] == "down":
                        Fantome1.deplace('d')
                        print("DOWN")

            elif demande[0] == "Thread-3>":
                if coordoné[0] == "deplace":
                    print(f"\n\nfantome deplacement 3 {coordoné[1]}\n\n")

                    if coordoné[1] == "right":
                        Fantome2.deplace('r')
                        print("RIGHT")

                    if coordoné[1] == "left":
                        Fantome2.deplace('l')
                        print("LEFT")

                    if coordoné[1] == "up":
                        Fantome2.deplace('u')
                        print("UP")

                    if coordoné[1] == "down":
                        Fantome2.deplace('d')
                        print("DOWN")

            elif demande[0] == "Thread-4>":
                if coordoné[0] == "deplace":
                    print(f"\n\nfantome deplacement 4 {coordoné[1]}\n\n")

                    if coordoné[1] == "right":
                        Fantome3.deplace('r')
                        print("RIGHT")

                    if coordoné[1] == "left":
                        Fantome3.deplace('l')
                        print("LEFT")

                    if coordoné[1] == "up":
                        Fantome3.deplace('u')
                        print("UP")

                    if coordoné[1] == "down":
                        Fantome3.deplace('d')
                        print("DOWN")



            print(f"{bcolors.AUCLIENT}* {message_recu} *{bcolors.RESET}")
            if not message_recu or message_recu.upper() =="FIN":
                    break

    # Le thread <réception> se termine ici.
    # On force la fermeture du thread <émission> :
        th_E._stop()
        print("Client arrêté. Connexion interrompue.")
        self.connexion.close()

class ThreadEmission(threading.Thread):
    """objet thread gérant l'émission des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn	     # réf. du socket de connexion

    def run(self):
        while 1:
            message_emis = input()
            self.connexion.send(message_emis.encode("Utf8"))


# Programme principal - Établissement de la connexion :


fen = Tk()

fen.title("Pacman")
tab = Tableau()
tab.open()

canvas = Canvas(fen, width=len(tab.tableau[0]) * 20, height=len(tab.tableau) * 20, background='#C7DCF1')

canvas.grid(row=1, column=1, columnspan=3)  # méthode qui permet de placer la zone de dessin dans la fenêtre
tab.place()

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((host, port))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("\n\nConnexion établie avec le serveur.\n\n")

# Dialogue avec le serveur : on lance deux threads pour gérer
# indépendamment l'émission et la réception des messages :
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()



fen.bind("<z>", lambda event: Joueurj.deplace('u'))
fen.bind("<s>", lambda event: Joueurj.deplace('d'))
fen.bind("<q>", lambda event: Joueurj.deplace('l'))
fen.bind("<d>", lambda event: Joueurj.deplace('r'))
fen.bind("<a>", lambda event: print(canvas.coords(player.pacman)))

fen.mainloop()
