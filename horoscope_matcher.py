#!/usr/bin/env python

# Feeding in bride specific details
bride_lagna = 'simha'
bride_chandran = 'meena'
bride_dasa = 'sukran'

# List of houses in clockwise order
house_list = ['mesha','rishaba','mithuna','karkadaga','simha','kanya','thula','vrichiga','dhanusu','makara','kumbha','meena']
# List of planets in clockwise order
planet_list = ['sevvai','sukran','budhan','chandran','suryan', 'budhan','sukran','sevvai','guru','sani','sani','guru']
# Compatible natchatram list for Cena
natchatra_list = ['tiruvonam','tiruvadurai','punarpoosam','uthram','aayilyam','hastham','swathi','revathi','ketai','magam','uthradam','sadhayam']
# Dictionary mapping of lagna subar planets for each house
lagna_subar = {'mesha':['sevvai','suryan','guru'],'rishaba':['sukran','budhan','sani'],'mithuna':['budhan','sukran','sani'],'karkadaga':['chandran','sevvai','guru'],'simha':['suryan','sevvai','guru'],'kanya':['budhan','sukran','sani'],'thula':['sukran','sani','budhan'],'vrichiga':['sevvai','guru','suryan'],'dhanusu':['guru','sevvai','suryan'],'makara':['sani','sukran','budhan'],'kumbam':['sani','budhan','sukran'],'meena':['guru','chandran','sevvai']}
# Dictionary mapping of natchatra nathan natchatrams for each planet
natchatra_nathan = {'ketu':['aswini','magam','moolam'],'sukran':['barani','pooram','pooradam'],'suryan':['krithigai','uthram','uthradam'],'chandran':['rohini','hastham','tiruvonam'],'sevvai':['mrigasirisham', 'chithirai','avittam'],'rahu':['tiruvadurai','swathi','sadhayam'],'guru':['punarpoosam','visaagam','poorattadhi'],'sani':['poosam','anusham','uthrattadhi'],'budhan':['aayilyam','revathi','ketai']}
#Dictionary maping of neecham planets for each house
neecham_houses = {'mesha':['sani'],'rishaba':['rahu','ketu'],'mithuna':['empty'],'karkadaga':['sevvai'],'simha':['empty'],'kanya':['sukran'],'thula':['suryan'],'vrichiga':['chandran'],'dhanusu':['empty'], 'makara':['guru'],'kumbha':['empty'],'meena':['budhan']}

