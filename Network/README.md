# Sensor

## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.<BR>
Pour la partie Network, plusieurs librairies sont utilisées et expliquées, tel que `network`,`socket`, `urequests` et `ntptime`.

  
## Affichage de l'heure et de la température sur l'écran LCD
Récupération de la date et l'heure à l'aide du module `ntptime`, et affichage de ces valeurs sur l'écran LCD. Récupération des données météos en temps réel à l'aide du module `urequest`et isolement de la température depuis le fichier JSON récupéré, et affichage de celle-ci sur l'écran LCD. 
 
Code : [DHT11](https://github.com/hepl-leclercq/smartcities/blob/25dd11630cc4ba6d2fc0b74e16389c21efe1a084/Sensor/DHT11.py)




## Module `Network`
Le module `Network` de MicroPython permet de gérer les connexions réseau sans fil et Ethernet sur des microcontrôleurs compatibles. Il met à disposition des classes et des fonctions pour la configuration et la gestion de connexions Wi-Fi et Ethernet.

Les principales classes offertes par ce module sont :

`WLAN`: permet de configurer et gérer les connexions Wi-Fi. <BR>
`LAN`: permet de configurer et gérer les connexions Ethernet.<BR>
`Server`: permet de créer un serveur HTTP ou FTP.<BR>
  
Les principales fonctions disponibles dans le module sont :

`WLAN.connect()`: permet de se connecter à un réseau Wi-Fi.<BR>
`WLAN.disconnect()`: permet de se déconnecter d'un réseau Wi-Fi.<BR>
`WLAN.isconnected()`: permet de vérifier si la connexion Wi-Fi est active.<BR>
`LAN.active()`: permet d'activer ou de désactiver la connexion Ethernet.<BR>
`LAN.ifconfig()`: permet de configurer l'adresse IP, le masque de sous-réseau et la passerelle par défaut pour une connexion Ethernet.<BR>
  
Le module `network` est très utile pour les projets IoT qui nécessitent une connexion réseau pour communiquer avec des serveurs ou des appareils distants

## Module `Socket`
Le module `socket` de MicroPython permet de communiquer avec différents protocoles réseau tels que TCP, UDP, SSL, etc. Il fournit une interface compatible avec la bibliothèque standard Python pour la gestion des sockets.

Les fonctions disponibles dans ce module sont :<BR>

`socket(family, type, proto=0)` : crée un nouveau socket avec une famille d'adresses et un type de socket spécifiés.<BR>
`bind(address)` : associe le socket à une adresse.<BR>
`listen(backlog)` : met le socket en mode écoute.<BR>
`accept()` : accepte une connexion entrante.<BR>
`connect(address)` : établit une connexion avec une adresse distante.<BR>
`send(bytes)` : envoie des données à l'autre extrémité de la connexion.<BR>
`recv(bufsize)` : reçoit des données depuis l'autre extrémité de la connexion.<BR>
`setblocking(flag)` : configure le mode bloquant ou non bloquant du socket.<BR>
`settimeout(value)` : définit le délai d'attente pour les opérations de socket.<BR>
`close()` : ferme le socket.<BR>
`getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)` : résout une adresse de serveur et renvoie une liste de tuples contenant les informations d'adresse.<BR>
`gethostname()` : renvoie le nom d'hôte local.<BR>
`gethostbyname(hostname)` : renvoie l'adresse IP correspondant à un nom d'hôte donné.<BR>
`gethostbyaddr(ip_address)` : renvoie le nom d'hôte correspondant à une adresse IP donnée.<BR>
Le module socket est utile pour la communication avec d'autres appareils sur un réseau, en utilisant différentes méthodes de communication réseau.
  
## Module `urequests`
Le module `urequests` de MicroPython permet de réaliser des requêtes HTTP basiques à partir de cartes de développement comme le Raspberry Pi Pico. Il s'appuie sur le module requests de Python et prend en charge les méthodes GET, POST, PUT et DELETE pour interagir avec des serveurs Web. Les principales fonctions disponibles dans le module urequests sont les suivantes :<BR>

`urequests.get()` : envoie une requête GET à l'URL spécifiée et renvoie la réponse sous forme de texte.<BR>
`urequests.post()` : envoie une requête POST à l'URL spécifiée avec les données fournies et renvoie la réponse sous forme de texte.<BR>
`urequests.put()` : envoie une requête PUT à l'URL spécifiée avec les données fournies et renvoie la réponse sous forme de texte.<BR>
`urequests.delete()` : envoie une requête DELETE à l'URL spécifiée et renvoie la réponse sous forme de texte.<BR>

## Module `ntptime`
Le module `ntptime` en MicroPython permet de synchroniser l'horloge temps réel d'un microcontrôleur avec l'heure universelle coordonnée (UTC) à l'aide du protocole Network Time Protocol (NTP).<BR>

Les fonctions principales disponibles dans ce module sont :<BR>

`settime()` : Met à jour l'horloge temps réel du microcontrôleur en utilisant l'heure UTC récupérée à partir d'un serveur NTP.<BR>
`time()` : Retourne l'heure UTC en secondes depuis l'époque Unix (1er janvier 1970).<BR>
`host2ntp(host)` : Convertit une adresse IP ou un nom de domaine en une adresse NTP.<BR>
`ntpc` : Objet de configuration pour le client NTP.<BR>
`NTP_DELTA` : Constante pour compenser le décalage de temps.<BR>
`NTP_PACKET_FORMAT` : Format de la trame de requête NTP.<BR>
