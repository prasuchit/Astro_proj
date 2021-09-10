from bride import rasi_chart as rc
def horoscopeCompatibility(params):
    guru_index = params.groom_lagna_house.index(params.guru_house[0])
    # print(guru_index)
    params.f.write("\nSPECIAL RULES FOR COMPATIBILITY\n")
    if(params.groom_dasa in ['guru', 'budh']):
        params.f.write("\n\tGroom dasa is {} which is shashtanga\n".format(params.groom_dasa))
    if(params.groom_bukthi in ['ketu', 'sury']):
        params.f.write("\n\tGroom bukthi is {} which is shashtanga\n".format(params.groom_bukthi))
    if(params.groom_planet_house[6] in params.neecham_houses[params.neecham_house_check_7[0]]):
        params.f.write("\n\t7th lord {} neecham in groom chart".format(params.groom_planet_house[6]))
    if(params.groom_planet_house[9] in params.neecham_houses[params.neecham_house_check_10[0]]):
        params.f.write("\n\t10th lord {} neecham in groom chart".format(params.groom_planet_house[6]))
    if(rc.rahu_house[0] == params.sury_house[0] or rc.sury_house[0] == params.rahu_house[0]):
        params.f.write("\n\tBride and Groom have suryan-rahu overlapping")
    if(rc.rahu_house[0] == params.chan_house[0] or rc.chan_house[0] == params.rahu_house[0]):
        params.f.write("\n\tBride and Groom have chandran-rahu overlapping")
    if(rc.sukr_house[0] == params.ketu_house[0]):
        params.f.write("\n\tBride's ketu overlapping with Groom's sukran")
    if(rc.budh_house[0] == params.chev_house[0] or rc.chev_house[0] == params.budh_house[0]):
        params.f.write("\n\tBudhan and chevvai overlapping")
    


    '''TBD: check chev house distance, index differs based on lagna'''
    # if(abs(rc.chev_index - params.chev_index) == 7):
    #     params.f.write("Bride and Groom have chev at 180 deg")
    # if(abs(rc.chev_index - params.rahu_index) == 7 or abs(rc.rahu_index - params.chev_index) == 7):
    #     params.f.write("Bride and Groom have chev and rahu at 180 deg")
    
    

    


    
