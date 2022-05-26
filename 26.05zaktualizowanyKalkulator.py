import tkinter as tk
import math

symbole = ['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6', '*', 'e', '', '1', '2', '3', '-', '^', '', '0', '.', 'j',
           '+', 'π']

#Pamiec--------
pamiec = []
#--------------

def tworzenieOkna():
    okno = tk.Tk()
    okno.configure(bg='light gray')
    okno.geometry('480x460')
    okno.title('Kalkulator')

    return okno


def tworzenieEkrany(okno):
    ekran = [tk.Label(okno, bg='#C0CBCB', width=68, anchor='w', borderwidth=2) for i in range(3)]

    for i in range(len(ekran)):
        ekran[i].grid(row=i, columnspan=6, ipady=15, ipadx=1)

    return ekran


def tworzeniePolaNaDane(okno, ekran):
    pole_na_dane = tk.Entry(okno, borderwidth=0, highlightcolor='white')
    pole_na_dane.grid(row=len(ekran), columnspan=6, ipadx=180, ipady=10)

    info = tk.Label(okno, bg='white', width=68, anchor='w', borderwidth=2)
    info.grid(row=len(ekran) + 1, columnspan=6, ipady=15, ipadx=1)

    return pole_na_dane, info


def przyciskKlik(pole_na_dane, symbol):
    def f():
        if symbol == '\u21BA':
            cofanie = pole_na_dane.get()[:-1]
            pole_na_dane.delete(0, tk.END)
            pole_na_dane.insert(0, cofanie)
        elif symbol == 'C':
            pole_na_dane.delete(0, tk.END)
        else:
            pole_na_dane.insert(tk.END, symbol)

    return f


def oblicz(pole_na_dane, ekran, info):
    def ostatniZnak(tekst):
        i = 1

        while tekst[-i] == ')':
            i += 1
        if tekst[-i] == "e" or tekst[-i] == "π":
            return True
        return tekst[-i].isdigit()

    def kilkaOperatorow(tekst):
        for i in range(len(tekst)):
            if not tekst[i].isdigit() and not tekst[i + 1].isdigit():
                return True
            return False

    def potenga(tekst):

        for i in range(len(tekst)):
            if tekst[i] == '^':
                tekst = tekst[:i] + '**' + tekst[i + 1:]

        return tekst

    def liczbaPi(tekst):

        for i in range(len(tekst)):
            if tekst[i] == 'π':
                tekst = tekst[:i] + str(math.pi) + tekst[(i + 1):]

        return tekst

    def liczbaEulara(tekst):

        for i in range(len(tekst)):
            if tekst[i] == 'e':
                tekst = tekst[:i] + 'math.e' + tekst[i + 1:]

        return tekst
    def f():
        tekst = pole_na_dane.get()


        if not ostatniZnak(tekst) or kilkaOperatorow(tekst):
            info['text'] = 'Coś poszło nie tak. Spróbuj ponowine'
        else:
            for i in range(1, len(ekran)):
                if ekran[i]['text']:
                    ekran[i - 1]['text'] = ekran[i]['text']
        if '^' in tekst:
            wyrazenie = potenga(tekst)
            ekran[-1]['text'] = tekst + '   =   ' + str(eval(wyrazenie))
            tekst_pamieci = tekst + '   =   ' + str(eval(wyrazenie))       #pamiec
        elif 'π' in tekst:
            wyrazenie = liczbaPi(tekst)
            ekran[-1]['text'] = tekst + '   =   ' + str(eval(wyrazenie))
            tekst_pamieci = tekst + '   =   ' + str(eval(wyrazenie))       #pamiec
        elif 'e' in tekst:
            wyrazenie = liczbaEulara(tekst)
            ekran[-1]['text'] = tekst + '   =   ' + str(eval(wyrazenie))
            tekst_pamieci = tekst + '   =   ' + str(eval(wyrazenie))       #pamiec
        else:
            ekran[-1]['text'] = tekst + '   =   ' + str(eval(tekst))
            tekst_pamieci = tekst + '   =   ' + str(eval(tekst))       #pamiec

        #Pamiec ------------
        if(len(pamiec) < 10):
            pamiec.append(tekst_pamieci)
        else:
            pamiec.pop(0)
            pamiec.append(tekst_pamieci)
        #-----------------

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
            wynik = math.atan(a / b)
        elif (a < 0 and b >= 0):
            wynik = math.atan(a / b) + math.pi
        elif (a < 0 and b < 0):
            wynik = math.atan(a / b) - math.pi
        elif (a == 0 and b > 0):
            wynik = math.pi / 2
        elif (a == 0 and b < 0):
            wynik = - (math.pi / 2)
        else:
            print("TEGO NIE WIE NIKT. POZOSTAWIAMY DO SAMOINTERPRETACJI")

        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i - 1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = 'arg(' + tekst + ')' + ' = ' + str(wynik)

        pole_na_dane.delete(0, 'end')

    return f


