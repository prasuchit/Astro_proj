def badCombinations(params):
    guru_index = params.groom_lagna_house.index(params.guru_house[0])
    # print(guru_index)
    params.f.write("\nSPECIAL RULES: BAD COMBINATIONS\n")
    if(params.groom_dasa in ['guru', 'budh']):
        params.f.write("Groom dasa is {}\n".format(params.groom_dasa))
    if(params.groom_bukthi in ['guru', 'budh']):
        params.f.write("Groom bukthi is {}\n".format(params.groom_bukthi))
    
