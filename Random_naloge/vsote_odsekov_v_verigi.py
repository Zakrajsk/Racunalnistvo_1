
class Vozel:
    '''Osnovni gradnik verig, narejen "špartansko" '''
    def __init__(self, podatek=None, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji
    
    def __str__(self):
        return str(self.podatek)
    
    def __repr__(self):
        return "Vozel({0}, {1})".format(self.podatek, repr(self.naslednji))


def vsote_odsekov(verizni, k):
    """
    Vrne nov verizni seznam, kjer so v verigi vozlov vsote odsekov k elementov iz veriznega
    """
    nova_veriga = Vozel("Vodilni", None) #Nardis novo verigo v kero bos zapisala rezultat (to je trik da naredis prazno verigo) tkole na koncu samo vrneš nova_veriga.naslendji
    pozicija_nove = nova_veriga #S tem se boš premikala po novi verigi da boš na konec dala taprav vozel (lahko bi bila tudi metoda pri razredu)
    stevec = 0 #steješ do K ja da potem zapišeš vsoto
    vsota = 0
    while verizni is not None: #greš čez vse vozle
        vsota += verizni.podatek 

        if stevec < k: #ce se niso trije samo povečaš števec in greš naprej
            stevec += 1

        else: #ce je ze tok vozlov kokr je k boš vsoto zapisala v vozel in jo pripela novi verigi
            pozicija_nove.naslednji = (Vozel(vsota, None))
            pozicija_nove = pozicija_nove.naslednji
            stevec = 0
            vsota = 0
        verizni = verizni.naslednji #premikanje po osnovni verigi
    
    if stevec != 0: # v primeru da se ne konča lepo sepravi da je st_vozlev % k != 0 morš še zadnjo vsoto nakdadno prište
        pozicija_nove.naslednji = (Vozel(vsota, None))
    return nova_veriga.naslednji #vrneš naslednji zato da izpustiš tistega "vodilnega" ki si ga naredila na začetku


def izpisi_vse_vozle(verizni): #funkcija samo za testirat 
    """
    Izpise vse vozle v veriznem seznamu
    """
    while verizni is not None:
        print(verizni.podatek)
        verizni = verizni.naslednji

#to je naloga iz besedila
testni = Vozel(0, Vozel(5, Vozel(3, Vozel(-1, Vozel(0, Vozel(-3, Vozel(2, Vozel(4, Vozel(3, Vozel(-2, Vozel(1, None)))))))))))


rezultat = vsote_odsekov(testni, 2)
izpisi_vse_vozle(rezultat)