def wczytajPoprzedni(pole_na_dane, ekran, okno):
    def f():

        pole_na_dane.delete(0, 'end')
        poprzedni = ekran[-1]['text']
        i = 0
        for el in poprzedni:
            if el != '=':
                pole_na_dane.insert(i, el)
                i += 1
            else:
                break

    return f


def obliczModul(pole_na_dane, ekran):
    def f():

        tekst = pole_na_dane.get()
        a = float(pole_na_dane.get()[-4])
        b = float(pole_na_dane.get()[-2])

        wynik = math.sqrt(a * a + b * b)

        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i - 1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = '\u007C' + tekst + '\u007C' + ' = ' + str(wynik)

        #Pamiec ------------
        if (len(pamiec) < 10):
            pamiec.append('\u007C' + tekst + '\u007C' + ' = ' + str(wynik))
        else:
            pamiec.pop(0)
            pamiec.append('\u007C' + tekst + '\u007C' + ' = ' + str(wynik))
        #-------------------

        pole_na_dane.delete(0, 'end')

    return f


def obliczPierwiastek(pole_na_dane, ekran):
    def f():

        tekst = pole_na_dane.get()
        a = float(pole_na_dane.get()[0:])

        wynik = math.sqrt(a)

        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i - 1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = '√' + tekst + ' = ' + str(wynik)

        pole_na_dane.delete(0, 'end')

        # Pamiec ------------
        if (len(pamiec) < 10):
            pamiec.append('√' + tekst + ' = ' + str(wynik))
        else:
            pamiec.pop(0)
            pamiec.append('√' + tekst + ' = ' + str(wynik))
        # -------------------

    return f


def obliczSilnie(pole_na_dane, ekran):
    def f():
        tekst = pole_na_dane.get()
        a = int(pole_na_dane.get()[0:])
        b = 1
        silnia = 1
        while (b < a + 1):
            silnia *= b
            b += 1
        wynik = silnia
        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i - 1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = tekst + '!' + ' = ' + str(wynik)

        pole_na_dane.delete(0, 'end')

        # Pamiec ------------
        if (len(pamiec) < 10):
            pamiec.append(tekst + '!' + ' = ' + str(wynik))
        else:
            pamiec.pop(0)
            pamiec.append(tekst + '!' + ' = ' + str(wynik))
        # -------------------

    return f


def obliczSinusa(pole_na_dane, ekran):
    def f():
        tekst_pierwotny = pole_na_dane.get()

        tekst = pole_na_dane.get()

        for i in range(len(tekst)):
            if tekst[i] == 'π':
                tekst = tekst[:i] + str(math.pi) + tekst[(i + 1):]

        argument_do_sinusa = eval(tekst)

        wynik = math.sin(argument_do_sinusa)

        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i - 1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = 'sin(' + tekst_pierwotny + ')' + ' = ' + str(wynik)

        pole_na_dane.delete(0, 'end')

        # Pamiec ------------
        if (len(pamiec) < 10):
            pamiec.append('sin(' + tekst_pierwotny + ')' + ' = ' + str(wynik))
        else:
            pamiec.pop(0)
            pamiec.append('sin(' + tekst_pierwotny + ')' + ' = ' + str(wynik))
        # -------------------

    return f


def obliczCosinusa(pole_na_dane, ekran):
    def f():
        tekst_pierwotny = pole_na_dane.get()

        tekst = pole_na_dane.get()

        for i in range(len(tekst)):
            if tekst[i] == 'π':
                tekst = tekst[:i] + str(math.pi) + tekst[(i + 1):]

        argument_do_cosinusa = eval(tekst)

        wynik = math.cos(argument_do_cosinusa)

        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i - 1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = 'cos(' + tekst_pierwotny + ')' + ' = ' + str(wynik)

        pole_na_dane.delete(0, 'end')

        # Pamiec ------------
        if (len(pamiec) < 10):
            pamiec.append('cos(' + tekst_pierwotny + ')' + ' = ' + str(wynik))
        else:
            pamiec.pop(0)
            pamiec.append('cos(' + tekst_pierwotny + ')' + ' = ' + str(wynik))
        # -------------------

    return f


