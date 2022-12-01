#include <iostream>

int main()
{
    int number1, number2;
    int suma, resta, multiplicacion, division, modulo;
    bool comparing;

    std::cout << "Ingrese un numero: ";
    std::cin >> number1;

    std::cout << "Ingrese otro numero: ";
    std::cin >> number2;

    // Operaciones aritmeticas.
    std::cout << "\nOperaciones aritmeticas"
              << "\n";
    suma = number1 + number2;
    std::cout << "El resultado de la suma es: " << suma << "\n";

    resta = number1 = number2;
    std::cout << "El resultado de la resta es: " << resta << "\n";

    multiplicacion = number1 * number2;
    std::cout << "El resultado de la multiplicacion es: " << multiplicacion << "\n";

    division = number1 / number2;
    std::cout << "El resultado de la division es: " << division << "\n";

    modulo = number1 % number2;
    std::cout << "El resultado del sobrante es: " << modulo << "\n";

    // Operacion logica en condicional.
    std::cout << "Operacion logica en condicional"
              << "\n";
    if (number1 > number2)
    {
        std::cout << "El primer numero ingresado es mayor al segundo";
    }
    else
    {
        std::cout << "El segundo numero ingresado es mayor al primero";
    }

    // Operacion logica
    std::cout << "\nOperadores logicos"
              << "\n";
    comparing = (suma > number2 && division < suma);
    std::cout << "La operacion logica resulto en: " << comparing << "\n";
    comparing = (modulo < suma || suma > multiplicacion);
    std::cout << "La operacion logica resulto en: " << comparing << "\n";
    comparing = !(modulo < suma || suma > multiplicacion);
    std::cout << "La operacion logica resulto en: " << comparing << "\n";
    return 0;
}