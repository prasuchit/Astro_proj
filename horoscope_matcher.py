#!/usr/bin/env python

# Feeding in bride specific details
bride_lagna = 'kanya'
bride_chan = 'meena'
bride_dasa = 'sukr'
dosha_match_count = 0
# List of houses in clockwise order
house_list = ['mesha','rishaba','mithuna','karkadaga','simha','kanya','thula','vrichiga','dhanusu','makara','kumbha','meena']
# List of planets in clockwise order
planet_list = ['chev','sukr','budh','chan','sury', 'budh','sukr','chev','guru','sani','sani','guru']
# Compatible natchatram list for Cena
natchatra_list = ['aayilyam','hastham','kettai','magam','punarpoosam','revathi','rohini','sadhayam','swathi','tiruvadurai','tiruvonam','uthram','uthradam']
# Dictionary mapping of lagna subar planets for each house
lagna_subar = {'mesha':['chev','sury','guru'],'rishaba':['sukr','budh','sani'],'mithuna':['budh','sukr','sani'],'karkadaga':['chan','chev','guru'],'simha':['sury','chev','guru'],'kanya':['budh','sukr','sani'],'thula':['sukr','sani','budh'],'vrichiga':['chev','guru','sury'],'dhanusu':['guru','chev','sury'],'makara':['sani','sukr','budh'],'kumbha':['sani','budh','sukr'],'meena':['guru','chan','chev']}
# Dictionary mapping of natchatra nathan natchatrams for each planet
natchatra_nathan = {'ketu':['aswini','magam','moolam'],'sukr':['barani','pooram','pooradam'],'sury':['krithigai','uthram','uthradam'],'chan':['rohini','hastham','tiruvonam'],'chev':['mrigasirisham', 'chithirai','avittam'],'rahu':['tiruvadurai','swathi','sadhayam'],'guru':['punarpoosam','visaagam','poorattadhi'],'sani':['poosam','anusham','uthrattadhi'],'budh':['aayilyam','revathi','kettai']}
#Dictionary maping of neecham planets for each house
neecham_houses = {'mesha':['sani'],'rishaba':['rahu','ketu'],'mithuna':['empty'],'karkadaga':['chev'],'simha':['empty'],'kanya':['sukr'],'thula':['sury'],'vrichiga':['chan'],'dhanusu':['empty'], 'makara':['guru'],'kumbha':['empty'],'meena':['budh']}

##################################################################################################################################################################################