def main():
	try:
		groom_chart = {}
		planets_in_house = []
		groom_lagna_house = []
		groom_planet_house = []
		print('Compatible natchatram list: \n\t')
		print(", ".join(natchatra_list))
		# natchatram_response = input("\nEnter Groom natchatra:	")
		natchatram_response = 'uthram'
		if natchatram_response in natchatra_list:
			print("\nList of houses: \n\t")
			print(", ".join(house_list))
			# groom_lagna = input("\nEnter groom's lagna:	")
			# groom_chandran = input("\nEnter groom's rasi:	")
			# groom_dasa = input("\nEnter groom's currently running dasa: ")
			# groom_dasa_nathan = input("\nEnter groom's dasa natchatra nathan: ")
			# print('\nList of natchatrams:\n\n\taswini, moolam, barani, pooram, pooradam, krithigai, rohini, mrigasirisham, chithirai,\n\tavittam, visaagam, poorattadhi, tiruvonam, tiruvadurai, punarpoosam, poosam, anusham, uthrattadhi,\n\tuthram, aayilyam, hastham, swathi, revathi, ketai, magam, uthradam, sadhayam')
			# sani_natchatram = input("\nEnter sani's natchatram from chart: ")
			groom_lagna = 'karkadaga'
			groom_chandran = 'mesha'
			groom_dasa = 'guru'
			groom_dasa_nathan = 'chandran'
			sani_natchatram = ' '
			# Checking if lagnam and rasi of groom and bride are not in 6th or 8th positions from one another
			lagna_check = abs(house_list.index(bride_lagna) - house_list.index(groom_lagna))
			rasi_check = abs(house_list.index(bride_chandran) - house_list.index(groom_chandran))
			# Start filling the rasi chart
			if not(lagna_check in [5,7]) and not(rasi_check in [5,7]):
				print('\nLets start filling the chart: ')
				for house in house_list:
					print('\nHow many planets does %s house have?	' %house)
					pnum = int(input())
					
					if pnum == 0:
						planets_in_house.append('empty')
						
					else:
						print('\nList of planets: \n\n\tsuryan, chandran, sevvai, sukran, budhan, guru, sani, rahu, ketu')
						for num in range(pnum):
							planet_name = input('Enter planet:	')
							planets_in_house.append(planet_name)
					groom_chart.update({house:planets_in_house})
					planets_in_house = []
					

				# groom_chart = {'mesha':'chandran','rishaba':'empty','mithuna':'empty','karkadaga':'empty','simha':'ketu','kanya':'sani','thula':'sevvai','vrichiga':['budhan','sukran'],'dhanusu':'suryan','makara':'empty','kumbha':'rahu','meena':'guru'}
				# sevvai_natchatra_athipathi = input("Enter Sevvai's saara nathan: ")
				# rahu_natchatra_athipathi = input("Enter Rahu's saara nathan: ")
				# ketu_natchatra_athipathi = input("Enter Ketu's saara nathan: ")
				# sani_natchatra_athipathi = input("Enter Sani's saara nathan: ")
				rahu_natchatra_athipathi = 'rahu'
				ketu_natchatra_athipathi = 'ketu'
				sani_natchatra_athipathi = 'guru'
				sevvai_natchatra_athipathi = ' '

				# Altering the default chart to start from the groom's lagnam
				for ghouse in range(len(house_list)):		
					if (house_list.index(groom_lagna))+ghouse >= len(house_list):	# Modifying index to obtain cyclic entry in chart
						groom_lagna_house.append(house_list[(house_list.index(groom_lagna)+ghouse)-len(house_list)])	# Houses from lagnam
						groom_planet_house.append(planet_list[(house_list.index(groom_lagna)+ghouse)-len(house_list)])	# Planet owners of each corresponding house
					else:
						groom_lagna_house.append(house_list[house_list.index(groom_lagna)+ghouse])	# Houses from lagnam
						groom_planet_house.append(planet_list[house_list.index(groom_lagna)+ghouse])	# Planet owners of each corresponding house
				# print(groom_chart)
				# print(groom_lagna_house)
				# print(groom_planet_house)

				# Extracting the house where the corresponding planet is residing
				suryan_house = [house  for (house, planet) in groom_chart.items() if 'suryan' in planet]
				rahu_house = [house  for (house, planet) in groom_chart.items() if 'rahu' in planet]
				ketu_house = [house  for (house, planet) in groom_chart.items() if 'ketu' in planet]
				sani_house = [house  for (house, planet) in groom_chart.items() if 'sani' in planet]
				sevvai_house = [house  for (house, planet) in groom_chart.items() if 'sevvai' in planet]
				chandran_house = [house  for (house, planet) in groom_chart.items() if 'chandran' in planet]
				budhan_house = [house  for (house, planet) in groom_chart.items() if 'budhan' in planet]
				sukran_house = [house  for (house, planet) in groom_chart.items() if 'sukran' in planet]
				guru_house = [house  for (house, planet) in groom_chart.items() if 'guru' in planet]
				second_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[2] in planet]
				sixth_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[5] in planet]
				seventh_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[6] in planet]
				eighth_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[7] in planet]
				twelfth_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[11] in planet]


				print('\n\n######################################### RESULTS #########################################')

				if(groom_dasa == bride_dasa):
					print('\n\tSame dasa running, check bukthi to proceed further')
				elif(groom_dasa in ['suryan','guru'] or (nathan for nathan in natchatra_nathan.get(groom_dasa_nathan) if nathan in ['sani','sukran','rahu','ketu'])):
					print('\n\tIncompatible dasa running for groom')
				else: 
					pass
				
				if(groom_lagna_house.index(suryan_house[0]) in [6,7,11]):
					print('\n\tSurya Dosham!')
				else:
					pass

				if(groom_lagna_house.index(sani_house[0]) in [0,1,4,6,7,11]):
					print('\n\tSani Dosham!')
					if (sani_natchatra_athipathi in lagna_subar.get(groom_lagna)):
						print('\t\tMitigated by lagna subar saaram')
					elif sani_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sani_house[0])) in [4,6,8]):
						print('\t\tAttained nivarthi by guru influence')
					elif sani_house[0] in ['makara', 'kumbha']:
						print('\t\tAttained nivarthi by aatchi')
				else:
					pass
				
				if(groom_lagna_house.index(rahu_house[0]) in [0,1,4,6,7,11]):
					if(groom_lagna_house.index(rahu_house[0]) in [4,11]):
						print('\n\tMild Rahu Dhosham')
						if (rahu_natchatra_athipathi in lagna_subar.get(groom_lagna)):
							print('\t\tMitigated by lagna subar saaram')
						elif rahu_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(rahu_house[0])) in [4,6,8]):
							print('\t\tAttained nivarthi by guru influence')
					else:	
						print('\n\tRahu Dosham!')
						if (rahu_natchatra_athipathi in lagna_subar.get(groom_lagna)):
							print('\t\tMitigated by lagna subar saaram')
						elif rahu_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(rahu_house[0])) in [4,6,8]):
							print('\t\tAttained nivarthi by guru influence')
				else:
					pass
				if(groom_lagna_house.index(ketu_house[0]) in [0,1,4,6,7,11]):
					if(groom_lagna_house.index(ketu_house[0]) in [4,11]):
						print('\n\tMild Ketu Dhosham')
						if (ketu_natchatra_athipathi in lagna_subar.get(groom_lagna)):
							print('\t\tMitigated by lagna subar saaram')
						elif ketu_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(ketu_house[0])) in [4,6,8]):
							print('\t\tAttained nivarthi by guru influence')
					else:	
						print('\n\tKetu Dosham!')
						if (ketu_natchatra_athipathi in lagna_subar.get(groom_lagna)):
							print('\t\tMitigated by lagna subar saaram')
						elif ketu_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(ketu_house[0])) in [4,6,8]):
							print('\t\tAttained nivarthi by guru influence')
				else:
					pass

				if(groom_lagna_house.index(sevvai_house[0]) in [1,3,6,7,11]) or (abs(groom_lagna_house.index(chandran_house[0]) - groom_lagna_house.index(sevvai_house[0])) in [1,3,6,7,11]):	
					print('\n\tSevvai Dosham! Sevvai in 2,4,7,8,12 places from lagnam or rasi')
					if(groom_lagna_house[0] in ['mesha','karkadaga','simha','vrichiga','dhanusu','meena']):
						print('\t\tAttained nivarthi by exceptional lagna property')
					elif sevvai_house[0] in ['mesha','vrichiga']:
						print('\t\tAttained nivarthi by own house property')
					elif sevvai_house[0] == 'makaram':
						if not groom_lagna_house[0] in ['mithuna','kumba']:
							print('\t\tAttained nivarthi by uchcham property')
					elif sevvai_house[0] == 'karkadaga':
						print('\t\tAttained nivarthi by neecham property')
					elif sevvai_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sevvai_house[0])) in [4,6,8]):
						print('\t\tAttained nivarthi by guru influence')
					elif (sevvai_natchatra_athipathi in lagna_subar.get(groom_lagna)):
							print('\t\tAttained nivarthi by lagna subar saaram')			
				else:
					pass

				if(chandran_house[0] == ketu_house[0]):
					print('\n\tChandran-ketu together!')
					if(chandran_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chandran_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass
				
				if(chandran_house[0] == budhan_house[0]):
					print('\n\tChandran-budhan together!')
					if(chandran_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chandran_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass
				
				if(sukran_house[0] == ketu_house[0]):
					print('\n\tSukran-ketu together!')
					if(sukran_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukran_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass
				
				if(sevvai_house[0] == sani_house[0]):
					print('\n\tSevvai-sani together!')
					if(sevvai_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sevvai_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass

				if(sukran_house[0] == chandran_house[0]):
					print('\n\tSukran-chandran together!')
					if(chandran_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chandran_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass

				if(chandran_house[0] == sani_house[0]):
					print('\n\tChandran-sani together!')
					if(chandran_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chandran_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass
				
				if(sukran_house[0] == sevvai_house[0]):
					print('\n\tSevvai-sukran together!')
					if(sukran_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukran_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass

				if(sukran_house[0] == suryan_house[0]):
					print('\n\tSuryan-sukran together!')
					if(sukran_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukran_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass

				if(seventh_house[0] == suryan_house[0] or seventh_house[0] == sani_house[0]  or seventh_house[0] == rahu_house[0] or seventh_house[0] == ketu_house[0] or seventh_house[0] == sevvai_house[0]):
					print('\n\t7th house planet with either suryan, rahu, ketu, sevvai or sani')
					if(seventh_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')				
				else:
					pass

				if(sukran_house[0] == suryan_house[0] or sukran_house[0] == sani_house[0]  or sukran_house[0] == rahu_house[0] or sukran_house[0] == ketu_house[0] or sukran_house[0] == sevvai_house[0]):
					print('\n\tSukran with either suryan, rahu, ketu, sevvai or sani')
					if(sukran_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukran_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass

				if(sixth_house[0] == seventh_house[0] or seventh_house[0] == eighth_house[0] or seventh_house[0] == twelfth_house[0]):
					print('\n\t6 and 7 or 7 and 8 or 7 and 12 house planets together')
					if(seventh_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')				
				elif(second_house[0] == sixth_house[0] or second_house[0] == eighth_house[0] or second_house[0] == twelfth_house[0]):
					print('\n\t2 and 6 or 2 and 8 or 2 and 12 house planets together')
					if(second_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(second_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')				
				elif(sukran_house[0] == sixth_house[0] or sukran_house[0] == eighth_house[0] or sukran_house[0] == twelfth_house[0]):
					print('\n\tSukran and 6 or sukran and 8 or sukran and 12 house planets together')
					if(sukran_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukran_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass

				# Extracting the 7th, 8th and 10th house needed to check kalathara dosham
				k_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[6] in planet]
				k_house1 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[7] in planet]
				k_house2 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[9] in planet]
				# Getting the house where the 7th house owner planet currently resides in the chart
				neecham_house_check = [house  for (house, planet) in groom_chart.items() if planet_list[house_list.index(k_house[0])] in planet]
				
				if(groom_lagna_house.index(k_house[0]) in [2,4]):
					print('\n\tKalathara Dosham!')
					if(k_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				elif (groom_lagna_house.index(k_house1[0]) == 4):
					print('\n\tKalathara Dosham!')
					if(k_house1[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				elif (groom_lagna_house.index(k_house2[0]) == 6):
					print('\n\tKalathara Dosham!')
					if(k_house2[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				elif (planet_list[house_list.index(k_house[0])] in neecham_houses.get(neecham_house_check[0])):
					print('\n\tKalathara Dosham!')
					if(k_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])) in [4,6,8])):
						print('\t\tAttained nivarthi by guru influence')
				else:
					pass
				
				if((abs(groom_lagna_house.index(chandran_house[0])-groom_lagna_house.index(sani_house[0])) in [2,6,9]) or chandran_house[0] == sani_house[0] or chandran_house[0] in ['makara','kumbha'] or sani_house[0] == 'karkadaga' or sani_natchatram in natchatra_nathan.get('chandran') or natchatram_response in natchatra_nathan.get('sani')):
					print('\n\tPunarpu Dosham!')
				else:
					pass
				
				# Extracting 5th, 7th and 8th house from lagnam needed for putra dosham
				p_house_5 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[4] in planet]
				p_house_7 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[6] in planet]
				p_house_8 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[7] in planet]
				p_house_12 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[11] in planet]
				if groom_lagna_house.index(p_house_5[0]) == 7 or groom_lagna_house.index(p_house_7[0]) == 4:
					print('\n\tPutra Dosham!')
				elif p_house_5 == groom_lagna_house[7] and p_house_7 == groom_lagna_house[4]:
					print('\n\tPutra Dosham!')
				elif p_house_5 == groom_lagna_house[7] and p_house_8 == groom_lagna_house[4]:
					print('\n\tPutra Dosham!')
				elif p_house_5 == groom_lagna_house[11] and p_house_12 == groom_lagna_house[4]:
					print('\n\tPutra Dosham!')
				elif groom_lagna_house.index(sevvai_house[0]) == 0 or groom_lagna_house.index(sani_house[0]) == 6 or groom_lagna_house.index(suryan_house[0]) == 11:
					print('\n\tPutra Dosham')
				elif (abs(groom_lagna_house.index(chandran_house[0]) - groom_lagna_house.index(sani_house[0])) in [2,6,9]) or (abs(0 #This is Lagna index value
				- groom_lagna_house.index(sani_house[0])) in [2,6,9]) or (abs(groom_lagna_house.index(p_house_5[0])-groom_lagna_house.index(sani_house[0])) in [2,6,9]):
					print('\n\tPutra Dosham')
				elif (groom_lagna_house.index(sani_house[0]) in [0,4,7,11] or groom_lagna_house.index(sevvai_house[0]) in [0,4,7,11]):
					print('\n\tPutra Dosham')
				elif (p_house_5 == sevvai_house[0] and groom_lagna_house.index(sevvai_house[0]) == 4 and (abs(groom_lagna_house.index(p_house_5)-groom_lagna_house.index(sani_house[0])) in [2,6,9])):
					print('\n\tPutra Dosham')
				else:
					pass
			else:	
				print('\n\tNo lagna or rasi match! Exiting')
		else: 
			print('\n\tSorry, no natchatra porutham')
		exit = input('\n\nPress any button to exit')			
	except (ValueError):
		print('\n\tIncorrect Value Entered!')
	except (RuntimeError):
		print('\n\tRuntimeError')
	except (TypeError):
		print('\n\tTypeError')
	except (NameError):
		print('\n\tNameError')
	
if __name__== "__main__":
	main()