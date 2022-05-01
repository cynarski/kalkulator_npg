import tkinter as tk
import math

symbole = ['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6', '*', '(',')','1','2','3','-','^2','√','0',',','π','+']

def tworzenieOkna():

    okno = tk.Tk()
    okno.configure(bg = 'light gray')
    okno.geometry('480x400')
    okno.title('Kalkulator')

    return okno

def tworzenieEkrany(okno):

    ekran = [tk.Label(okno, bg= '#C0CBCB', width=68, anchor='w' , borderwidth= 2) for i in range(3)]

    for i in range(len(ekran)):
        ekran[i].grid(row= i , columnspan= 6, ipady= 15 , ipadx=1)

    return ekran

def tworzeniePolaNaDane(okno,ekran):

    pole_na_dane = tk.Entry(okno, borderwidth= 0,highlightcolor='white')
    pole_na_dane.grid(row=len(ekran) , columnspan=6, ipadx= 180, ipady=10)

    info = tk.Label(okno, bg='white',  width=68, anchor='w', borderwidth=2)
    info.grid(row= len(ekran) + 1 , columnspan= 6, ipady= 15 , ipadx=1)

    return pole_na_dane , info

def przyciskKlik(pole_na_dane,symbol):
    def f():
        if symbol =='\u21BA':
            cofanie = pole_na_dane.get()[:-1]
            pole_na_dane.delete(0,tk.END)
            pole_na_dane.insert(0,cofanie)
        elif symbol == 'C':
            pole_na_dane.delete(0, tk.END)
        else:
            pole_na_dane.insert(tk.END,symbol)

    return f



def tworzeniePrzyciskow(okno, ekran,info):
    przyciski = [tk.Button(okno, text=symbol,borderwidth=0,bg = 'light gray') for symbol in symbole]

    j = len(ekran) + 2
    for i in range(len(przyciski)):
        if i % 6 == 0:
            j += 1
        margines = 60 if len(przyciski) == 1 else 30
        przyciski[i].grid(row = j, column= i% 6, ipady= 5 , ipadx= margines)
        przyciski[i].configure(command= przyciskKlik(pole_na_dane,przyciski[i]['text']))

    znak_rownosci = tk.Button(okno, text= '=' , bg = '#00BFFF', borderwidth= 0,command = oblicz(pole_na_dane,ekran,info) )

    znak_rownosci.grid(row = len(ekran) + 6, column= 4,columnspan= 2, ipady= 5 , ipadx= 60)

    return przyciski

def oblicz(pole_na_dane,ekran,info):

    def ostatniZnak(tekst):
        i = 1

        while tekst[-i] == ')':
            i += 1
        return tekst[-i].isdigit()

    def kilkaOperatorow(tekst):
        for i in range(len(tekst)):
            if not tekst[i].isdigit() and not tekst[i + 1].isdigit():
                return True
            return False
    def potenga(tekst):

        for i in range(len(tekst)):
            if tekst[i] == '^':
                tekst = tekst[:i] + '**' + tekst[i + 1 :]

        return tekst

    def pierwiastek(tekst):
        for i in range(len(tekst)):
            if  tekst[i] == '√':
                return math.sqrt()

    def f():
        tekst=pole_na_dane.get()

        if not ostatniZnak(tekst) or kilkaOperatorow(tekst):
            info['text'] = 'Coś poszło nie tak. Spróbuj ponowine'
        else:
            for i in range(1 , len(ekran)):
                if ekran[i]['text']:
                    ekran[i - 1]['text'] = ekran[i]['text']
        if '^' in tekst:
            wyrazenie = potenga(tekst)
            ekran[-1]['text'] = tekst + '   =   ' + str(eval(wyrazenie))
        elif '√' in tekst:
            wyrazenie = pierwiastek(tekst)
            
        else:
            ekran[-1]['text'] = tekst + '   =   ' + str(eval(tekst))

    return f

if __name__ == '__main__':


    okno = tworzenieOkna()

    ekran = tworzenieEkrany(okno)

    pole_na_dane , info = tworzeniePolaNaDane(okno,ekran)

    przyciski = tworzeniePrzyciskow(okno,ekran,info)

    okno.mainloop()



