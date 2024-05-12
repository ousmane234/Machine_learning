from datetime import datetime 
# Fonction permettant d'afficher une facture (facture forfait internet ou  forfait télé)
def afficher_facture(id_forfait ,  sous_totale =0 , nom = "" , prenom= "" , numero="" ,adresse="" ):
	tva = (sous_totale * 18)//100 # egal à 18% du sous totale
	montant_total= sous_totale + tva 
	print("\n")
	print("\t"*4 ," ## facture ##")
	print("____________________________________________________________________________________")## information sur sengalConnect::
	print("Senegal-connect\n UCAD - LACGAA - MS2E 2024\n Facture n° : \t \t " , datetime.now().date() ,"  " , datetime.now().time().strftime("%H:%M:%S"))
					## information sur le client :::
	print("_____________________________________________________________________________________")
	print("Prenom et nom du client : " , prenom ," " ,nom ,"\t  numéro de téléphone: ", numero)
	print("Adresse du client : " ,adresse)
	print("\n")
	print("Description - forfait                                                         prix")
	print("-".ljust(85,"-"))
	print(id_forfait["description"].ljust(70 ," "),id_forfait["prix"],"CFA")
	print("Sous totale ".ljust(70, " "),sous_totale ,"CFA")
	print("Montant TVA ".ljust(70, " "),tva ,"CFA")
	print("Montant totale ".ljust(70, " "),montant_total,"CFA")
	print("-".ljust(85 , "-"))
	print("Merci de  votre confiance\n".ljust(40, " "))
					
print (" -------------------------------------------------------------------") 
print("|Bienvenu dans le systeme de facturation  d'Internet-Télé pour Tous.".ljust(60 , " "),"|\n"
      "|Ce system permet de calculer la facture des  abonnés selon le prix ".ljust(60 , " "),"|\n"
      "|et le nombre de forfaite choici. Il affiche aussi le nombre ".ljust(70 ," "),"|\n"
      "|d'abonnés par forfait ".ljust(70 ," "), "|")
print(" ---------------------------------------------------------------------")
print("\t *** Menu de choix ***\n" ,
      "\t1. Facturer un Abonnement\n" ,
      "\t2. Afficher le nombre d'abonnés par forfait\n" , 
      "\t3. Quitter le programme")
