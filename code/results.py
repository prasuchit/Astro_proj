import chart
import doshams as d
import plan_conj as pc
import specialRules as sr

def calcResults():
    try:
        params = chart.chartParams()
        # print(params.neecham_house_check[0])
        # print(params.groom_lagna_house.index(params.house_7[0]))
        # print(params.groom_planet_house[6])
        # print("Hey:", params.neecham_houses[params.neecham_house_check_7[0]])
        params.f.write("\n\n######################################### RESULTS #########################################")
        params.f.write("\nDOSHAM LIST:")

        d.lagRasDasa(params)
        
        d.suryaDosham(params)

        d.saniDosham(params)
        
        d.rahuDosham(params)

        d.ketuDosham(params)

        d.chevDosham(params)

        d.kalatharaDosham(params)
        
        d.punarpuDosham(params)

        d.putraDosham(params)

        pc.planetoryConj(params)

        # sr.horoscopeCompatibility(params)

        params.f.write("\n\n###################################### END OF RESULTS ######################################")
        params.f.close()

    except Exception as e:
	    print("Exception in results.py is: ", e)
        
    return params
