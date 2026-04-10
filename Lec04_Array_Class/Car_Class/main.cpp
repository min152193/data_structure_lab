#include "Car.h"
#include <cstdio>

class SportsCar : public Car {
public:
    bool bTurbo;

    //°ª Àü´Þ
    SportsCar(int s, char* n, int g) : Car(s, n, g) { bTurbo = false; }

    void setTurbo(bool bTur) { bTurbo = bTur; }
    void speedUp() {
        if (bTurbo) speed += 20;
        else Car::speedUp();
    }
};

int main() {
    Car normalCar(0, (char*)"¾Æ¹Ý¶¼", 1);
    normalCar.display();
    normalCar.speedUp();
    normalCar.display();

    printf("\n");

    SportsCar mySportsCar(0, (char*)"Å·°«¾ÚÆä·²Æ÷¸£½¦", 1);
    mySportsCar.display();
    mySportsCar.setTurbo(true);
    mySportsCar.speedUp();
    mySportsCar.display();

    return 0;
}