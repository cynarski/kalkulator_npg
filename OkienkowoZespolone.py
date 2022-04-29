import tkinter as tk
import math

symbole = ['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6', '*', '(',')','1','2','3','-','^2','\u221A','0',',','%','+','','','j','','']


def okienko():
    root = tk.Tk()
    root.title("kalkulatorNPG")
    root.geometry("420x450")

    return root

def ustawieniaEkranu(root):
    ekran = [tk.Label(root, bg='#C0CBCB', text = ' ', width=60, anchor = 'w', borderwidth=2) for i in range(3)]

    for i in range(len(ekran)):
        ekran[i].grid(row = i, columnspan = 6, ipady = 15, ipadx = 1)


    return ekran
    
def PoleNaDane(root, ekran):

    pole_na_dane = tk.Entry(root, borderwidth = 0)
    pole_na_dane.grid(row = len(ekran), columnspan = 6, ipadx = 120, ipady = 10)

    return pole_na_dane

def ustawieniaPrzyciski(root, ekran):
    przyciski = [tk.Button(root, text = symbol) for symbol in symbole]

    j = len(ekran) + 2
    for i in range(len(przyciski)):
        if i % 6 == 0:
            j+=1
        przyciski[i].grid(row = j, column = i % 6, ipady = 5, ipadx = 20)
        przyciski[i].configure(command = PrzyciskKlikniecie(pole_na_dane, przyciski[i]['text']))
    
    znak_rownosci = tk.Button(root, text = '=', command = oblicz(pole_na_dane, ekran))
    znak_rownosci.grid(row = len(ekran) + 6, column = 4, columnspan = 2, ipady = 5, ipadx = 50)
    
    znak_modulu = tk.Button(root, text = '\u007C'+'z'+'\u007C', command = obliczModul(pole_na_dane, ekran))
    znak_modulu.grid(row = len(ekran) + 7, column = 1, ipady = 5, ipadx = 20)


    znak_argumentu = tk.Button(root, text = 'arg(z)', command = obliczArgument(pole_na_dane, ekran))
    znak_argumentu.grid(row = len(ekran) + 7, column = 2, ipady = 5, ipadx = 20)

    wczytaj_poprzedni = tk.Button(root, text = '\u2B05', command = wczytajPoprzedni(pole_na_dane, ekran, root))
    wczytaj_poprzedni.grid(row = len(ekran), column = 4, ipady = 5, ipadx = 20)

    return przyciski


def PrzyciskKlikniecie(pole_na_dane, symbol):
    def f():
        if symbol == '\u21BA':
            bufor = pole_na_dane.get()[:-1]
            pole_na_dane.delete(0, tk.END)
            pole_na_dane.insert(0, bufor)
        elif symbol == 'C':
            pole_na_dane.delete(0, tk.END)
        else:
            pole_na_dane.insert(tk.END, symbol)

    return f

def oblicz(pole_na_dane, ekran):
    def f():

        tekst = pole_na_dane.get()

        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i-1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = tekst + ' = ' + str(eval(tekst))


        pole_na_dane.delete(0, 'end')

    return f


def obliczModul(pole_na_dane, ekran):
    def f():

        tekst = pole_na_dane.get()
        a = float(pole_na_dane.get()[-4])
        b = float(pole_na_dane.get()[-2])

        wynik = math.sqrt(a*a + b*b)

        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i-1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = '\u007C'+tekst + '\u007C' + ' = ' + str(wynik)


        pole_na_dane.delete(0, 'end')


    return f


def obliczArgument(pole_na_dane, ekran):
    def f():

        tekst = pole_na_dane.get()
        a = float(pole_na_dane.get()[-4])
        b = float(pole_na_dane.get()[-2])

        if pole_na_dane.get()[-3] == '-':
            b = -b
        if pole_na_dane.get()[0] == '-':
            a = -a
        
        
        
        if a > 0:
            wynik = math.atan(a/b)
        elif(a < 0 and b >= 0):
            wynik = math.atan(a/b) + math.pi
        elif(a < 0 and b < 0 ):
            wynik = math.atan(a/b) - math.pi
        elif(a == 0 and b > 0):
            wynik = math.pi/2
        elif(a ==0 and b < 0 ):
            wynik = - (math.pi/2)
        else:
            print("TEGO NIE WIE NIKT. POZOSTAWIAMY DO SAMOINTERPRETACJI")


        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i-1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = 'arg('+tekst + ')' + ' = ' + str(wynik)

        pole_na_dane.delete(0, 'end')

    return f


def wczytajPoprzedni(pole_na_dane, ekran, root):
    def f():

        pole_na_dane.delete(0, 'end')
        poprzedni = ekran[-1]['text']
        i=0
        for el in poprzedni:
            if el != '=':
                pole_na_dane.insert(i, el)
                i+=1
            else:
                break

    return f


if __name__ == '__main__':

    root = okienko();

    ekran = ustawieniaEkranu(root)

    pole_na_dane = PoleNaDane(root, ekran)

    przyciski = ustawieniaPrzyciski(root, ekran)

    root.mainloop()
