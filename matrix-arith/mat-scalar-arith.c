#include <stdio.h>

// int* apply_scalar(int* mat[], int (*apply)(a, b));

// simple calculation functions
int add(int a, int b);
int sub(int a, int b);
int mult(int a, int b);
int div(int a, int b);

int main() {
  int mat[3][2] = { {1, 2}, {3, 4}, {5, 6} };
  int out[3][2];
  
  for (int i = 0; i < 3; i++) {
  	for (int j = 0; j < 2; j++)
    	out[i][j] = add(mat[i][j], 1);
  }
  
  for (int i = 0; i < 3; i++) {
  	for (int j = 0; j < 2; j++)
    	printf("%d", out[i][j]);
  return 0;
}


int add(int a, int b) {
	return a + b;
}


int sub(int a, int b) {
	return a - b;
}


int mult(int a, int b) {
	return a * b;
}


int div(int a, int b) {
	return a / b;
}