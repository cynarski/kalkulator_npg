import math

def zadanie(dane, wyniki):
    x = int(dane[0])
    dzialanie = dane[1]
    y = int(dane[2])
    if dzialanie == "+":
        print(x + y)
        wyniki.append(x + y)
    elif dzialanie == "-":
        print(x - y)
        wyniki.append(x - y)
    elif dzialanie == "*":
        print(x * y)
        wyniki.append(x * y)
    elif dzialanie == "/":
        if y == 0:
            print("PAMIĘTAJ CHOLERO, NIE DZIEL PRZEZ ZERO")
        else:
            print(x / y)
            wyniki.append(x / y)
    elif dzialanie == "^":
        print(x ** y)
        wyniki.append(x ** y)
    else:
        print("COŚ ZEPSUŁEŚ")
    return None


def main():
    pamiec = []
    wyniki = []
    while True:
        x = input("PODAJ POLECENIE, NAPISZ STOP ABY ZAKOŃCZYC, PAMIEC ABY SPRAWDZIC PAMIĘĆ: ")
        if x == "STOP":
            print("ZAKOŃCZONO PROGRAM")
            break
        elif x == "PAMIEC":                  # pokazywanie pamieci
            if len(pamiec) < 1:
                print("PAMIEC JEST PUSTA")
                continue
            for i in range(len(pamiec)):
                print(pamiec[i], "=", wyniki[i])
        elif x == "WYCZYSC":
            pamiec.clear()
            wyniki.clear()
        else:
            if len(pamiec) < 2:      # pamiec ostatnich 10 elementow
                pamiec.append(x)
            else:
                pamiec.pop(0)
                pamiec.append(x)
                wyniki.pop(0)
            dane = x.split()
            if dane[0] == "sqrt":                       # pierwiastkowanie
                print(math.sqrt(int(dane[1])))
                wyniki.append(math.sqrt(int(dane[1])))
            else:
                zadanie(dane, wyniki)                         # wykonywanie dzialan

            #print(dane)
    return None


main()
