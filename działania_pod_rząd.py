import math

def zadanie(dane):
    x = int(dane[0])
    dzialanie = dane[1]
    y = int(dane[2])
    if dzialanie == "+":
        return(x + y)
    elif dzialanie == "-":
        return(x - y)

    elif dzialanie == "*":
        return(x * y)
    elif dzialanie == "/":
        if y == 0:
            print("PAMIETAJ CHOLERO, NIE DZIEL PRZEZ ZERO")
        else:
            return(x / y)
    elif dzialanie == "^":
        return(x ** y)


    return None


def main():
    pamiec = []

    while True:
        x = input("PODAJ POLECENIE, NAPISZ STOP ABY ZAKONCZYC: ")
        if x == "STOP":
            print("ZAKONCZONO PROGRAM")
            break
        else:
            pamiec.append(x)
            dane = x.split()
            
            wynik = 0

            while True:
                dzialanie = dane[:3]
                wynik = zadanie(dzialanie)
                
                dane.pop(0)
                dane.pop(0)
                dane[0] = str(wynik)
               
                
                if len(dane) == 1:
                    break

            print(wynik)

    return None


main()
