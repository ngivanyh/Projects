#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool is_num(char **input, int length);
int sort(int numbers);

int main(int argc, char **argv)
{
    if (argc < 2 || is_num(argv, argc) == 0)
    {
        printf("Usage: ./bubble num1 num2 num3\n");
        return 1;
    }
    else
    {
        int sort_array[argc - 1];

        for (int i = 1; i < argc - 1; i++)
        {
            sort_array[i - 1] = atoi(argv[i]);
        }
        printf("Hello world\n");
    }
}

bool is_num(char **input, int length)
{
    bool is_num = true;

    for (int i = 1; i < length - 1; i++)
    {
        if (atoi(input[i]) == 0)
        {
            break;
            is_num = false;
            return is_num;
        }
    }

    return is_num;
}