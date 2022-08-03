# =============================================================================
# mnożenie napisów (str)
# =============================================================================
a = "Hello"
b = 3
print(a*b)  #HelloHelloHello
print(a+a+a) #HelloHelloHello

# =============================================================================
# operatory matematyczne
# =============================================================================
c = 3
d = 2
print(c+d) #drukuje się 5
print(c-d) #drukuje się 1
print(c*d) #drukuje się 6
print(c/d) #drukuje się 1.5
print(51//2) #drukuje się 25
print(5**2) #drukuje się 25
print(7%3) #drukuje się 1

# =============================================================================
# kolejność czytania kodu, zmiana zmiennej
# =============================================================================
print("przed zmianą")
x = 1
print(x) #drukuje się 1
print("po zmianie")
x += 1 # 1+1
print(x) #drukuje się 2
print("Po odejmowaniu")
x -= 3 
print(x) #drukuje się -1

# =============================================================================
# jak wyjąć/wyrwać część napisu?
# =============================================================================
n = "HelloWorld"
#    0123456789
#-10-9-8-7-6-5-4-3-2-1
print(n[0:5]) #od 0 do 5 (nie wliczając 5), drukuje się: Hello
print(n[:5]) #drukuje się: Hello
print(n[-2]) #drukuje się: l
print(n[-5:-2]) #drukuje się: Wor
print(n[-9:-3]) #drukuje się: elloWo
print(n[2:]) #drukuje się: lloWorld

# =============================================================================
# Wbudowane funkcje napisów (str)
# =============================================================================
m = "Hello World. Nazywam się Andrzej"
print(m.upper()) #drukuje się napis, gdzie wszystkie litery są duże: HELLO WORLD. NAZYWAM SIĘ ANDRZEJ
print(m.lower()) #drukuje się napis, gdzie wszystkie litery są małe: hello world. nazywam się andrzej
print(m.strip()) #funkcja kasuje niepotrzebne spacje z przodu i na końcu napisu
print(len(m)) #drukuje długość napisu: 32
print(m.replace("H","J")) #druguje napis ze zmianą liter: Jello World. Nazywam się Andrzej
print(m.split()) #drukują się pojedyncze słowa rozdzielone spacją
#['Hello', 'World.', 'Nazywam', 'się', 'Andrzej']

# =============================================================================
# ZADANIE
# =============================================================================

# 1) Zmień "Lubię Dizzę" na "LUBIĘ PIZZĘ"
a = "LubięDizzę"
b = a.upper() #LUBIĘ DIZZĘ"
print(b.replace("D", "P"))
print(a.upper().replace("D","P")) #funkcje można powołać po kropce, nie musi być pojedynczo 

# 2) wydrukuj: bięDiz
print(a[2:8])
