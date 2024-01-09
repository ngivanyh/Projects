#include "snippets.h"

void add(snippet input)
{
    FILE *snippet_file = fopen("snippets.txt", "a");

    if (snippet_file == NULL)
    {
        printf("Error occured during fopen. (Snippet file)");
        return;
    }

    fwrite(input.name, input.size_n, 1, snippet_file);
    fwrite(input.content, input.size_c, 1, snippet_file);

    modify_cnt(1);

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

void modify_cnt(int fluc)
{
    FILE *count_file = fopen("count.txt", "r+");

    if (count_file == NULL)
    {
        printf("Error occured during fopen. (Count file)");
        return;
    }

    int size = 0;
    fseek(count_file, 0L, SEEK_END);
    size = ftell(count_file);
    fseek(count_file, 0L, SEEK_SET);

    if (size == 0)
    {
        char one = '1';
        fwrite(&one, sizeof(char), 1, count_file);
        return;
    }

    char* num;

    for (int i = 0; i < size; i++)
    {
        fread(num, sizeof(char), 1, count_file);
    }

    long rnum = ((long) num) + fluc;

    fwrite((char*) rnum, sizeof(long), 1, count_file);
}