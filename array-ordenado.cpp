#include <iostream>
#include <algorithm> 
using namespace std;

int main() {
    const int TAM = 5; 
    int numeros[TAM];

    cout << "Ingresa " << TAM << " numeros:\n";
    for (int i = 0; i < TAM; i++) {
        cout << "Numero " << i + 1 << ": ";
        cin >> numeros[i];
    }

    sort(numeros, numeros + TAM);

    cout << "\nArray ordenado: ";
    for (int i = 0; i < TAM; i++) {
        cout << numeros[i] << " ";
    }
    cout << endl;

    return 0;
}
