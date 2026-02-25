#include <stdio.h>

typedef unsigned long long ullong;

#define GENERATION_TARGET 1500

int main(void)
{
    ullong numbers[GENERATION_TARGET];
    numbers[0] = 1;

    ullong candidates[3];
    for (int i = 1; i < GENERATION_TARGET;)
    {

    }

    printf("The 1500'th ugly number is %llu.", numbers[1]);
}