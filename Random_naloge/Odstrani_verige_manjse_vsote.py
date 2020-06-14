
def vsota_verige(veriga):
    """Vrne vsoto členov v verigi"""
    vsota = 0
    while veriga != None: #gre čez celo verigo dokler ne pride do konca
        vsota += veriga.podatek  #sešteva vsoto
        veriga = veriga.naslednji #se premikamo po verigi
    return vsota


def odstrani_manjse(vrsta_verig):
    """Odstrani tiste verige vozlov, katere vsota vozlov je nmanjša od vsote vozlov v prejšni verigi"""
    vrsta_verig.vstavi(-1) #damo na konec da bomo vedl kdaj smo pregledal vse verige
    trenutna_vsota = vsota_verige(vrsta_verig.zacetek()) #sm damo vsoto prve verige
    while vrsta_verig.zacetek() != -1: #začnemo gledati od prve verige naprej

        if vsota_verige(vrsta_verig.zacetek()) < trenutna_vsota:

            #če je vsota trenutne verige manjša jo odstranmo iz seznama
            vrsta_verig.odstrani() #samo odstraniš, ker je ne rabiš več

        else:
        
            #Če je vsota večja ali enaka samo nadomestimo trenutno vsoto z naslednjo
            trenutna_vsota = vsota_verige(vrsta_verig.zacetek())
            vrsta_verig.vstavi(vrsta_verig.zacetek()) #premakneš tisto iz začetka na konec
            vrsta_verig.odstrani() #odstraniš iz začetka 
    
    vrsta_verig.odstrani() #odstranimo tega -1 k smo ga porabil da smo vedl če smo vse pogledal
    return vrsta_verig
