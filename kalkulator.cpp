#include "kalkulator.hpp"

#include <cmath>

#include <iostream>

Wynik_dzialania::Wynik_dzialania(double a, double b, double c) {
    pierwszy_skladnik = a;
    drugi_skladnik = b;
    wynik = c;
}

void Wynik_dzialania::dodawanie() {
    std::cin >> pierwszy_skladnik;
    std::cout << "+" << " ";
    std::cin >> drugi_skladnik;

    wynik = pierwszy_skladnik + drugi_skladnik;



    std::cout << "= "<< wynik << std::endl;
}

void Wynik_dzialania::odejmowanie() {
    std::cin >> pierwszy_skladnik;
    std::cout << "-" << " ";
    std::cin >> drugi_skladnik;

    wynik = pierwszy_skladnik - drugi_skladnik;



    std::cout << "= "<< wynik << std::endl;
}
