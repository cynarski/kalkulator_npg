#include "kalkulator.hpp"
#include <iostream>


int main() {
    char wybrane_dzialanie;
    std::cout << "wybierz dzialanie" << std::endl;
    std::cin >> wybrane_dzialanie;

    if(wybrane_dzialanie == '+'){
        Wynik_dzialania d1(1,1,1);
        d1.dodawanie();
    }
    if(wybrane_dzialanie == '-'){
       

    return EXIT_SUCCESS;
}
