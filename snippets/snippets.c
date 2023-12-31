#include "snippets.h"
#include <stdio.h>
#include <string.h>

void add(snippet input)
{
    FILE *snippet_file = fopen("snippets.txt", "w");

    if (snippet_file == NULL)
    {
        printf("Error occured during fopen.");
        return;
    }

    int sizes_1 = strlen(input.name);
    int sizes_2 = strlen(input.content);

    printf("this is the add func\n");
    fwrite(input.name, sizes_1, 1, snippet_file);
    fwrite(input.content, sizes_2, 1, snippet_file);

    fclose(snippet_file);
}

void del(snippet input)
{
    return;
}

void modify(snippet input)
{
    return;
}

snippet find(char* name);