def obliczTangensa(pole_na_dane, ekran):
    def f():
        tekst_pierwotny = pole_na_dane.get()

        tekst = pole_na_dane.get()

        for i in range(len(tekst)):
            if tekst[i] == 'π':
                tekst = tekst[:i] + str(math.pi) + tekst[(i + 1):]

        argument = eval(tekst)

        wynik = math.tan(argument)

        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i - 1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = 'tg(' + tekst_pierwotny + ')' + ' = ' + str(wynik)

        pole_na_dane.delete(0, 'end')

        # Pamiec ------------
        if (len(pamiec) < 10):
            pamiec.append('tg(' + tekst_pierwotny + ')' + ' = ' + str(wynik))
        else:
            pamiec.pop(0)
            pamiec.append('tg(' + tekst_pierwotny + ')' + ' = ' + str(wynik))
        # -------------------

    return f


def obliczArccos(pole_na_dane, ekran):
    def f():
        tekst_pierwotny = pole_na_dane.get()

        tekst = pole_na_dane.get()

        for i in range(len(tekst)):
            if tekst[i] == 'π':
                tekst = tekst[:i] + str(math.pi) + tekst[(i + 1):]

        argument = eval(tekst)

        wynik = math.acos(argument)

        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i - 1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = 'arccos(' + tekst_pierwotny + ')' + ' = ' + str(wynik)

        pole_na_dane.delete(0, 'end')

        # Pamiec ------------
        if (len(pamiec) < 10):
            pamiec.append('arccos(' + tekst_pierwotny + ')' + ' = ' + str(wynik))
        else:
            pamiec.pop(0)
            pamiec.append('arccos(' + tekst_pierwotny + ')' + ' = ' + str(wynik))
        # -------------------

    return f


def obliczArcsin(pole_na_dane, ekran):
    def f():
        tekst_pierwotny = pole_na_dane.get()

        tekst = pole_na_dane.get()

        for i in range(len(tekst)):
            if tekst[i] == 'π':
                tekst = tekst[:i] + str(math.pi) + tekst[(i + 1):]

        argument = eval(tekst)

        wynik = math.asin(argument)

        for i in range(1, len(ekran)):
            if ekran[i]['text']:
                ekran[i - 1]['text'] = ekran[i]['text']
        ekran[-1]['text'] = 'arcsin(' + tekst_pierwotny + ')' + ' = ' + str(wynik)

        pole_na_dane.delete(0, 'end')

        # Pamiec ------------
        if (len(pamiec) < 10):
            pamiec.append('arcsin(' + tekst_pierwotny + ')' + ' = ' + str(wynik))
        else:
            pamiec.pop(0)
            pamiec.append('arcsin(' + tekst_pierwotny + ')' + ' = ' + str(wynik))
        # -------------------

    return f

#Funkcja pamieci -----------------------------
def funkcjaPamieci():

    global okno_pamieci
    okno_pamieci = tk.Tk()
    okno_pamieci.configure(bg='light gray')
    okno_pamieci.geometry('358x550')
    okno_pamieci.title('Pamięć')

    ekrany_pamieci = [tk.Label(okno_pamieci, bg='#C0CBCB', width=50, anchor='w', borderwidth=2) for i in range(10)]
    for i in range(len(ekrany_pamieci)):
        ekrany_pamieci[i].grid(row=i, columnspan=4, ipady=15, ipadx=1)
    kosz = tk.Button(okno_pamieci, text="\U0001F5D1", borderwidth=0, bg='light gray',
                               command=czyszczeniePamieci(ekrany_pamieci))
    kosz.grid(columnspan=4, ipady=5, ipadx=160)

    for i in range(len(pamiec)):
        ekrany_pamieci[len(pamiec) - i - 1]['text'] = pamiec[i]
    if len(pamiec) == 0:
        ekrany_pamieci[0]['text'] = "PAMIĘĆ JEST PUSTA !"

