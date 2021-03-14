print("""

 █████╗ ███╗   ██╗████████╗██╗    ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██╔══██╗████╗  ██║╚══██╔══╝██║    ██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
███████║██╔██╗ ██║   ██║   ██║    ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██╔══██║██║╚██╗██║   ██║   ██║    ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
██║  ██║██║ ╚████║   ██║   ██║    ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                                             
                        """)
print("Simple tool pour vérifié la présence d'un logger sur une config OpenBullet.\n")


file = input("Donne moi une config a analysé, Exemple: (PSN.anom)\n >> ")

with open(file) as co:
	if '"https://api.telegram.org/bot' in co.read():
		print("ATTENTION LA CONFIG CONTIENT UN LOGGER SUR TELEGRAM!")
	elif '"https://discordapp.com/api/webhooks/' in co.read():
		print("ATTENTION LA CONFIG CONTIENT UN LOGGER SUR DISCORD !")
	elif 'https://docs.google.com/forms/d' in co.read():
		print("ATTENTION LA CONFIG CONTIENT UN LOGGER SUR GOOGLEFORMS !")
	else:
		print("La recherche n'a rien donné, la config est logiquement safe, pense a vérifié tout de même.")

print("Bye <3")
