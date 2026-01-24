#include <stdio.h>

int main(void) {
    int mat_a[3][2] = { {1, 2}, {2, 3}, {4, 5} };
    int mat_b[3][2] = { {9, 8}, {7, 6}, {5, 4} };

    int out[3][2];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++)
            out[i][j] = mat_a[i][j] + mat_b[i][j];
    }

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 2; j++)
            printf("%d", out[i][j]);
    return 0;
}