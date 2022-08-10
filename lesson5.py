# =============================================================================
# PĘTLA FOR 
# =============================================================================

#Pętla FOR to służy w Pythonie do iteracji 
#(powtarzanie tej samej instrukcji z góry 
#określoną liczbę razy lub aż do spełnienia 
#określonego warunku) po sekwencji 
#(np. lista, krotka (tuple), łańcuch string) 
#lub innych iterowanych obiektach (np. słowniki). 

#Przykład:
    
krotka = ("jabłko","ananas","banan")
for elementy in krotka:
    print(elementy)

lista = ["jabłko","ananas","banan"]
for elementy in lista:
    print(elementy)
    
#Funkcja for używa się też, aby uruchomić 
#blok kodu wiele razy. W tym wypadku użyjemy
#fukcji RANGE, czyli "w zasięgu". Funkcja ta
#pozwala uruchomić kod bloku tyle, ile podamy
#w nawiasach tej funkcji. Funkcja RANGE ma
#trzy parametry: range(start, koniec, o_ile?)
#   - start (opcjonalne), czyli jaką wartość początkową musi mieć "i"?
#   - koniec, czyli do kiedy ma uruchomić się blok kodu poniżej
#   - o_ile? (opcjonalne), czyli jak musi się zwiększać liczba "i"

#Przykład:
    
for i in range(0,4,1):
    print("Hello World")

#Tutaj wartość "i" będzie miała początkowo 0.
#Pętla ta ma się powtarzać do kiedy wartość "i"
#będzie większa lub równa 4. 
#Wartość "i" będzie się za każdym razem zwiększać
#o 1, czyli i+=1 za każdym razem.

#można to też zapisać tak:
for i in range(4):
    print(i)
    print("Hello World")
    
#Tak samo zadziała ten blok kodu. 
#dla jasności dodałem print(i), żebyś
#zobaczył(a) jak ta wartość się zmienia
#za każdym razem pętla się uruchamia. 

#Teraz omówimy sobie drugi sposób drukowania
#każdego elementu listy

lista2 = ["jabłko","gruszka","ananas","arbuz"] 
#          0          1        2         3
for i in range(len(lista2)):
    print(lista2[i])
    
#Tutaj i zaczyna się od wartości 0, ponieważ
#parametr "start" funkcji RANGE nie został określony.
#wartość "i" będzie się za każdym razem zwiększać o 1,
#ponieważ również nie został podany ten parametr.
#a więc, dwie lekcje temu wytłumaczyłem Tobie o 
#drukowaniu indeksów np. listy. A więc, ponieważ
#wartość "i" będzie zaczynała od 0 i kończyła na wartości 3 
#(i będzie miała wartości 1,2,3 na tym przykładzie),
#oraz, ponieważ indeksy w liście zaczynają się zawsze od 0,
#można tym sposobem przywołać wszystkie elementy tej listy
#przywołując ich indeksy sposobem lista2[tutaj jest indeks]

#FUNKCJE BREAK I CONTINUE

#break - zaprzestać
#continue - kontynuować

for indeks in range(len(lista)):
    if indeks == 2:
        break #cała pętla zostanie zatrzymana
        #gdy indeks będzie miał wartość 2
    print(indeks)
    print(lista[indeks])
    
for indeks in range(len(lista)):
    if indeks == 2:
        continue #continue powoduje, że gdy
        #indeks będzie miał wartość 2,
        #kod poniżej zostanie ominięty.
        #Następnie wszystko będzie normalnie
        #kontynuować, a więc następny indeks
        #będzie miał wartość 3 i tak dalej...
    print(indeks)
    print(lista[indeks])


# =============================================================================
# PĘTLA WHILE 
# =============================================================================
#Pętla while to polecenie, które służy do wielokrotnego 
#wykonywania bloku instrukcji dotąd, aż warunek 
#zostanie spełniony. Za pomocą tej pętli, 
#można osiągnąć podobne efekty jak za pomocą 
#pętli for, i często stosowane są zamiennie. 

i = 0
while i<4: 
    print(i)
    i+=1 
    
#to samo będzie z pętlą FOR

for i in range(4):
    print(i)
    
    
    
