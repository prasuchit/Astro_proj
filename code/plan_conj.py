def planetoryConj(params):

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