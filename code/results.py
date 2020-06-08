import chart

def calcResults():
    try:
        params = chart.chartParams()
        params.f.write("\n\n######################################### RESULTS #########################################")
        params.f.write("\nDOSHAM LIST:")
        if (params.lagna_check in [5,7]):
            params.f.write("\n\tLagnam in"+ (params.lagna_check+1))
        if (params.rasi_check in [5,7]):
            params.f.write("\n\tRasi in"+ (params.rasi_check+1))
        if(params.groom_dasa == params.bride_dasa):
            params.f.write("\n\tSame "+params.groom_dasa+" dasa running, check bukthi to proceed further")
        elif(params.groom_dasa in ['sury','guru']):
            params.f.write("\n\tIncompatible dasa running for groom! "+params.groom_dasa+" dasa running")
        elif(params.groom_dasa_nathan in ['sani','sukr','rahu','ketu']):
            params.f.write("\n\tIncompatible dasa running for groom! Dasa natchatra nathan is: "+ params.groom_dasa_nathan)
        else: 
            pass
        
        if(params.sury_index in [6,7,11]):
            params.f.write("\n\tSurya Dosham! Sury in "+str(params.sury_index+1)+" house")
        else:
            pass

        if(params.sani_index in [0,1,4,6,7,11]):
            params.f.write("\n\tSani Dosham! Sani in "+str(params.sani_index+1)+" house")
            if (params.sani_natchatra_athipathi in params.lagna_subar.get(params.groom_lagna)):
                params.f.write("\t\tMitigated by lagna subar saaram")
            elif params.sani_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) in [4,6,8]):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) + 1)+" place")
            elif params.sani_house[0] in ['makara', 'kumbha']:
                params.f.write("\n\t\tAttained nivarthi by aatchi at"+params.sani_house[0])
        else:
            pass
        
        if(params.rahu_index in [0,1,4,6,7,11]):
            if(params.rahu_index in [4,11]):
                params.f.write("\n\tMild Rahu Dhosham! Rahu in "+ str(params.rahu_index+1))
                # dosha_match_count = dosha_match_count + 1
                if (params.rahu_natchatra_athipathi in params.lagna_subar.get(params.groom_lagna)):
                    params.f.write("\t\tMitigated by lagna subar saaram")
                elif params.rahu_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.rahu_index) in [4,6,8]):
                    params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.rahu_index) + 1)+" place")
            else:	
                params.f.write("\n\tRahu Dosham! Rahu in "+str(params.rahu_index+1))
                if (params.rahu_natchatra_athipathi in params.lagna_subar.get(params.groom_lagna)):
                    params.f.write("\t\tMitigated by lagna subar saaram")
                elif params.rahu_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.rahu_index) in [4,6,8]):
                    params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.rahu_index) + 1)+" place")
        else:
            pass

        if(params.ketu_index in [0,1,4,6,7,11]):
            if(params.ketu_index in [4,11]):
                params.f.write("\n\tMild Ketu Dhosham! Ketu in"+ (params.ketu_index+1))
                if (params.ketu_natchatra_athipathi in params.lagna_subar.get(params.groom_lagna)):
                    params.f.write("\t\tMitigated by lagna subar saaram")
                elif params.ketu_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.ketu_index) in [4,6,8]):
                    params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.ketu_index)+1)+" place")
            else:	
                params.f.write("\n\tKetu Dosham! Ketu in "+str(params.ketu_index+1))
                if (params.ketu_natchatra_athipathi in params.lagna_subar.get(params.groom_lagna)):
                    params.f.write("\t\tMitigated by lagna subar saaram")
                elif params.ketu_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.ketu_index) in [4,6,8]):
                    params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.ketu_index)+1)+" place")
        else:
            pass

        if(params.chev_index in [1,3,6,7,11]):
            params.f.write("\n\tChev Dosham! Chev in "+str(params.chev_index+1)+" place from lagnam")
            if(params.groom_lagna_house[0] in ['mesha','karkadaga','simha','vrichiga','dhanusu','meena']):
                params.f.write("\n\t\tAttained nivarthi by exceptional lagna property")
            elif params.chev_house[0] in ['mesha','vrichiga']:
                params.f.write("\n\t\tAttained nivarthi by own house property")
            elif params.chev_house[0] == 'makaram':
                if not params.groom_lagna_house[0] in ['mithuna','kumba']:
                    params.f.write("\n\t\tAttained nivarthi by uchcham property")
            elif params.chev_house[0] == 'karkadaga':
                params.f.write("\n\t\tAttained nivarthi by neecham property")
            elif params.chev_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.chev_index) in [4,6,8]):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.chev_index)+1)+" place")
            elif (params.chev_natchatra_athipathi in params.lagna_subar.get(params.groom_lagna)):
                    params.f.write("\n\t\tAttained nivarthi by lagna subar saaram")
        elif(abs(params.groom_lagna_house.index(params.chan_house[0]) - params.chev_index) in [1,3,6,7,11]):	
            params.f.write("\n\tChev Dosham! Chev in "+str(abs(params.groom_lagna_house.index(params.chan_house[0]) - params.chev_index) +1)+" place from rasi")
            if(params.groom_lagna_house[0] in ['mesha','karkadaga','simha','vrichiga','dhanusu','meena']):
                params.f.write("\n\t\tAttained nivarthi by exceptional lagna property")
            elif params.chev_house[0] in ['mesha','vrichiga']:
                params.f.write("\n\t\tAttained nivarthi by own house property")
            elif params.chev_house[0] == 'makaram':
                if not params.groom_lagna_house[0] in ['mithuna','kumba']:
                    params.f.write("\n\t\tAttained nivarthi by uchcham property")
            elif params.chev_house[0] == 'karkadaga':
                params.f.write("\n\t\tAttained nivarthi by neecham property")
            elif params.chev_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.chev_index) in [4,6,8]):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.chev_index)+1)+" place")
            elif (params.chev_natchatra_athipathi in params.lagna_subar.get(params.groom_lagna)):
                    params.f.write("\n\t\tAttained nivarthi by lagna subar saaram")			
        else:
            pass

        
        if(params.groom_lagna_house.index(params.k_house[0]) in [2,4]):
            params.f.write("\n\tKalathara Dosham! 7th house lord in "+str(params.groom_lagna_house.index(params.k_house[0])+1)+" place")
            if(params.k_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.k_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.k_house[0]))+1)+" place")
        elif (params.groom_lagna_house.index(params.k_house1[0]) == 4):
            params.f.write("\n\tKalathara Dosham! 8th house lord in 5th place")
            if(params.k_house1[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.k_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.k_house[0]))+1)+" place")
        elif (params.groom_lagna_house.index(params.k_house2[0]) == 6):
            params.f.write("\n\tKalathara Dosham! 10th house lord in 7th place")
            if(params.k_house2[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.k_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.k_house[0]))+1)+" place")
        elif (params.planet_list[params.house_list.index(params.k_house[0])] in params.neecham_houses.get(params.neecham_house_check[0])):
            params.f.write("\n\tKalathara Dosham! 7th house lord attaining neecham")
            if(params.k_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.k_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.k_house[0]))+1)+" place")
        else:
            pass
        
        if(((params.groom_lagna_house.index(params.chan_house[0])-params.sani_index) in [2,6,9])): 
            params.f.write("\n\tPunarpu Dosham! Sani influence on chan")
        elif(params.chan_house[0] == params.sani_house[0]): 
            params.f.write("\n\tPunarpu Dosham! Sani and chan together")
        elif(params.chan_house[0] in ['makara','kumbha']):
            params.f.write("\n\tPunarpu Dosham! chan in Makara or kumbha rasi")
        elif(params.sani_house[0] == 'karkadaga'):
            params.f.write("\n\tPunarpu Dosham! Sani in Karkadaga rasi")
        elif(params.sani_natchatram in params.natchatra_nathan.get('chan')):
            params.f.write("\n\tPunarpu Dosham! Sani natchatram in chan natchatra nathan list")
        elif(params.natchatram_response in params.natchatra_nathan.get('sani')):
            params.f.write("\n\tPunarpu Dosham! chan natchatram in sani natchatra nathan list")
        else:
            pass

        if params.groom_lagna_house.index(params.p_house_5[0]) == 6:
            params.f.write("\n\tPutra Dosham! 5th house lord in 7th place")
        elif params.groom_lagna_house.index(params.p_house_7[0]) == 4:
            params.f.write("\n\tPutra Dosham! 7th house lord in 5th place")
        elif params.p_house_5 == params.groom_lagna_house[7] and params.p_house_7 == params.groom_lagna_house[4]:
            params.f.write("\n\tPutra Dosham! 5th house lord in 8th house and 7th house lord in 5th house")
        elif params.p_house_5 == params.groom_lagna_house[7] and params.p_house_8 == params.groom_lagna_house[4]:
            params.f.write("\n\tPutra Dosham! 5th house lord in 8th house and 8th house lord in 5th house")
        elif params.p_house_5 == params.groom_lagna_house[11] and params.p_house_12 == params.groom_lagna_house[4]:
            params.f.write("\n\tPutra Dosham! 5th house lord in 12th house and 12th house lord in 5th house")
        elif params.chev_index == 0:
            params.f.write("\n\tPutra Dosham! chev in lagnam")
        elif params.sani_index == 6:	  
            params.f.write("\n\tPutra Dosham! Sani in 7th house")
        elif params.sury_index == 11:
            params.f.write("\n\tPutra Dosham! sury in 12th house")
        elif (abs(params.groom_lagna_house.index(params.chan_house[0]) - params.sani_index) in [2,6,9]):
            params.f.write("\n\tPutra Dosham! Sani parvai on chan")
        elif ((0 #This is Lagna index value
                - params.sani_index) in [2,6,9]):
            params.f.write("\n\tPutra Dosham! Sani parvai on lagnam")
        elif ((params.groom_lagna_house.index(params.p_house_5[0])-params.sani_index) in [2,6,9]):
            params.f.write("\n\tPutra Dosham! Sani parvai on 5th house")
        elif (params.sani_index in [0,4,7,11]): 
            params.f.write("\n\tPutra Dosham! Sani in "+str(params.sani_index+1)+" house")
        elif (params.chev_index in [0,4,7,11]):
            params.f.write("\n\tPutra Dosham! Chev in "+str(params.chev_index+1)+" house")
        elif (params.p_house_5 == params.chev_house[0] and params.chev_index == 4 and ((params.groom_lagna_house.index(params.p_house_5)-params.sani_index) in [2,6,9])):
            params.f.write("\n\tPutra Dosham! 5th house lord with chev, both(5th house lord and chev) currently in 5th place and have sani paarvai")
        else:
            pass
        params.f.write("\nPLANETORY CONJUNCTION:\n")

        if(params.chan_house[0] == params.ketu_house[0]):
            params.f.write("\n\tchan-ketu together!")
            if(params.chan_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.chan_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.chan_house[0]))+1)+" place")
        else:
            pass
        
        if(params.chan_house[0] == params.budh_house[0]):
            params.f.write("\n\tchan-budh together!")
            if(params.chan_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.chan_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.chan_house[0]))+1)+" place")
        else:
            pass
        
        if(params.sukr_house[0] == params.ketu_house[0]):
            params.f.write("\n\tsukr-ketu together!")
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0]))+1)+" place")
        else:
            pass
        
        if(params.chev_house[0] == params.sani_house[0]):
            params.f.write("\n\tchev-sani together!")
            if(params.chev_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.chev_index) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.chev_index)+1)+" place")
        else:
            pass

        if(params.sukr_house[0] == params.chan_house[0]):
            params.f.write("\n\tsukr-chan together!")
            if(params.chan_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.chan_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.chan_house[0]))+1)+" place")
        else:
            pass

        if(params.chan_house[0] == params.sani_house[0]):
            params.f.write("\n\tchan-sani together!")
            if(params.chan_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.chan_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.chan_house[0]))+1)+" place")
        else:
            pass
        
        if(params.sukr_house[0] == params.chev_house[0]):
            params.f.write("\n\tchev-sukr together!")
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0]))+1)+" place")
        else:
            pass

        if(params.sukr_house[0] == params.sury_house[0]):
            params.f.write("\n\tsury-sukr together!")
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0]))+1)+" place")
        else:
            pass

        if(params.seventh_house[0] == params.sury_house[0]):
            params.f.write("\n\t7th house lord with sury")
            if(params.seventh_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0]))+1)+" place")				
        elif(params.seventh_house[0] == params.sani_house[0]):
            params.f.write("\n\t7th house lord with sani")
            if(params.seventh_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0]))+1)+" place")				
        if(params.seventh_house[0] == params.rahu_house[0]):
            params.f.write("\n\t7th house lord with rahu")
            if(params.seventh_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0]))+1)+" place")				
        if(params.seventh_house[0] == params.ketu_house[0]):
            params.f.write("\n\t7th house lord with ketu")
            if(params.seventh_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0]))+1)+" place")				
        if(params.seventh_house[0] == params.chev_house[0]):
            params.f.write("\n\t7th house lord with chev")
            if(params.seventh_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0]))+1)+" place")				
        else:
            pass

        if(params.sukr_house[0] == params.sury_house[0]):
            params.f.write("\n\tsukr with sury")
            # dosha_match_count = dosha_match_count + 1
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) +1)+" place")
        elif(params.sukr_house[0] == params.rahu_house[0]):
            params.f.write("\n\tsukr with rahu")
            # dosha_match_count = dosha_match_count + 1
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) +1)+" place")
        elif(params.sukr_house[0] == params.ketu_house[0]):
            params.f.write("\n\tsukr with ketu")
            # dosha_match_count = dosha_match_count + 1
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) +1)+" place")
        elif(params.sukr_house[0] == params.chev_house[0]):
            params.f.write("\n\tsukr with chev")
            # dosha_match_count = dosha_match_count + 1
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) +1)+" place")
        elif(params.sukr_house[0] == params.sani_house[0]):
            params.f.write("\n\tsukr with sani")
            # dosha_match_count = dosha_match_count + 1
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) +1)+" place")
        else:
            pass

        if(params.sixth_house[0] == params.seventh_house[0]): 
            params.f.write("\n\t6 and 7th house lords together") 
            if(params.seventh_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0]))+1)+" place")				
        else:
            pass
        if (params.seventh_house[0] == params.eighth_house[0]): 
            params.f.write("\n\t7 and 8th house lords together") 
            if(params.seventh_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0]))+1)+" place")				
        else:
            pass
        if (params.seventh_house[0] == params.twelfth_house[0]):
            params.f.write("\n\t7 and 12th house lords together")
            if(params.seventh_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.seventh_house[0]))+1)+" place")				
        else:
            pass
        if(params.second_house[0] == params.sixth_house[0]): 
            params.f.write("\n\t2 and 6th house lords together")
            if(params.second_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.second_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.second_house[0]))+1)+" place")	
        else:
            pass
        if(params.second_house[0] == params.eighth_house[0]): 
            params.f.write("\n\t2 and 8th house lords together")
            if(params.second_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.second_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.second_house[0]))+1)+" place")	
        else:
            pass
        if(params.second_house[0] == params.twelfth_house[0]):
            params.f.write("\n\t2 and 12th house lords together")
            if(params.second_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.second_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.second_house[0]))+1)+" place")				
        else:
            pass
        if(params.sukr_house[0] == params.sixth_house[0]):
            params.f.write("\n\tsukr and 6th house lords together") 
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0]))+1)+" place")
        else:
            pass
        if(params.sukr_house[0] == params.eighth_house[0]): 
            params.f.write("\n\tsukr and 8th house lords together") 
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0]))+1)+" place")
        else:
            pass
        if(params.sukr_house[0] == params.twelfth_house[0]):
            params.f.write("\n\tsukr and 12th house lords together")
            if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
                params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0]))+1)+" place")
        else:
            pass

        params.f.write("\n\n###################################### END OF RESULTS ######################################")
        params.f.close()

    except Exception as e:
	    print("Exception is: ", e)
        
    return params