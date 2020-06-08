import init
import os
def getInput():
    try:
        ini = init.chartInit()
        
        ini.groom_name = input("Enter groom's name: ")
        ini.f = open(os.path.join(ini.outpath, '%s.txt' % ini.groom_name), 'w+')
        print("Compatible natchatram list: \n\t")
        print(", ".join(ini.natchatra_list))
        ini.natchatram_response = input("\nEnter Groom natchatra:	")
        if ini.natchatram_response in ini.natchatra_list:
            print("\nList of houses: \n\t")
            print(", ".join(ini.house_list))
            ini.groom_lagna = input("\nEnter groom's lagna:	")
            ini.groom_chan = input("\nEnter groom's rasi:	")
            
            # Checking if lagnam and rasi of groom and bride are not in 6th or 8th positions from one another
            ini.lagna_check = (ini.house_list.index(ini.bride_lagna) - ini.house_list.index(ini.groom_lagna))
            ini.rasi_check = (ini.house_list.index(ini.bride_chan) - ini.house_list.index(ini.groom_chan))
            
            # Start filling the rasi chart
            print("\nList of planets: \n\n\tbudh, chan, guru, ketu, rahu, sani, chev, sukr, sury")
            ini.groom_dasa = input("\nEnter groom's currently running dasa: ")
            ini.groom_dasa_nathan = input("\nEnter groom's dasa natchatra nathan: ")
            print("\nList of natchatrams:\n\n\taayilyam, anusham, aswini, avittam, barani, chithirai,  hastham, kettai, krithigai,\n\t magam, moolam, mrigasirisham, pooradam, pooram, poorattadhi, poosam,  punarpoosam, revathi,\n\t rohini, sadhayam, swathi, tiruvonam, tiruvadurai, uthram,  uthradam, uthrattadhi, visaagam")
            ini.sani_natchatram = input("\nEnter sani's natchatram from chart: ")
            ini.chev_natchatra_athipathi = input("Enter chev's saara nathan: ")
            ini.rahu_natchatra_athipathi = input("Enter Rahu's saara nathan: ")
            ini.ketu_natchatra_athipathi = input("Enter Ketu's saara nathan: ")
            ini.sani_natchatra_athipathi = input("Enter Sani's saara nathan: ")
            print("\nLets start filling the chart: ")
            planets_in_house = []
            for house in ini.house_list:
                print("\nHow many planets does %s house have?	" %house)
                pnum = int(input())
                
                if pnum == 0:
                    planets_in_house.append("empty")
                    
                else:
                    print("\nList of planets: \n\n\tbudh, chan, guru, ketu, rahu, sani, chev, sukr, sury")
                    for num in range(pnum):
                        planet_name = input("Enter planet:	")
                        planets_in_house.append(planet_name)
                ini.groom_chart.update({house:planets_in_house})
                planets_in_house = []

        else: 
            ini.f.write("\n\tSorry, no natchatra porutham")
            
    except Exception as e:
        print("Exception is: ", e)
    return ini