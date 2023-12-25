#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <snippets.h>

const int func_cnt = 3;

// Funcitons: add, delete, modify

int main(int argc, char **argv)
{
    if (argc < 3)
    {
        printf("E: Insufficient function arguments.\n");
        return 1;
    }
    
    char *func[] = {"add", "delete", "modify"};

    if (strcmp(argv[1], func[0]) == 0)
    {
        printf("add\n");
    }
    else if (strcmp(argv[1], func[1]) == 0)
    {
        printf("delete\n");
    }
    else if (strcmp(argv[1], func[2]) == 0)
    {
        printf("modify\n");
    }
    else
    {
        printf("E: Not a official function.\n");
    }
    
    
}
