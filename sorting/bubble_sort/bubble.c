#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool sort(int numbers[], int length);

int main(int argc, char **argv)
{
    const int total_size = argc - 1;
    const int loop_cnt = total_size - 1;
    int sort_array[total_size];

    for (int i = 0; i < total_size; i++)
    {
        sort_array[i] = atoi(argv[i + 1]);
    }

    while (sort(sort_array, loop_cnt))
        ;

    for (int i = 0; i < total_size; i++)
    {
        printf("%i ", sort_array[i]);
    }

    printf("\n");

    return 0;
}

bool sort(int numbers[], int length)
{
    int cur_num, next_num;
    bool change = false;

    for (int i = 0; i < length; i++)
    {
        if ((cur_num = numbers[i]) > (next_num = numbers[i + 1]))
        {
            numbers[i] = next_num;
            numbers[i + 1] = cur_num;
            change = true;
        }
    }

    return change;
}