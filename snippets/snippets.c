#include "snippets.h"
#include <stdio.h>
#include <string.h>

void add(snippet input)
{
    FILE *snippet_file = fopen("snippets.txt", "a");

    if (snippet_file == NULL)
    {
        printf("Error occured during fopen.");
        return;
    }

    printf("this is the add func\n");
    fwrite(input.name, input.size_n, 1, snippet_file);
    fwrite(input.content, input.size_c, 1, snippet_file);

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

char* find(char* name);

void get_size(snippet* input)
{
    input->size_n = strlen(input->name);
    input->size_c = strlen(input->content);
}