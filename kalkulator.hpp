#ifndef INCLUDE_KALKULATOR
#define INCLUDE_KALKULATOR


class Wynik_dzialania{
public:
    Wynik_dzialania(double a = 1, double b = 1, double c = 1);
    void dodawanie();
    void odejmowanie();
    void mnozenie();
    void dzielenie();

private:
    double pierwszy_skladnik;
    double drugi_skladnik;
    double wynik;
};




#endif /* INCLUDE_KALKULATOR */
