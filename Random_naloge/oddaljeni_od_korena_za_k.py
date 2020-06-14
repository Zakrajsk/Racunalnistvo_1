def oddaljeni_za_k(drevo, k):
    if drevo is None: #če smo pršli do konca za list ne se funckija zakluči
        return
    if k == 0: #če smo na tem nivoju izpišemo podatek
        print(drevo.podatek)
    else:
        #tuki se mormo premaknt v levo in desno poddrevo 
        #nevem točno kako je bla metoda da si pršča v levopoddrevo in desnopoddrevo
        #to morš si pogledat v zapiskih jst sm zaenkrat napisu kr drevo.levopoddrevo() ampak mislm da je mal drgač
        oddaljeni_za_k(drevo.levopoddrevo(), k -1) #se premaknemo v levo poddrevo 
        oddaljeni_za_k(drevo.desnopoddrevo(), k - 1) #se premaknemo v desno poddrevo