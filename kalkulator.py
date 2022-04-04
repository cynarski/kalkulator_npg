import math

def zadanie(dane):
    x = int(dane[0])
    dzialanie = dane[1]
    y = int(dane[2])
    if dzialanie == "+":
        print(x + y)
    elif dzialanie == "-":
        print(x - y)
    return None


def main():
    pamiec = []
    while True:
        x = input("PODAJ POLECENIE, NAPISZ STOP ABY ZAKOŃCZYC: ")
        if x == "STOP":
            print("ZAKOŃCZONO PROGRAM")
            break
        else:
            pamiec.append(x)
            dane = x.split()
            zadanie(dane)

            #print(dane)
    return None


main()
