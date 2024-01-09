#include <stdio.h>
#include <string.h>
#include <stdbool.h>

typedef struct
{
    char* name;
    char* content;
    long size_n;
    long size_c;
} snippet;

// snippet file manipulation
void add(snippet input);
void delete(snippet input);
void modify(snippet input);
char* find(char* name);
void get_size(snippet* input);

// count file manipulation
void modify_cnt(int fluc);