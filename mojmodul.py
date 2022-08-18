# =============================================================================
# TUTAJ ZNAJDUJE SIĘ STWORZONY PRZEZ NAS MODUŁ O NAZWIE modmodul
#(normalny plik Python), KTÓRY MOŻE BYĆ WYKORZYSTANY W INNYCH PLIKACH
# =============================================================================

class OperatoryMatematyczne: #stworzyliśmy klasę o nazwie
# "OperatoryMatematyczne" w tym module
    #w tej klasie znajdują się funkcje (pamiętajcie, że przed podaniem
    #parametrów, trzeba dodać parametr "self", żeby program mógł prawidłowo
    #się uruchomić), które można przywołać w pliku "lekcja8.py"
    def dodawanie(self,m,n): 
        print(m + n)
    def odejmowanie(self,m,n):
        print(m - n)
    def mnozenie(self,m,n):
        print(m * n)
    def dzielenie(self,m,n):
        #dzielenie z wydrukowaną resztą
        print(str(int(m / n))+", reszta "+str(m%n)) 
