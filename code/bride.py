import init
class rasi_chart():
    try:
        ini_b = init.chartInit()
        bride_lagna_house = []
        bride_planet_house = []
        lagna = 'kanya'
        chan = 'meena'
        dasa = 'sukr'
        bukthi = 'chan'
        chart = {'mesha':['empty'],'rishaba':['empty'],'mithuna':['guru'],'karkadaga':['ketu'],'simha':['empty'],'kanya':['empty'],'thula':['chev'],'vrichiga':['sury'],'dhanusu':['sani','budh'],'makara':['rahu','sukr'],'kumbha':['empty'],'meena':['chan']}
        plan_degs = {'lagna': 26.72028, 'chev': 29.22194, 'sury': 22.11667, 'sani': 19.19861, 'budh': 6.777222, 'rahu': 25.08361, 'sukr': 4.893611, 'chan': 15.7}
        # Altering the default chart to start from the groom's lagnam
        for bhouse in range(len(ini_b.house_list)):		
            if (ini_b.house_list.index(lagna))+bhouse >= len(ini_b.house_list):	# Modifying index to obtain cyclic entry in chart
                bride_lagna_house.append(ini_b.house_list[(ini_b.house_list.index(lagna)+bhouse)-len(ini_b.house_list)])	# Houses from lagnam
                bride_planet_house.append(ini_b.planet_list[(ini_b.house_list.index(lagna)+bhouse)-len(ini_b.house_list)])	# Planet lords of each corresponding house
            else:
                bride_lagna_house.append(ini_b.house_list[ini_b.house_list.index(lagna)+bhouse])	# Houses from lagnam
                bride_planet_house.append(ini_b.planet_list[ini_b.house_list.index(lagna)+bhouse])	# Planet lords of each corresponding house
        # print(chart['makara'])
        # Extracting the house where the corresponding planet is residing
        sury_house = ['vrichiga']
        rahu_house = ['makara']
        ketu_house = ['karkadaga']
        sani_house = ['dhanusu']
        chev_house = ['thula']
        chan_house = ['meena']
        budh_house = ['dhanusu']
        sukr_house = ['makara']
        guru_house = ['mithuna']
        # Following variables say where that house lord is currently at.
        house_2 = ['makara']
        house_5 = ['dhanusu']
        house_6 = ['dhanusu']
        house_7 = ['mithuna']
        house_8 = ['thula']
        house_10 = ['dhanusu']
        house_12 = ['vrichiga']

        # Paava grahas index values from chart
        chev_index = 2
        sani_index = 4
        sury_index = 3
        rahu_index = 5
        ketu_index = 11        

        # Getting the house where the 7th and 10th house lord currently resides in the chart
        neecham_house_check_7 = ['mithuna']
        neecham_house_check_10 = ['dhanusu']
    
    except Exception as e:
        print("Exception in bride.py rasi_chart is: ", e)
##################################################################################################################################################################################

class navamsa_chart():

    chart = {'mesha':['empty'],'rishaba':['empty'],'mithuna':['chev', 'budh'],'karkadaga':['empty'],'simha':['rahu'],'kanya':['sani'],'thula':['empty'],'vrichiga':['chan'],'dhanusu':['empty'],'makara':['sury'],'kumbha':['ketu', 'sukr', 'guru'],'meena':['empty']}
