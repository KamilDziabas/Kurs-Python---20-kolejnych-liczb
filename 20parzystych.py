print("Podaj liczbę:")
a = int(input())
if a%2 != 0: #gdy użytkownik poda liczbę nieparzystą
    a = a+1
for a in range (a, a + 40, 2):
    print(a)
