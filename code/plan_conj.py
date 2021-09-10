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

    if(params.house_7[0] == params.sury_house[0]):
        params.f.write("\n\t7th house lord with sury")
        if(params.house_7[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0]))+1)+" place")				
    elif(params.house_7[0] == params.sani_house[0]):
        params.f.write("\n\t7th house lord with sani")
        if(params.house_7[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0]))+1)+" place")				
    if(params.house_7[0] == params.rahu_house[0]):
        params.f.write("\n\t7th house lord with rahu")
        if(params.house_7[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0]))+1)+" place")				
    if(params.house_7[0] == params.ketu_house[0]):
        params.f.write("\n\t7th house lord with ketu")
        if(params.house_7[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0]))+1)+" place")				
    if(params.house_7[0] == params.chev_house[0]):
        params.f.write("\n\t7th house lord with chev")
        if(params.house_7[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0]))+1)+" place")				
    else:
        pass

    if(params.sukr_house[0] == params.sury_house[0]):
        params.f.write("\n\tsukr with sury")
        if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) +1)+" place")
    elif(params.sukr_house[0] == params.rahu_house[0]):
        params.f.write("\n\tsukr with rahu")
        if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) +1)+" place")
    elif(params.sukr_house[0] == params.ketu_house[0]):
        params.f.write("\n\tsukr with ketu")
        if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) +1)+" place")
    elif(params.sukr_house[0] == params.chev_house[0]):
        params.f.write("\n\tsukr with chev")
        if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) +1)+" place")
    elif(params.sukr_house[0] == params.sani_house[0]):
        params.f.write("\n\tsukr with sani")
        if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.sani_index) +1)+" place")
    else:
        pass

    if(params.house_6[0] == params.house_7[0]): 
        params.f.write("\n\t6 and 7th house lords together") 
        if(params.house_7[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0]))+1)+" place")				
    else:
        pass
    if (params.house_7[0] == params.house_8[0]): 
        params.f.write("\n\t7 and 8th house lords together") 
        if(params.house_7[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0]))+1)+" place")				
    else:
        pass
    if (params.house_7[0] == params.house_12[0]):
        params.f.write("\n\t7 and 12th house lords together")
        if(params.house_7[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_7[0]))+1)+" place")				
    else:
        pass
    if(params.house_2[0] == params.house_6[0]): 
        params.f.write("\n\t2 and 6th house lords together")
        if(params.house_2[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_2[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_2[0]))+1)+" place")	
    else:
        pass
    if(params.house_2[0] == params.house_8[0]): 
        params.f.write("\n\t2 and 8th house lords together")
        if(params.house_2[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_2[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_2[0]))+1)+" place")	
    else:
        pass
    if(params.house_2[0] == params.house_12[0]):
        params.f.write("\n\t2 and 12th house lords together")
        if(params.house_2[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_2[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.house_2[0]))+1)+" place")				
    else:
        pass
    if(params.sukr_house[0] == params.house_6[0]):
        params.f.write("\n\tsukr and 6th house lords together") 
        if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0]))+1)+" place")
    else:
        pass
    if(params.sukr_house[0] == params.house_8[0]): 
        params.f.write("\n\tsukr and 8th house lords together") 
        if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0]))+1)+" place")
    else:
        pass
    if(params.sukr_house[0] == params.house_12[0]):
        params.f.write("\n\tsukr and 12th house lords together")
        if(params.sukr_house[0] == params.guru_house[0] or (abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0])) in [4,6,8])):
            params.f.write("\n\t\tAttained nivarthi by guru influence at: "+str(abs(params.groom_lagna_house.index(params.guru_house[0]) - params.groom_lagna_house.index(params.sukr_house[0]))+1)+" place")
    else:
        pass