global nb_abonnes
while True:
	option = int(input("Entrer votre option:"))
	# on initialise le nombre d'abonne pour chaque forfait à 0 dans un dictionnaire contenant l'ensemble des  forfaits possibles
	nb_abonnes ={"50": 0 ,"150":0, "500":0 ,"B":0 ,"T":0 ,"E":0}
	id_services = (1,2 ,3)
	id_forfaits_internet = {
		"50":{"description": "Internet fibre hybride 50" ,"prix": 12500} ,
		"150":{"description":"internet fibre hybride 150" , "prix":15250 } ,
		"500":{"description": "internet fibre hybride 500" , "prix": 20500}
	}
	id_forfaits_tele = {
		"B":{"description":"Forfait Bien -choix 15 chaines à la carte" , "prix":4900},
		"T":{"description":"Forfait Tres Bien - choix de 25 chaines à la carte", "prix": 8400},
		"E":{"description" : "Forfait excellent - choix de 35 chaines à la carte" , "prix": 12500}
	}
	if option ==1:
		nom = input("Entrer le nom de l'abonné") 
		prenom = input("Entrer le prenom de l'abonné")
		numero = input("Entrer le numéro de l'abonné")
		adresse = input("Entrer l'adresse de l'abonné")
		
		while True :
			service = int(input("Entrer les numéro des services \n(1 = Internet , 2 = Télé , 3 = Internet et Télé) :" ) )
			if service not in id_services:
				print( "numéro de service inconnu") 
				continue # redemander des numéros de  services
			else :
				break  # sinon :  on continue les traitement
		if service == 1 :
			while True :
				forfait = input("Entrer l'identifiant du forfait (50 , 150 ,100)")
				if forfait not in id_forfaits_internet.keys():
					print("numéro de forfait invalide :\n")
					continue
				else:
					id_forfait =id_forfaits_internet[forfait]
					sous_totale = id_forfait["prix"]
					# si l'utilisateur  ajout un forfait un internet ,on doit increment le nombre d'abonne de ce forait là
					# pour pouvoir ensuit l'utiler dans le traitement de la partie2.
					nb_abonnes[forfait] += 1 
					afficher_facture( id_forfait , nom=nom , prenom = prenom, adresse = adresse , numero = numero  , sous_totale= sous_totale )
					break
				
		elif service == 2:
			while True:
				forfait = input("Entrer  l'identifiant du forfait \n\t>> B = Forfait bien -choix de 15 chaine à la carte ,\n\t>> T = Forfait Trés Bine -choix de 25 chaine à la carte\n\t>> E = Excellent -choix de 35 chaine à la carte)\n")
				if forfait not in id_forfaits_tele.keys():
					print("Le numero  forfait est invalide\n")
					continue
				else: 
					id_forfait = id_forfaits_tele[forfait]
					sous_totale =  id_forfait["prix"]
					nb_abonnes[forfait] += 1 # increment  le nombre d'abonnés de ce forfait à 1
					afficher_facture(id_forfait ,nom= nom  ,prenom = prenom , adresse= adresse , numero= numero , sous_totale= sous_totale)
					break	
		else: # service 3 ( internet +  tele)
			while True :
				forfait_internet = input("Entrer l'identifiant du  forfait innternet : (50 ,150 ,500)")
				forfait_tele = input("Entrer  l'identifiant du forait  tele (B ,T , E)")
				if forfait_internet not in id_forfaits_internet.keys() or forfait_tele not in id_forfaits_tele.keys():
					print("numéro du forfait internet ou télé invalide \n")
					continue 
				else:
					sous_totale = id_forfaits_tele[forfait_tele]["prix"] + id_forfaits_internet[forfait_internet]["prix"]
					tva = (sous_totale * 18)//100 # egal à 18% du sous totale
					montant_total= sous_totale + tva 
					# incrementer de 1 le nombre d'abonnés  corespondant à ces  forfaits (internet et tel)
					nb_abonnes[forfait_tele] += 1
					nb_abonnes[forfait_internet] += 1
					print("\n")
					print("\t"*4 ," ## facture ##")
					print("____________________________________________________________________________________")## information sur sengalConnect::
					print("Senegal-connect\n UCAD - LACGAA - MS2E 2024\n Facture n° : \t \t " , datetime.now().date() ,"  " , datetime.now().time().strftime("%H:%M:%S"))
									## information sur le client :::
					print("_____________________________________________________________________________________")
					print("Prenom et nom du client : " , prenom ," " ,nom ,"\t  numéro de téléphone: ", numero)
					print("Adresse du client : "                                                      ,adresse)
					print("\n")
					print("Description - forfait                                                         prix")
					print("-----------------------------------------------------------------------------------")
					print(id_forfaits_internet[forfait_internet]["description"].ljust(70 ," ") , id_forfaits_internet[forfait_internet]["prix"] ," CFA")
					print(id_forfaits_tele[forfait_tele]["description"] ,"                    ",id_forfaits_tele[forfait_tele]["prix"], " CFA")
					print("Sous totale                                                            " , sous_totale ," CFA")
					print("Montant TVA                                                            " ,tva ,"CFA")
					print("Montant totale                                                         " , montant_total ," CFA")
					print("------------------------------------------------------------------------------------")
					print("\t"*4 ,"Merci de  votre confiance\n")
					break ;		# faire les traitements correspondants sur les forfaits tele et internet ?		
	elif option == 2:
		print("-----------------------------------------------------------------------")
		print("Senegal Connect")
		print("Date et Heure:\t" , datetime.now().date(), "  " , datetime.now().time().strftime("%H:%M:%S"))
		print("------------------------------------------------------------------------")
		print("Forfaits Nb. d'abonnés")
		print("********************************************************************")
		print("Internet fibre hybride 50                                       :", nb_abonnes["50"])
		print("Internet ifbre hybride 150                                      :", nb_abonnes["150"])
		print("Internet fibre hybride 500                                      :", nb_abonnes["500"]) 
		print("Forfait bien - choix de 15 chaines à la carte                   :", nb_abonnes["B"])
		print("Forfait très bien - choix de 25 chaines à la carte              :", nb_abonnes["T"])
		print("Forfait Excellent - choix de 35 chaines à la carte       	:", nb_abonnes["E"])
		print("---------------------------------------------------------------------")
		
	else:
		print("Au revoir !!!")
		break 




	
		
			




		
	


