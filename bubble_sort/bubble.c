#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool sort(int numbers[], int length);
void print_array(int array[], int length);

int main(int argc, char **argv)
{
    int total_size = argc - 1;
    int loop_cnt = total_size - 1;
    int sort_array[total_size];

    // printf("%i %i", total_size, loop_cnt);

    for (int i = 0; i < total_size; i++)
    {
        sort_array[i] = atoi(argv[i + 1]);
    }

    // printf("A");
    // print_array(sort_array, total_size);

    while (!sort(sort_array, loop_cnt))
        loop_cnt--;

    // printf("C");
    print_array(sort_array, total_size);

    // printf("\n");
}

bool sort(int numbers[], int length)
{
    int cur_num;
    int next_num;
    bool change = false;

    for (int i = 0; i < length; i++)
    {
        cur_num = numbers[i];
        next_num = numbers[i + 1];

        // printf("    cn %i nn %i    ", cur_num, next_num);

        if (cur_num > next_num)
        {
            // printf("    111cur_index %i 111next_index %i    ", numbers[i], numbers[i + 1]);

            numbers[i] = next_num;
            numbers[i + 1] = cur_num;
            change = true;

            // printf("    cur_index %i next_index %i    ", numbers[i], numbers[i + 1]);
        }

        // printf("B");
        // print_array(numbers, length);
    }

    return change;
}

void print_array(int array[], int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("%i\n", array[i]);
    }
}