def main():
	try:
		groom_chart = {}
		planets_in_house = []
		groom_lagna_house = []
		groom_planet_house = []
		print('Compatible natchatram list: \n\t')
		print(", ".join(natchatra_list))
		natchatram_response = input("\nEnter Groom natchatra:	")
		# natchatram_response = 'uthram'
		if natchatram_response in natchatra_list:
			print("\nList of houses: \n\t")
			print(", ".join(house_list))
			groom_lagna = input("\nEnter groom's lagna:	")
			groom_chan = input("\nEnter groom's rasi:	")
			
			# groom_lagna = 'karkadaga'
			# groom_chan = 'mesha'
			# groom_dasa = 'guru'
			# groom_dasa_nathan = 'chan'
			# sani_natchatram = ' '
			# Checking if lagnam and rasi of groom and bride are not in 6th or 8th positions from one another
			lagna_check = abs(house_list.index(bride_lagna) - house_list.index(groom_lagna))
			rasi_check = abs(house_list.index(bride_chan) - house_list.index(groom_chan))
			# Start filling the rasi chart
			print('\nList of planets: \n\n\tbudh, chan, guru, ketu, rahu, sani, chev, sukr, sury')
			groom_dasa = input("\nEnter groom's currently running dasa: ")
			groom_dasa_nathan = input("\nEnter groom's dasa natchatra nathan: ")
			print('\nList of natchatrams:\n\n\taayilyam, anusham, aswini, avittam, barani, chithirai,  hastham, kettai, krithigai,\n\t magam, moolam, mrigasirisham, pooradam, pooram, poorattadhi, poosam,  punarpoosam, revathi,\n\t rohini, sadhayam, swathi, tiruvonam, tiruvadurai, uthram,  uthradam, uthrattadhi, visaagam')
			sani_natchatram = input("\nEnter sani's natchatram from chart: ")
			chev_natchatra_athipathi = input("Enter chev's saara nathan: ")
			rahu_natchatra_athipathi = input("Enter Rahu's saara nathan: ")
			ketu_natchatra_athipathi = input("Enter Ketu's saara nathan: ")
			sani_natchatra_athipathi = input("Enter Sani's saara nathan: ")
			# rahu_natchatra_athipathi = 'rahu'
			# ketu_natchatra_athipathi = 'ketu'
			# sani_natchatra_athipathi = 'guru'
			# chev_natchatra_athipathi = ' '
			print('\nLets start filling the chart: ')
			for house in house_list:
				print('\nHow many planets does %s house have?	' %house)
				pnum = int(input())
				
				if pnum == 0:
					planets_in_house.append('empty')
					
				else:
					print('\nList of planets: \n\n\tbudh, chan, guru, ketu, rahu, sani, chev, sukr, sury')
					for num in range(pnum):
						planet_name = input('Enter planet:	')
						planets_in_house.append(planet_name)
				groom_chart.update({house:planets_in_house})
				planets_in_house = []
				

			# groom_chart = {'mesha':'chan','rishaba':'empty','mithuna':'empty','karkadaga':'empty','simha':'ketu','kanya':'sani','thula':'chev','vrichiga':['budh','sukr'],'dhanusu':'sury','makara':'empty','kumbha':'rahu','meena':'guru'}
			

			# Altering the default chart to start from the groom's lagnam
			for ghouse in range(len(house_list)):		
				if (house_list.index(groom_lagna))+ghouse >= len(house_list):	# Modifying index to obtain cyclic entry in chart
					groom_lagna_house.append(house_list[(house_list.index(groom_lagna)+ghouse)-len(house_list)])	# Houses from lagnam
					groom_planet_house.append(planet_list[(house_list.index(groom_lagna)+ghouse)-len(house_list)])	# Planet lords of each corresponding house
				else:
					groom_lagna_house.append(house_list[house_list.index(groom_lagna)+ghouse])	# Houses from lagnam
					groom_planet_house.append(planet_list[house_list.index(groom_lagna)+ghouse])	# Planet lords of each corresponding house
			# print(groom_chart)
			# print(groom_lagna_house)
			# print(groom_planet_house)

			# Extracting the house where the corresponding planet is residing
			sury_house = [house  for (house, planet) in groom_chart.items() if 'sury' in planet]
			rahu_house = [house  for (house, planet) in groom_chart.items() if 'rahu' in planet]
			ketu_house = [house  for (house, planet) in groom_chart.items() if 'ketu' in planet]
			sani_house = [house  for (house, planet) in groom_chart.items() if 'sani' in planet]
			chev_house = [house  for (house, planet) in groom_chart.items() if 'chev' in planet]
			chan_house = [house  for (house, planet) in groom_chart.items() if 'chan' in planet]
			budh_house = [house  for (house, planet) in groom_chart.items() if 'budh' in planet]
			sukr_house = [house  for (house, planet) in groom_chart.items() if 'sukr' in planet]
			guru_house = [house  for (house, planet) in groom_chart.items() if 'guru' in planet]
			second_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[1] in planet]
			sixth_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[5] in planet]
			seventh_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[6] in planet]
			eighth_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[7] in planet]
			twelfth_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[11] in planet]

			# Paava grahas index values from chart
			chev_index = groom_lagna_house.index(chev_house[0])
			sani_index = groom_lagna_house.index(sani_house[0])
			sury_index = groom_lagna_house.index(sury_house[0])
			rahu_index = groom_lagna_house.index(rahu_house[0])
			ketu_index = groom_lagna_house.index(ketu_house[0])

