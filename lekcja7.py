# =============================================================================
# KLASY I OBIEKTY
# =============================================================================
#Obiekty są połączeniem zmiennych i funkcji w jedną 
#strukturalną całość. Obiekty biorą swoje zmienne i funkcje z klas. 
#Klasy są podstawowym schematem, według których tworzone są obiekty.

class Telefon:
    def robienie_zdjęć(self):
        print("Robię zdjęcia")

mójObiekt = Telefon() #jeśli chcemy uruchomić funkcję "robienie_zdjęć"
#musimy "włączyć" telefon poprzez przypisanie tej klasy do pewnego
#obiektu
mójObiekt.robienie_zdjęć() #wtedy, w ten sam sposób jak 
#wbudowane funkcje napisów czy listów, możemy przywołać tą funkcję. 

#ITERATORY - obiekty, które zawierają indeksy

napis = "HelloWorld"
#indeks: 0123456789

lista = [1,2,3]
#indeks: 0,1,2

mójtuple = (1,2,3)
#indeks:    0,1,2


#proces iteracji
for i in napis:
    print(i)
    
for j in lista:
    print(j)

for k in lista:
    print(k)

#ITERACJA DLA SŁOWNIKÓW
slownik = {
            "klucz":"wartość",
            "dom":"czerwony"     
                                 }
#MOŻNA POMYŚLEĆ O SŁOWNIKU JAKO LISTA, KTÓRA ZAWIERA DWIE LISTY W SOBIE,
#PIERWSZA: WSZYSTKIE KLUCZE, DRUGA LISTA: WSZYSTKIE WARTOŚCI
# =============================================================================
# lista1 = [
#             ["klucz","dom"],
#             ["wartość","czerwony"]
#                                     ]
# =============================================================================

for s in slownik.keys(): #iterowanie przez wszystkie klucze
    print(s)
for a in slownik.values(): #iterowanie przez wszystkie wartości
    print(a)
    
for q,p in slownik.items(): #iterowanie przez wszystkie pary klucz-wartość
    print(q,p)
    
#ZASIĘG
x = 1 #zmienna globalna
def robienie_zdjęć():
    global x #bez tego wyskoczy błąd, ponieważ, wartość x, nie została
    #określona w środku zasięgu lokalnego (w tym przypadku, w funkcji)
    #poprzez wpisanie "global (zmienna, tutaj x)", program zwróci
    #uwagę również na zmienne znajdujące się w zasięgu globalnym
    print(x)
    x = 2 #zmieniamy wartość zmiennej globalnej
    
robienie_zdjęć()
print(x) #tutaj x już będzie miał wartość 2, bo przywołaliśmy
#sobie funkcję robienie_zdjęć(), która zmienia wartość x na 2
    
    
    
#INPUT - służy do wprowadzania zmiennych przez użytkownika programu. 
    
t = input("Jak się nazywasz?: ") #wpiszę słowo Andrzej, następnie 
#wcisnę ENTER
#wtedy x będzie miał wartość "Andrzej"
#--> x = "Andrzej"
print("Cześć "+ t) #gdy mamy tą wartość, możemy ją wykorzystywać
#w naszym programie, np. poprzez wydrukowanie komunikatu "Cześć Andrzej"
y = input("Twoje ulubione jedzienie:") #tak samo
print("Lubisz "+y) #output
ile_lat = int(input("Ile masz lat?: ")) #gdy przypisujemy wartość
#do zmiennej "ile_lat", typ tej wartości to str, czyli napis.
#dlatego gdy chcemy zmienić typ tej zmiennej w np.liczbę całkowitą,
#użyjemy funkcji int(),

for i in range(ile_lat): #drukuje się od 0-15
    print(i)
    