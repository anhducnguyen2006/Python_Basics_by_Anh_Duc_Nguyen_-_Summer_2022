import turtle #importujemy moduł (plik Python) o nazwie turtle.py
#turtle jest modułem, który wykorzystywany jest do rysowania


#aby uruchomić ten program, wciśnij w pasce zadań: run ->
#-> configuration per file -> run file with custom configuration ->
#-> execute in an external system terminal

kursor = turtle.Turtle() #przywołujemy/tworzymy kursor, którym będziemy 
#rysować.
ekran = turtle.Screen() #przywołujemy/tworzymy ekran (biały), na którym
#będziemy rysować.

kursor.color("red","yellow") #kolor "kredki" to czerwony, żółty zatem jest
#wykorzystywany jako wypełnienie funkcji "begin_fill()" i "end_fill()"

kursor.begin_fill() #zaczyna wypełniać obszar kolorem
for _ in range(2): #rysujemy kwadrat
    kursor.forward(50) #rysujemy w górę kreskę
    kursor.right(90) #zmieniamy kąt(skręcamy kredkę) o 90 stopni w prawo
    kursor.fd(50) #drugi sposób pisania "forward()"
    kursor.rt(90) #drugi sposób zmieniania kątu w prawo "right()"
kursor.end_fill() #kończy wypełnianie obszaru

ekran.mainloop() #program się zamknie, gdy zamkniemy okno tego programu