def czyszczeniePamieci(ekrany_pamieci):
    def f():
        pamiec.clear()
        for i in range(10):
            ekrany_pamieci[i]['text'] = ""
    return f
#---------------------------------------------


def tworzeniePrzyciskow(okno, ekran, info):
    przyciski = [tk.Button(okno, text=symbol, borderwidth=0, bg='light gray') for symbol in symbole]

    # Przycisk pamieci --------------
    przycisk_pamiec = tk.Button(okno, text="Pamiec", borderwidth=0, bg='light gray', command=funkcjaPamieci)
    przycisk_pamiec.grid(row=9, column=5, ipady=5, ipadx=30)
    #--------------------------------

    j = len(ekran) + 2
    for i in range(len(przyciski)):
        if i % 6 == 0:
            j += 1
        margines = 60 if len(przyciski) == 1 else 30
        przyciski[i].grid(row=j, column=i % 6, ipady=5, ipadx=margines)
        przyciski[i].configure(command=przyciskKlik(pole_na_dane, przyciski[i]['text']))

    znak_rownosci = tk.Button(okno, text='=', bg='#00BFFF', borderwidth=0, command=oblicz(pole_na_dane, ekran, info))
    znak_rownosci.grid(row=len(ekran) + 8, column=4, columnspan=2, ipady=5, ipadx=60)

    wczytaj_poprzedni = tk.Button(okno, text='\u2B05', command=wczytajPoprzedni(pole_na_dane, ekran, okno))
    wczytaj_poprzedni.grid(row=len(ekran), column=5, ipady=5, ipadx=20)

    znak_argumentu = tk.Button(okno, text='arg(z)', borderwidth=0, bg='light gray',
                               command=obliczArgument(pole_na_dane, ekran))
    znak_argumentu.grid(row=len(ekran) + 8, column=3, ipady=5, ipadx=20)

    znak_modulu = tk.Button(okno, text='\u007C' + 'z' + '\u007C', borderwidth=0, bg='light gray',
                            command=obliczModul(pole_na_dane, ekran))
    znak_modulu.grid(row=len(ekran) + 8, column=2, ipady=5, ipadx=20)

    znak_pierwiastka = tk.Button(okno, text='√', borderwidth=0, bg='light gray',
                                 command=obliczPierwiastek(pole_na_dane, ekran))
    znak_pierwiastka.grid(row=len(ekran) + 5, column=5, ipadx=20)

    znak_silnii = tk.Button(okno, text='!', borderwidth=0, bg='light gray', command=obliczSilnie(pole_na_dane, ekran))
    znak_silnii.grid(row=len(ekran) + 4, column=5, ipadx=20)

    znak_sinusa = tk.Button(okno, text='sin', borderwidth=0, bg='light gray', command=obliczSinusa(pole_na_dane, ekran))
    znak_sinusa.grid(row=len(ekran) + 7, column=0, ipady=5, ipadx=20)

    znak_cosinusa = tk.Button(okno, text='cos', borderwidth=0, bg='light gray',
                              command=obliczCosinusa(pole_na_dane, ekran))
    znak_cosinusa.grid(row=len(ekran) + 7, column=1, ipady=5, ipadx=20)

    znak_tangensa = tk.Button(okno, text='tan', borderwidth=0, bg='light gray',
                              command=obliczTangensa(pole_na_dane, ekran))
    znak_tangensa.grid(row=len(ekran) + 7, column=2, ipady=5, ipadx=20)

    znak_arcsin = tk.Button(okno, text='arcsin', borderwidth=0, bg='light gray',
                            command=obliczArcsin(pole_na_dane, ekran))
    znak_arcsin.grid(row=len(ekran) + 7, column=3, ipady=5, ipadx=20)

    znak_arccos = tk.Button(okno, text='arccos', borderwidth=0, bg='light gray',
                            command=obliczArccos(pole_na_dane, ekran))
    znak_arccos.grid(row=len(ekran) + 7, column=4, ipady=5, ipadx=20)

    return przyciski


if __name__ == '__main__':
    okno = tworzenieOkna()

    ekran = tworzenieEkrany(okno)

    pole_na_dane, info = tworzeniePolaNaDane(okno, ekran)

    przyciski = tworzeniePrzyciskow(okno, ekran, info)

    okno.mainloop()
