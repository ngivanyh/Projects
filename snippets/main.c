#include <ctype.h>
#include "snippets.h"

const int func_cnt = 3;

bool check_fargs(int argc, int threshold);

// Funcitons: add, delete, modify
// next steps: make an online version with js (node) that also has a database

int main(int argc, char **argv)
{
    if (!check_fargs(argc, 2))
    {
        printf("E: Insufficient function arguments.\n");
        return 1;
    }
    
    if (argc < 2 || argv[1][0] != '-' )
    {
        printf("Nothing to do.\n");
        return 1;
    }

    switch (argv[1][1])
    {
        case 'a':
            printf("add\n");
            check_fargs(argc, 4);

            snippet input;

            input.name = strcat(argv[2], "\n\n");
            input.content = strcat(argv[3],"\n\n");
            get_size(&input);

            printf("%s", input.content);

            add(input);

            break;
        case 'd':
            printf("delete\n");
            break;
        case 'm':
            printf("modify\n");
            break;
        
        default:
            printf("E: Not a function.\n");
            break;
    }
    
}

bool check_fargs(int argc, int threshold)
{
    if (argc < threshold)
    {
        return false;
    }

    return true;
}