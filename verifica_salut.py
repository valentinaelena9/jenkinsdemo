date_asteptate = "Salut din jenkinsdemo si Python"
date_primite = input()
print("Verifica Salut: primit:", date_primite)
try: 
    assert(date_asteptate == date_primite)
    print("SUCCES")
except AssertionError as e:
    #interceptam eroarea si dam un mesaj
    print("EROARE")
    print("asteptat:", date_asteptate)
    print("primit:  ", date_primite)
    #reridicam eroarea pentru a face programul sa cada cu eroare
    raise(e)
