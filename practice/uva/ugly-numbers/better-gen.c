#include <stdio.h>

typedef unsigned long long ullong;

#define GENERATION_TARGET 1500

ullong min(ullong ns[], size_t length);

int main(void)
{
    ullong numbers[GENERATION_TARGET];
    numbers[0] = 1;

    ullong i2 = 0, i3 = 0, i5 = 0;
    for (size_t i = 1; i < GENERATION_TARGET; ++i)
    {
        ullong candidates[3] = {
            numbers[i2] * 2,
            numbers[i3] * 3,
            numbers[i5] * 5
        };

        numbers[i] = min(candidates, 3);

        if (numbers[i] == candidates[0]) ++i2;
        if (numbers[i] == candidates[1]) ++i3;
        if (numbers[i] == candidates[2]) ++i5;
    }

    printf("The %llu'th ugly number is %llu.\n", (ullong) GENERATION_TARGET, numbers[GENERATION_TARGET - 1]);
}

ullong min(ullong ns[], size_t length)
{
    ullong min = ns[0];

    for (size_t i = 1; i < length; ++i)
        if (ns[i] < min)
            min = ns[i];

    return min;
}