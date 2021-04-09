# Définition d'un serveur réseau gérant un système de CHAT simplifié.
# Utilise les threads pour gérer les connexions clientes en parallèle.

HOST = 'localhost'
PORT = 40000

from tkinter import *
from tkinter.messagebox import *
import socket, sys, threading

class ThreadClient(threading.Thread):
    '''dérivation d'un objet thread pour gérer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        # Dialogue avec le client :
        nom = self.getName()	    # Chaque thread possède un nom
        while 1:
            msgClient = self.connexion.recv(1024).decode("Utf8")
            if not msgClient or msgClient.upper() =="FIN":
                 break
            elif msgClient == "start":
                msg = "start"
                conn_client[cle].send(start.encode("Utf8"))
            elif msgClient == "client_co":
                dernier_clients = list(conn_client.keys())
                print(dernier_clients[-1])
            #message = "%s> %s" % (nom,msgClient)
            if nom == "Thread-1":
                message = f"Pacman {msgClient}"
            if nom == "Thread-2":
                message = f"Fant1 {msgClient}"
            if nom == "Thread-3":
                message = f"Fant2 {msgClient}"
            if nom == "Thread-4":
                message = f"Fant3 {msgClient}"
            print(message)
            # Faire suivre le message à tous les autres clients :
            for cle in conn_client:
                if cle != nom:	  # ne pas le renvoyer à l'émetteur
                    conn_client[cle].send(message.encode("Utf8"))

      # Fermeture de la connexion :
    #self.connexion.close()	  # couper la connexion côté serveur
    #del conn_client[nom]	# supprimer son entrée dans le dictionnaire
    #print("Client %s déconnecté." % nom)
      # Le thread se termine ici

# Initialisation du serveur - Mise en place du socket :
conn_client = {}


def connexion():


    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        mySocket.bind((HOST.get(), PORT.get()))
    except socket.error:
        print("La liaison du socket à l'adresse choisie a échoué.")
        sys.exit()
    print("Serveur prêt, en attente de requêtes ...")
    mySocket.listen(5)

    # Attente et prise en charge des connexions demandées par les clients :
	####################### dictionnaire des connexions clients
    while 1:
        connexion, adresse = mySocket.accept()
        # Créer un nouvel objet thread pour gérer la connexion :
        th = ThreadClient(connexion)
        th.start()
        # Mémoriser la connexion dans le dictionnaire :
        it = th.getName()	  # identifiant du thread
        conn_client[it] = connexion
        print("Client %s connecté, adresse IP %s, port %s." % (it, adresse[0], adresse[1]))
        # Dialogue avec le client :
        msg ="\n\nVous êtes connecté. Envoyez vos messages.\n\n"
        dernier_clients = list(conn_client.keys())
        #connexion.send(msg.encode("Utf8"))
        numeros_clients = f"def {dernier_clients[-1]}"
        connexion.send(numeros_clients.encode("Utf8"))



            #role = conn_client.to_bytes()
            #connexion.send(role)


# Création de la fenêtre principale (main window)
Mafenetre = Tk()

Mafenetre.title('Mise en réseau - Serveur')

# Cadre1 : paramètres serveur
cadre1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
cadre1.grid(row=0,column=0,padx=5,pady=5,sticky=W+E)

Label(cadre1, text = "Hôte").grid(row=0,column=0,padx=5,pady=5,sticky=W)
HOST = StringVar()
HOST.set('Localhost')
Entry(cadre1, textvariable= HOST).grid(row=0,column=1,padx=5,pady=5)

Label(cadre1, text = "Port").grid(row=1,column=0,padx=5,pady=5,sticky=W)
PORT = IntVar()
PORT.set(40000)
Entry(cadre1, textvariable= PORT).grid(row=1,column=1,padx=5,pady=5)

ButtonConnexion = Button(cadre1, text ='Ouvrir le serveur',command=connexion)
ButtonConnexion.grid(row=0,column=2,rowspan=2,padx=5,pady=5)




Mafenetre.mainloop()
