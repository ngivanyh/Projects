#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int sort(int numbers[], int length);
bool sorted(int numbers[], int length);
void print_array(int array[], int length);

int main(int argc, char **argv)
{
    int total_size = argc - 1;
    int sort_array[total_size];

    for (int i = 0; i < total_size; i++)
    {
        sort_array[i] = atoi(argv[i + 1]);
    }

    do
    {
        sort(sort_array, total_size);
    }
    while (sorted(sort_array, total_size) == 0);

    print_array(sort_array, total_size);

    printf("\n");
}

int sort(int numbers[], int length)
{
    int cur_num;
    int next_num;

    for (int i = 0; i < length; i++)
    {
        cur_num = numbers[i];
        next_num = numbers[i + 1];

        if (numbers[i] > numbers[i + 1])
        {
            printf("    111cur_index %i 111next_index %i    ", numbers[i], numbers[i + 1]);

            numbers[i] = next_num;
            numbers[i + 1] = cur_num;

            printf("    cur_index %i next_index %i    ", numbers[i], numbers[i + 1]);
        }

        print_array(numbers, length);
    }

    return *numbers;
}

bool sorted(int numbers[], int length)
{
    bool sorted = false;

    for (int i = 0; i < length; i++)
    {
        if (!(numbers[i] <= numbers[i + 1]))
        {
            printf("    not sorted    ");
            return sorted;
        }
    }

    printf("    sorted    ");
    sorted = true;
    return sorted;
}

void print_array(int array[], int length)
{
    for (int j = 0; j < length; j++)
    {
        printf("%i", array[j]);
    }
}