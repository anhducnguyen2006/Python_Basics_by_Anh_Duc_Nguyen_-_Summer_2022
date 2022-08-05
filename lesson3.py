# =============================================================================
#                               LISTY
# =============================================================================
#LISTA to zmienna, która może zawierać wiele wartości
#LISTA zawsze oznaczona jest kwadratowymi nawiasami, np. l = [] <- pusta lista

lista = ["jabłko", "gruszka", "brzoskwinia"]
#           0          1             2
#listy również zawierają indeksy

lista[0] = "winogron" #zmiana danej w liście o określonym indeksie
#"jabłko" zamienia się w "winogron"
print(lista)
lista.append("arbuz") #dodawanie danej typu (str) "arbuz" do listy po prawej stronie
lista.insert(1, "ogórek") #dodawanie danej na konkretnej pozycji (indeks)
print(lista)
 
lista.pop(1) #usuwanie danej pod konkretnym indeksem: 1, usuwa nam się ogórek
print(lista)
 
lista.remove("arbuz") #usuwamy arbuza funkcją remove
print(lista)
 
del lista[1] #usuwamy daną pod konkretnym indeksem (inny sposób): 1
print(lista)

lista.pop() #usuwamy ostatnią daną (po prawej stronie) w liście
print(lista)

print(lista) #wydrukuje się cała lista
print(lista[0]) #wydrukuje się element listy znajdujący się na pozycji indeks = 0
print(lista[1]) #wydrukuje się element listy znajdujący się na pozycji indeks = 1
print(lista[2]) #wydrukuje się element listy znajdujący się na pozycji indeks = 2
print(lista[0:2]) #wydrukują się elementy listy znajdujące się na pozycjach indeks = 0:2,
# gdzie element o indeksie 2 się nie liczy
print(lista[-1]) #wydrukuje nam się ostatni element listy
print(lista[-2:-1]) #wydrukuje nam się element na pozycji indeks = -2 (ponieważ -1 się nie liczy)


# =============================================================================
# WYTŁUMACZENIE WBUDOWANEJ FUNKCJI SPLIT Z POPRZEDNIEJ LEKCJI
# =============================================================================
napis = "Hello World"
lista4 = napis.split(' ') #funkcja split sprawia, że 
#napis dzieli się na krótsze napisy, rozdzielone pewnym kryterium w nawiasie,
#w tym wypadku spacją. Nie zapisanie żadnego parametru w funkcji split() powoduje,
#że napis rozdzielony będzie spacją
print(lista4)


#print(lista)
lista2 = [1,2,3]

lista.append(lista2) #dodawanie listy do listy, przypadek "nested lists", czyli lista w liście

print(lista)
print(lista[3][0]) #jak wyjąć daną 1 z przypadku "lista w liście"

lista3 = [4,5,6] #nowa lista

lista3 = lista + lista2 #dodawanie listy do drugiej listy

#lista.extend(lista2)  <- drugi sposób dodawania listy do listy
#print(lista)

lista.sort()#sortujemy listę
#jeśli lista zawiera napisy, sortuje napisy od a do z
#jeśli lista zawiera liczby całkowite, sortuje je od -nieskończoności do nieskończoności
lista.sort(reverse=True)#sortuje listę odwrotnie (od z do a)lub(od nieskończoności do -nieskończoności)

print(lista)

print(len(lista)) #drukujemy długość listy

#1 sposób wydrukowania wszystkich danych w liście pojedynczo
for i in range(len(lista)): 
    print(lista[i])

#2 sposób wydrukowania wszystkich danych w liście pojedynczo
for i in lista:
    print(i)

lista.clear() #czyścimy listę
lista.pop() #usuwamy całą listę
