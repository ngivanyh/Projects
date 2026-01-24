#include <stdio.h>

int main()
{
    printf("%d", EOF);
    int rows = 2;
    int cols = 3;
    int mat[2][3] = { 1,2,3,4,5,6 };
    
    int trans_mat[cols][rows];
    
    for (int i = 0; i < cols; ++i) {
      for (int j = 0; j < rows; j++) {
        printf("i: %d j: %d mat: %d\n", i , j, mat[j][i]);
        trans_mat[i][j] = mat[j][i];
      }
    }
    
    for (int i = 0; i < cols; ++i) {
      for (int j = 0; j < rows; j++) {
        printf("%d ", trans_mat[i][j]);
      }
      printf("\n");
      
    }
    // printf()
    return 0;
}