##################################################################################################################################################################################

			print('\n\n######################################### RESULTS #########################################')
			print('\nDOSHAM LIST:')
			if (lagna_check in [5,7]):
				print('\n\tLagnam in ',lagna_check)
			if (rasi_check in [5,7]):
				print('\n\tRasi in ',rasi_check)
			if(groom_dasa == bride_dasa):
				print('\n\tSame ',groom_dasa,' dasa running, check bukthi to proceed further')
			elif(groom_dasa in ['sury','guru']):
				print('\n\tIncompatible dasa running for groom! ',groom_dasa,' dasa running')
			elif(groom_dasa_nathan in ['sani','sukr','rahu','ketu']):
				print('\n\tIncompatible dasa running for groom! Dasa natchatra nathan is ', groom_dasa_nathan)
			else: 
				pass
			
			if(sury_index in [6,7,11]):
				print('\n\tSurya Dosham! Sury in ',sury_index,' house')
			else:
				pass

			if(sani_index in [0,1,4,6,7,11]):
				print('\n\tSani Dosham! Sani in ',sani_index,' house')
				if (sani_natchatra_athipathi in lagna_subar.get(groom_lagna)):
					print('\t\tMitigated by lagna subar saaram')
				elif sani_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - sani_index) in [4,6,8]):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - sani_index),' place')
				elif sani_house[0] in ['makara', 'kumbha']:
					print('\t\tAttained nivarthi by aatchi at ',sani_house[0])
			else:
				pass
			
			if(rahu_index in [0,1,4,6,7,11]):
				if(rahu_index in [4,11]):
					print('\n\tMild Rahu Dhosham! Rahu in ', rahu_index)
					# dosha_match_count = dosha_match_count + 1
					if (rahu_natchatra_athipathi in lagna_subar.get(groom_lagna)):
						print('\t\tMitigated by lagna subar saaram')
					elif rahu_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - rahu_index) in [4,6,8]):
						print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - rahu_index),' place')
				else:	
					print('\n\tRahu Dosham! Rahu in ',rahu_index)
					if (rahu_natchatra_athipathi in lagna_subar.get(groom_lagna)):
						print('\t\tMitigated by lagna subar saaram')
					elif rahu_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - rahu_index) in [4,6,8]):
						print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - rahu_index),' place')
			else:
				pass

			if(ketu_index in [0,1,4,6,7,11]):
				if(ketu_index in [4,11]):
					print('\n\tMild Ketu Dhosham! Ketu in 5 or 12')
					if (ketu_natchatra_athipathi in lagna_subar.get(groom_lagna)):
						print('\t\tMitigated by lagna subar saaram')
					elif ketu_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - ketu_index) in [4,6,8]):
						print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - ketu_index),' place')
				else:	
					print('\n\tKetu Dosham! Ketu in ',ketu_index)
					if (ketu_natchatra_athipathi in lagna_subar.get(groom_lagna)):
						print('\t\tMitigated by lagna subar saaram')
					elif ketu_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - ketu_index) in [4,6,8]):
						print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - ketu_index),' place')
			else:
				pass

			if(chev_index in [1,3,6,7,11]):
				print('\n\tChev Dosham! Chev in ',chev_index,' place from lagnam')
				if(groom_lagna_house[0] in ['mesha','karkadaga','simha','vrichiga','dhanusu','meena']):
					print('\t\tAttained nivarthi by exceptional lagna property')
				elif chev_house[0] in ['mesha','vrichiga']:
					print('\t\tAttained nivarthi by own house property')
				elif chev_house[0] == 'makaram':
					if not groom_lagna_house[0] in ['mithuna','kumba']:
						print('\t\tAttained nivarthi by uchcham property')
				elif chev_house[0] == 'karkadaga':
					print('\t\tAttained nivarthi by neecham property')
				elif chev_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - chev_index) in [4,6,8]):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - chev_index),' place')
					# dosha_match_count = dosha_match_count + 1
				elif (chev_natchatra_athipathi in lagna_subar.get(groom_lagna)):
						print('\t\tAttained nivarthi by lagna subar saaram')
			elif(abs(groom_lagna_house.index(chan_house[0]) - chev_index) in [1,3,6,7,11]):	
				print('\n\tChev Dosham! Chev in ',abs(groom_lagna_house.index(chan_house[0]) - chev_index),' place from rasi')
				if(groom_lagna_house[0] in ['mesha','karkadaga','simha','vrichiga','dhanusu','meena']):
					print('\t\tAttained nivarthi by exceptional lagna property')
				elif chev_house[0] in ['mesha','vrichiga']:
					print('\t\tAttained nivarthi by own house property')
				elif chev_house[0] == 'makaram':
					if not groom_lagna_house[0] in ['mithuna','kumba']:
						print('\t\tAttained nivarthi by uchcham property')
				elif chev_house[0] == 'karkadaga':
					print('\t\tAttained nivarthi by neecham property')
				elif chev_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - chev_index) in [4,6,8]):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - chev_index),' place')
				elif (chev_natchatra_athipathi in lagna_subar.get(groom_lagna)):
						print('\t\tAttained nivarthi by lagna subar saaram')			
			else:
				pass
	
			# Extracting the 7th, 8th and 10th house needed to check kalathara dosham
			k_house = [house  for (house, planet) in groom_chart.items() if groom_planet_house[6] in planet]
			k_house1 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[7] in planet]
			k_house2 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[9] in planet]
			# Getting the house where the 7th house lord currently resides in the chart
			neecham_house_check = [house  for (house, planet) in groom_chart.items() if planet_list[house_list.index(k_house[0])] in planet]
			
			if(groom_lagna_house.index(k_house[0]) in [2,4]):
				print('\n\tKalathara Dosham! 7th house lord in ',groom_lagna_house.index(k_house[0]),' place')
				if(k_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])),' place')
			elif (groom_lagna_house.index(k_house1[0]) == 4):
				print('\n\tKalathara Dosham! 8th house lord in 5th place')
				if(k_house1[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])),' place')
			elif (groom_lagna_house.index(k_house2[0]) == 6):
				print('\n\tKalathara Dosham! 10th house lord in 7th place')
				if(k_house2[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])),' place')
			elif (planet_list[house_list.index(k_house[0])] in neecham_houses.get(neecham_house_check[0])):
				print('\n\tKalathara Dosham! 7th house lord attaining neecham')
				if(k_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(k_house[0])),' place')
			else:
				pass
			
			if(((groom_lagna_house.index(chan_house[0])-sani_index) in [2,6,9])): 
				print('\n\tPunarpu Dosham! Sani influence on chan')
			elif(chan_house[0] == sani_house[0]): 
				print('\n\tPunarpu Dosham! Sani and chan together')
			elif(chan_house[0] in ['makara','kumbha']):
				print('\n\tPunarpu Dosham! chan in Makara or kumbha rasi')
			elif(sani_house[0] == 'karkadaga'):
				print('\n\tPunarpu Dosham! Sani in Karkadaga rasi')
			elif(sani_natchatram in natchatra_nathan.get('chan')):
				print('\n\tPunarpu Dosham! Sani natchatram in chan natchatra nathan list')
			elif(natchatram_response in natchatra_nathan.get('sani')):
				print('\n\tPunarpu Dosham! chan natchatram in sani natchatra nathan list')
			else:
				pass
			
			# Extracting 5th, 7th and 8th house from lagnam needed for putra dosham
			p_house_5 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[4] in planet]
			p_house_7 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[6] in planet]
			p_house_8 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[7] in planet]
			p_house_12 = [house  for (house, planet) in groom_chart.items() if groom_planet_house[11] in planet]
			if groom_lagna_house.index(p_house_5[0]) == 6:
				print('\n\tPutra Dosham! 5th house lord in 7th place')
			elif groom_lagna_house.index(p_house_7[0]) == 4:
				print('\n\tPutra Dosham! 7th house lord in 5th place')
			elif p_house_5 == groom_lagna_house[7] and p_house_7 == groom_lagna_house[4]:
				print('\n\tPutra Dosham! 5th house lord in 8th house and 7th house lord in 5th house')
			elif p_house_5 == groom_lagna_house[7] and p_house_8 == groom_lagna_house[4]:
				print('\n\tPutra Dosham! 5th house lord in 8th house and 8th house lord in 5th house')
			elif p_house_5 == groom_lagna_house[11] and p_house_12 == groom_lagna_house[4]:
				print('\n\tPutra Dosham! 5th house lord in 12th house and 12th house lord in 5th house')
			elif chev_index == 0:
				print('\n\tPutra Dosham! chev in lagnam')
			elif sani_index == 6:	  
				print('\n\tPutra Dosham! Sani in 7th house')
			elif sury_index == 11:
				print('\n\tPutra Dosham! sury in 12th house')
			elif (abs(groom_lagna_house.index(chan_house[0]) - sani_index) in [2,6,9]):
				print('\n\tPutra Dosham! Sani parvai on chan')
			elif ((0 #This is Lagna index value
					- sani_index) in [2,6,9]):
				print('\n\tPutra Dosham! Sani parvai on lagnam')
			elif ((groom_lagna_house.index(p_house_5[0])-sani_index) in [2,6,9]):
				print('\n\tPutra Dosham! Sani parvai on 5th house')
			elif (sani_index in [0,4,7,11]): 
				print('\n\tPutra Dosham! Sani in ', sani_index,' house')
			elif (chev_index in [0,4,7,11]):
				print('\n\tPutra Dosham! Chev in ',chev_index,' house')
			elif (p_house_5 == chev_house[0] and chev_index == 4 and ((groom_lagna_house.index(p_house_5)-sani_index) in [2,6,9])):
				print('\n\tPutra Dosham! 5th house lord with chev, both(5th house lord and chev) currently in 5th place and have sani paarvai')
			else:
				pass
