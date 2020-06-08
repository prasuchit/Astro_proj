#!/usr/bin/env python
import os
class chartInit():
    try:
        outpath = 'results'
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        
        # Feeding in bride specific details
        bride_lagna = 'kanya'
        bride_chan = 'meena'
        bride_dasa = 'sukr'
        bride_bukthi = 'chan'
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
        # Ucham houses are diametrically opposite 7th houses

        groom_chart = {}
        groom_lagna_house = []
        groom_planet_house = []
        groom_name = ''
        f = None
        natchatram_response = ''
        groom_lagna = ''
        groom_chan = ''
        lagna_check = ''
        rasi_check = ''
        groom_dasa = ''
        groom_dasa_nathan = ''
        sani_natchatram = ''
        chev_natchatra_athipathi = ''
        rahu_natchatra_athipathi = ''
        ketu_natchatra_athipathi = ''
        sani_natchatra_athipathi = ''
        sury_house = []
        rahu_house = []
        ketu_house = []
        sani_house = []
        chev_house = []
        chan_house = []
        budh_house = []
        sukr_house = []
        guru_house = []
        second_house = []
        sixth_house = []
        seventh_house = []
        eighth_house = []
        twelfth_house = []
        chev_index = []
        sani_index = []
        sury_index = []
        rahu_index = []
        ketu_index = []
        k_house = []
        k_house1 = []
        k_house2 = []
        neecham_house_check = []
        p_house_5 = []
        p_house_7 = []
        p_house_8 = []
        p_house_12 = []

    except Exception as e:
        print("Exception is: ", e)
##################################################################################################################################################################################
