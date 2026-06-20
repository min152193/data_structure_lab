#pragma once
#include <cstdio>
#include <cstring>

class Car {
protected:
    int speed;
    char name[40];
public:
    int gear;
    Car() {}
    ~Car() {}
    Car(int s, char* n, int g) : speed(s), gear(g) {
        strcpy_s(name, sizeof(name), n);
    }
    void speedUp() { speed += 5; }
    void display() { printf("[%s] : 기어=%d단 속도=%dkmph\n", name, gear, speed); }
};