#pragma once
#define _CRT_SECURE_NO_WARNINGS //라인 21 오류떄문에 넣었습니다
#define MAX_DEGREE 80
#include <cstdio>
#include <cstring>

class Polynomial {
	int degree;
	float coef[MAX_DEGREE];
public:
	Polynomial() { degree = 0; }
	// 멤버함수
	void read() {
		printf("다항식의 최고 차수를 입력하시오: ");
		scanf("%d", &degree);
		printf("각 항의 계수를 입력하시오 (총 %d개): ", degree + 1);
		for (int i = 0; i <= degree; i++)
			scanf("%f", coef + i);
	}
	// 내용출력
	void display(const char* str = " Poly = ") {
		printf("\t%s", str);
		for (int i = 0; i < degree; i++)
			printf("%5.1f x^%d + ", coef[i], degree - i);
		printf("%4.1f\n", coef[degree]);
	}
	void add(Polynomial a, Polynomial b) {
		degree = (a.degree > b.degree) ? a.degree : b.degree;
		for (int i = 0; i <= degree; i++)
			coef[i] = 0;
		for (int i = 0; i <= a.degree; i++)
			coef[i + (degree - a.degree)] += a.coef[i];
		for (int i = 0; i <= b.degree; i++)
			coef[i + (degree - b.degree)] += b.coef[i];
	}
};