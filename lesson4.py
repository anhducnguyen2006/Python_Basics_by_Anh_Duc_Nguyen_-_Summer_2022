# =============================================================================
# SŁOWNIKI - DICTIONARIES 
# =============================================================================

#słownik jest podobny do listy, ale zamiast 
#indeksów, w słowniku znajdują się klucze.
#Dlatego słownik to nieuporządkowany zbiór
#par klucz-wartość.

#Słownik jest zawsze oznaczony klamrowanymi nawiasami
#   { = shift + [

przykład = {} #pusty słownik

#PODOBIEŃSTWO SŁOWNIKA DO LISTY
lista = ["piórnik", "czerwony", "Topgal", 2022]
#indeks      0          1          2       3

słownik = {
            "przedmiot": "piórnik",
            "kolor": "czerwony",
            "marka": "Topgal",
            "rok": 2022         }

słownik.update({"miejsceProdukcji": "Chiny"})  
#dodawanie nowej pary klucz-wartość
słownik["miejsceProdukcji"] = "Chiny"
#drugi sposób dodawania (niczym się nie różnią)
słownik["kolor"] = "żółty" #zmiana wartości klucza "kolor"
słownik.pop("rok") #usuwanie konkretnej pary klucz-wartość
słownik.popitem() #usuwanie ostatniej pary klucz-wartość


#keys = klucze
x = słownik.keys() #jak wydrukować wszystkie klucze słownika
print(x)

#values = wartości
y = słownik.values() #jak wydrukować wszystkie wartości słownika

#items = elementy
print(słownik.items()) #jak wydrukować wszystkie elementy,
#czyli -> i klucze i wartości słownika
#gdy drukujemy słownik.items(), to uzyskamy list wypełniony
#tuplami, które zawierają klucz i wartość

#TUPLE - ZMIENNA, KTÓRA MOŻE TRZYMAĆ WIELE ELEMENTÓW (podobne do listów)
#nie można zmienić jej elementy
mójTupel = (1,2,3) #<-- oznacza się je normalnymi nawiasami

#DODATKOWE
#jak wydrukować słownik w wsposób klucz wartość
for x, y in słownik.items(): #wytłumaczę pętlę FOR na następnej lekcji
    print(x, y)
    
    
słownik.clear() #wbudowana funkcja, która czyści słownik
del słownik #funkcja del usuwa cały słownik



# =============================================================================
# FUNKCJA JEŻELI - IF
# =============================================================================


#TO SĄ KONDYCJE, KTÓRE NALEŻY WPISAĆ W FUNKCJĘ IF,
#GDY CHCEMY PORÓWNAĆ MINIMUM DWIE ZMIENNE ZE SOBĄ
# =============================================================================
# == #równe
# <= #mniejsze lub równe
# >= #większe lub równe
# != #nie równe
# < #mniejsze
# > #większe
# =============================================================================
#W funkcji jeżeli (if) ZAWSZE po kondycji wpisujemy : i enter,
#wtedy blok kodu będzie się znajdowało o jeden "tab" dalej 
#niż kondycja
#PRZYKŁAD
# =============================================================================
# if kondycja:
#     blok kodu
# =============================================================================
#można zobaczyć, że przed blokiem kodu jest tab, 
#zawsze trzeba wstawić po kondycji taki tab i później wpisać naszą instrukcję (blok kodu)


# Przykład

a = 1

if a > 2: #pierwsza kondycja, "Jeżeli a jest większe niż 2"
    print("Nie prawda") #jednak jest to nie prawda, a więc
    #blok kodu się nie uruchomi
elif x == 1: #druga kondycja, "Jeżeli a równa się 1"
    print("Prawda!") #uruchomi się, ponieważ a równa się 1
else: #elif - w przeciwnym wypadku/ dla pozostałych kondycji
    print("Nie prawda") #została już spełniona kondycja a==1
    #dlatego ten blok kodu się nie uruchomi


#: --> to
#znak ":" używany jest jako most pomiędzy kondycją a blokiem kodu poniżej
#w ten sposób możemy uruchomić ten blok kodu poniżej gdy kondycja zostanie spełniona

#KOLEJNY PRZYKŁAD

x = "HelloWorld"

if x == "HelloWorld": #pierwsza kondycja
    print("Prawidłowa odpowiedź!") #uruchomi się blok kodu,
    #ponieważ została spełniona kondycja
elif x =="World": #resza nie działa, gdyż już została spełniona pierwsza kondycja
    print("Prawie dobrze")
else: 
    print("Błędna odpowiedź")
    

#TYP LOGICZNY BOOL
#możemy powiązać kondycję z typem logicznym BOOL
#typ danej "bool" ma tylko dwie zmienne: True i False (w Pythonie zawsze z dużej litery!)
m = True #true = prawda
n = False #false = fałsz

print(x == "HelloWorld") #<-- wydrukuje się "True", ponieważ kondycja jest prawdą
#zmienna x, którą określiłem wartością "HelloWorld" powyżej równa się "HelloWorld",
#dlatego x == "HelloWorld" jest prawdą, a więc, jest True
print(1>2) #wydrukuje się "False", ponieważ 1 nie jest większe niż 2, a więc, 
#kondycja jest błędna

#Wytłumaczenie
if True: #możemy wpisać 1 == 1 i wyjdzie tak samo, ponieważ 1 równa się 1, a więc, jest prawdą
    print("Prawda!")
else: 
    print("Fałsz!")

#skrócona wersja funkcji IF
p = 1
q = 2
if p < q: print("Prawda") 




# =============================================================================
# ZADANIE
#
# Masz 10 złotych. Napisz kod,który pozwoli ci kupić 
# jabłko i arbuza, które razem kosztują 10 złotych.
# Rozwiąż zadanie w taki sposób, żeby uzystać wartości 
# 7 i 3 przez słownik
# NIE ZMIENIAJ WPISANEGO JUŻ TUTAJ KODU
# =============================================================================

slownik = {"jabłko":7, "banan":5, "arbuz":3}
odpowiedz = None #nic

# =============================================================================
# TUTAJ WPISZ SWÓJ KOD (na dole znajduje się odpowiedź)
# =============================================================================

if odpowiedz == 10:
    print("Prawidłowa odpowiedź!")
else:
    print("Błędna odpowiedź!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#ODPOWIEDŹ:         #7                #3
odpowiedz = slownik["jabłko"]+slownik["arbuz"]


