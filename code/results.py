import chart
import doshams as d
import plan_conj as pc
import specialRules as sr

def calcResults():
    try:
        params = chart.chartParams()
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

        # sr.badCombinations(params)

        params.f.write("\n\n###################################### END OF RESULTS ######################################")
        params.f.close()

    except Exception as e:
	    print("Exception is: ", e)
        
    return params
