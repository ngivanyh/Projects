// stupid and failed solution

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// less typing with this shortcut
typedef unsigned long ulong;

// unsigned linked list
typedef struct LinkedList {
    ulong value;
    struct LinkedList* prev;
    struct LinkedList* next;
} LinkedList;

// generation amount/goal
#define GENERATION_GOAL 1500

/*
Method of Generation:
Each ugly number is generated using this equation: 2^a * 3^b * 5^c

Check all possible combinations of a, b, and c when a + b + c increases (from 1, 2, and beyond)
 */

int main(void)
{
    // we skip the first ugly number: 1
    ulong generated_numbers = 1;
    ulong exponent_sum = 1;

    // the exponents
    int two_raise;
    int three_raise;
    int five_raise;

    LinkedList UglyNumbers = { 1, NULL, NULL };
    LinkedList* current_ugly_number = &UglyNumbers;

    while (generated_numbers < GENERATION_GOAL)
    {
        for (two_raise = exponent_sum; two_raise >= 0; --two_raise)
        {
            // printf("a: %d\n", two_raise);
            for (three_raise = 0; three_raise <= exponent_sum - two_raise; ++three_raise)
            {
                five_raise = exponent_sum - two_raise - three_raise;
                // printf("b: %d, c: %d\n", three_raise, five_raise);
                LinkedList* ugly_number = malloc(sizeof(LinkedList));

                (*ugly_number).next = NULL;
                (*ugly_number).prev = current_ugly_number;
                (*ugly_number).value = (ulong) pow(2, two_raise) * (ulong) pow(3, three_raise) * (ulong) pow(5, five_raise);

                (*current_ugly_number).next = ugly_number;
                current_ugly_number = ugly_number;

                ++generated_numbers;
            }
        }
        ++exponent_sum;
        // printf("| current status |\na+b+c: %lu, generated: %lu\n", exponent_sum, generated_numbers);
    }

    ulong numbers[generated_numbers];
    for (int i = 0; i < generated_numbers; ++i)
        numbers[i] = 0;

    while ((*current_ugly_number).prev != NULL)
    {
        ulong current_number = (*current_ugly_number).value;

        // insertion sort
        int i;
        for (i = 0; numbers[i] < current_number && i < generated_numbers; ++i)
            ;
        if (numbers[i] != 0)
        {
            numbers[i - 1] = numbers[i];
            numbers[i] = current_number;
        }

        current_ugly_number = (*current_ugly_number).prev;
        free((*current_ugly_number).next);
    }

    for (int i = 0; i <generated_numbers; ++i)
        printf("%lu\n", numbers[i]);

    printf("The 1500'th ugly number is %lu.\n", numbers[1499]);

    return 0;
}