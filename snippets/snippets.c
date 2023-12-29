#include "snippets.h"
#include <stdio.h>
#include <string.h>

void add(snippet snippet)
{
    FILE *snippet_file = fopen("snippets.txt", "w");

    if (snippet_file == NULL)
    {
        printf("Error occured during fopen.");
        return;
    }

    fwrite(snippet.content, strlen(snippet.content), 1, snippet_file);
}

void del(snippet snippet)
{
    return;
}

void modify(snippet snippet)
{
    return;
}

snippet find(char* name);