import tkinter as tk
import math


def wykonaj_dzialanie():
    pamiec = []
    wyniki = []
    x = pole_na_dzialanie.get()


    if x == "STOP":
            wyswietlanie.config(text="ZAKONCZONO PROGRAM")
    elif x == "PAMIEC":                  
        if len(pamiec) < 1:
            wyswietlanie.config(text="PAMIEC JEST PUSTA")      
        for i in range(len(pamiec)):
            wyswietlanie.config(text=pamiec[i] + "=" + wyniki[i])       
    elif x == "WYCZYSC":
        pamiec.clear()
        wyniki.clear()
    else:
        if len(pamiec) < 2:
            pamiec.append(x)
        else:
            pamiec.pop(0)
            pamiec.append(x)
            wyniki.pop(0)
        dane = x.split()
        if dane[0] == "sqrt":                       
            wyswietlanie.config(text= str(math.sqrt(int(dane[1]))) )  
            wyniki.append(math.sqrt(int(dane[1])))
        else:
            dane = x.split()
            a = int(dane[0])
            dzialanie = dane[1]
            b = int(dane[2])


            if dzialanie == "+":
                wyswietlanie.config(text=str(a+b))
                wyniki.append(a + b)
            elif dzialanie == "-":
                wyswietlanie.config(text=str(a-b))
                wyniki.append(a - b)
            elif dzialanie == "*":
                wyswietlanie.config(text=str(a*b))
                wyniki.append(a * b)
            elif dzialanie == "/":
                if b == 0:
                    wyswietlanie.config(text=" PAMIETAJ CHOLERO, NIE DZIEL PRZEZ ZERO")
                else:
                    wyswietlanie.config(text=str(a/b))
                    wyniki.append(a / b)
            elif dzialanie == "^":
                wyswietlanie.config(text=str(a**b))
                wyniki.append(a ** b)
            else:
                wyswietlanie.config(text="COS ZEPSULES")





    




root = tk.Tk()
root.title("kalkulatorNPG")
root.geometry("600x400")


pole_na_dzialanie = tk.Entry(root, width=40)            
pole_na_dzialanie.pack()            

przycisk = tk.Button(root, text="Oblicz", font=40, width=10, command=lambda: wykonaj_dzialanie())        
przycisk.pack()

wyswietlanie = tk.Label(width = 100, height = 50, text="tekst")
wyswietlanie.pack()     







root.mainloop()
