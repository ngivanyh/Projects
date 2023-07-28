#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool is_num(char **input, int length);

int main(int argc, char **argv)
{
    if (argc < 1 || is_num(argv, argc) == 0)
    {
        printf("Usage: ./bubble num1 num2 num3\n");
    }
    else
    {
        printf("Hello world\n");
    }
}

bool is_num(char **input, int length)
{
    bool is_num = true;

    for (int i = 1; i < length - 1; i++)
    {
        if (atoi(input[1]) == 0)
        {
            break;
            is_num = false;
            return is_num;
        }
    }

    return is_num;
}