##################################################################################################################################################################################
			print('\nPLANETORY CONJUNCTION:\n')

			if(chan_house[0] == ketu_house[0]):
				print('\n\tchan-ketu together!')
				if(chan_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chan_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chan_house[0])),' place')
			else:
				pass
			
			if(chan_house[0] == budh_house[0]):
				print('\n\tchan-budh together!')
				if(chan_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chan_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chan_house[0])),' place')
			else:
				pass
			
			if(sukr_house[0] == ketu_house[0]):
				print('\n\tsukr-ketu together!')
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])),' place')
			else:
				pass
			
			if(chev_house[0] == sani_house[0]):
				print('\n\tchev-sani together!')
				if(chev_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - chev_index) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - chev_index),' place')
			else:
				pass

			if(sukr_house[0] == chan_house[0]):
				print('\n\tsukr-chan together!')
				if(chan_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chan_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chan_house[0])),' place')
			else:
				pass

			if(chan_house[0] == sani_house[0]):
				print('\n\tchan-sani together!')
				if(chan_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chan_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(chan_house[0])),' place')
			else:
				pass
			
			if(sukr_house[0] == chev_house[0]):
				print('\n\tchev-sukr together!')
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])),' place')
			else:
				pass

			if(sukr_house[0] == sury_house[0]):
				print('\n\tsury-sukr together!')
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])),' place')
			else:
				pass

			if(seventh_house[0] == sury_house[0]):
				print('\n\t7th house lord with sury')
				if(seventh_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])),' place')				
			elif(seventh_house[0] == sani_house[0]):
				print('\n\t7th house lord with sani')
				if(seventh_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])),' place')				
			if(seventh_house[0] == rahu_house[0]):
				print('\n\t7th house lord with rahu')
				if(seventh_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])),' place')				
			if(seventh_house[0] == ketu_house[0]):
				print('\n\t7th house lord with ketu')
				if(seventh_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])),' place')				
			if(seventh_house[0] == chev_house[0]):
				print('\n\t7th house lord with chev')
				if(seventh_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])),' place')				
			else:
				pass

			if(sukr_house[0] == sury_house[0]):
				print('\n\tsukr with sury')
				# dosha_match_count = dosha_match_count + 1
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - sani_index),' place')
			elif(sukr_house[0] == rahu_house[0]):
				print('\n\tsukr with rahu')
				# dosha_match_count = dosha_match_count + 1
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - sani_index),' place')
			elif(sukr_house[0] == ketu_house[0]):
				print('\n\tsukr with ketu')
				# dosha_match_count = dosha_match_count + 1
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - sani_index),' place')
			elif(sukr_house[0] == chev_house[0]):
				print('\n\tsukr with chev')
				# dosha_match_count = dosha_match_count + 1
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - sani_index),' place')
			elif(sukr_house[0] == sani_house[0]):
				print('\n\tsukr with sani')
				# dosha_match_count = dosha_match_count + 1
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - sani_index),' place')
			else:
				pass

			if(sixth_house[0] == seventh_house[0]): 
				print('\n\t6 and 7th house lords together') 
				if(seventh_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])),' place')				
			else:
				pass
			if (seventh_house[0] == eighth_house[0]): 
				print('\n\t7 and 8th house lords together') 
				if(seventh_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])),' place')				
			else:
				pass
			if (seventh_house[0] == twelfth_house[0]):
				print('\n\t7 and 12th house lords together')
				if(seventh_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(seventh_house[0])),' place')				
			else:
				pass
			if(second_house[0] == sixth_house[0]): 
				print('\n\t2 and 6th house lords together')
				if(second_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(second_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(second_house[0])),' place')	
			else:
				pass
			if(second_house[0] == eighth_house[0]): 
				print('\n\t2 and 8th house lords together')
				if(second_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(second_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(second_house[0])),' place')	
			else:
				pass
			if(second_house[0] == twelfth_house[0]):
				print('\n\t2 and 12th house lords together')
				if(second_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(second_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(second_house[0])),' place')				
			else:
				pass
			if(sukr_house[0] == sixth_house[0]):
				print('\n\tsukr and 6th house lords together') 
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])),' place')
			else:
				pass
			if(sukr_house[0] == eighth_house[0]): 
				print('\n\tsukr and 8th house lords together') 
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])),' place')
			else:
				pass
			if(sukr_house[0] == twelfth_house[0]):
				print('\n\tsukr and 12th house lords together')
				if(sukr_house[0] == guru_house[0] or (abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])) in [4,6,8])):
					print('\t\tAttained nivarthi by guru influence at: ',abs(groom_lagna_house.index(guru_house[0]) - groom_lagna_house.index(sukr_house[0])),' place')
			else:
				pass
##################################################################################################################################################################################

			# if(dosha_match_count == 3):
			# 	print('DOSHAM COMBINATION MATCHING WITH BRIDE! SUITABLE MATCH')
			# else:
			# 	print('DOSHAM COMBINATION NOT MATCHING WITH BRIDE!')
			
			print('\n\n###################################### END OF RESULTS ######################################')
			
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