import input

def chartParams():
    try:
        inputs = input.getInput()

        # Altering the default chart to start from the groom's lagnam
        for ghouse in range(len(inputs.house_list)):		
            if (inputs.house_list.index(inputs.groom_lagna))+ghouse >= len(inputs.house_list):	# Modifying index to obtain cyclic entry in chart
                inputs.groom_lagna_house.append(inputs.house_list[(inputs.house_list.index(inputs.groom_lagna)+ghouse)-len(inputs.house_list)])	# Houses from lagnam
                inputs.groom_planet_house.append(inputs.planet_list[(inputs.house_list.index(inputs.groom_lagna)+ghouse)-len(inputs.house_list)])	# Planet lords of each corresponding house
            else:
                inputs.groom_lagna_house.append(inputs.house_list[inputs.house_list.index(inputs.groom_lagna)+ghouse])	# Houses from lagnam
                inputs.groom_planet_house.append(inputs.planet_list[inputs.house_list.index(inputs.groom_lagna)+ghouse])	# Planet lords of each corresponding house

        # Extracting the house where the corresponding planet is residing
        inputs.sury_house = [house  for (house, planet) in inputs.groom_chart.items() if 'sury' in planet]
        inputs.rahu_house = [house  for (house, planet) in inputs.groom_chart.items() if 'rahu' in planet]
        inputs.ketu_house = [house  for (house, planet) in inputs.groom_chart.items() if 'ketu' in planet]
        inputs.sani_house = [house  for (house, planet) in inputs.groom_chart.items() if 'sani' in planet]
        inputs.chev_house = [house  for (house, planet) in inputs.groom_chart.items() if 'chev' in planet]
        inputs.chan_house = [house  for (house, planet) in inputs.groom_chart.items() if 'chan' in planet]
        inputs.budh_house = [house  for (house, planet) in inputs.groom_chart.items() if 'budh' in planet]
        inputs.sukr_house = [house  for (house, planet) in inputs.groom_chart.items() if 'sukr' in planet]
        inputs.guru_house = [house  for (house, planet) in inputs.groom_chart.items() if 'guru' in planet]
        inputs.second_house = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[1] in planet]
        inputs.sixth_house = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[5] in planet]
        inputs.seventh_house = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[6] in planet]
        inputs.eighth_house = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[7] in planet]
        inputs.twelfth_house = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[11] in planet]

        # Paava grahas index values from chart
        inputs.chev_index = inputs.groom_lagna_house.index(inputs.chev_house[0])
        inputs.sani_index = inputs.groom_lagna_house.index(inputs.sani_house[0])
        inputs.sury_index = inputs.groom_lagna_house.index(inputs.sury_house[0])
        inputs.rahu_index = inputs.groom_lagna_house.index(inputs.rahu_house[0])
        inputs.ketu_index = inputs.groom_lagna_house.index(inputs.ketu_house[0])

        # Extracting the 7th, 8th and 10th house needed to check kalathara dosham
        inputs.k_house = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[6] in planet]
        inputs.k_house1 = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[7] in planet]
        inputs.k_house2 = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[9] in planet]
        # Getting the house where the 7th house lord currently resides in the chart
        inputs.neecham_house_check = [house  for (house, planet) in inputs.groom_chart.items() if inputs.planet_list[inputs.house_list.index(inputs.k_house[0])] in planet]
        
            
        # Extracting 5th, 7th and 8th house from lagnam needed for putra dosham
        inputs.p_house_5 = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[4] in planet]
        inputs.p_house_7 = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[6] in planet]
        inputs.p_house_8 = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[7] in planet]
        inputs.p_house_12 = [house  for (house, planet) in inputs.groom_chart.items() if inputs.groom_planet_house[11] in planet]
    
    except Exception as e:
	    print("Exception is: ", e)
        
    return inputs