import mojmodul as mm #stworzyliśmy sobie moduł (inny plik) o nazwie mojmodul
#tym sposobem możemy ten plik(mojmodul.py) wykorzystać w tym pliku(lekcja8.py)
import numpy as np #importowanie z biblioteki modułu o nazwie numpy
#Numpy to moduł (plik Python), który zawiera zaawansowanie funckje  
#matematyczne oraz wiele innych funkcji (np.numpy.array(), etc.).

#import ... as --> "as" pozwala nam skrócić nazwę modułu dla 
#wygody, gdy odwołujemy się do tego modułu (jak poniżej)

x = mm.OperatoryMatematyczne() #przywołaliśmy sobie klasę (class) o nazwie
#OperatoryMatematyczne(), poprzez stworzenie obiektu o nazwie x.
x.dodawanie(1,2) #w tej klasie, przywołaliśmy sobie funkcje (tutaj dodawanie)
x.odejmowanie(4,3) #tutaj przywołaliśmy funkcję odejmowanie z tej klasy
x.mnozenie(3,3) #...
x.dzielenie(5,2) #...

print(np.add(5,2)) #tutaj przywołaliśmy sobie funkcję znajdującą się w module
#numpy.py (w tym pliku nie ma klas, są tam od razu funkcje) (tutaj, dodawanie)
print(np.subtract(10,8))  #odejmowanie
print(np.ceil(4.2)) #zaokrąglenie liczby do najmniejszej liczby całkowitej,
#która jest większa od tej liczby
print(np.floor(3.6)) #zaokrąglenie liczby do największej liczby całkowitej,
#która jest mniejsza od tej liczby
print(np.round(3.1234)) #zaokrąglenie liczby do liczby całkowitej, znajdującej
#się najbliżej tej liczby
