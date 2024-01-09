typedef struct
{
    char* name;
    char* content;
    long size_n;
    long size_c;
} snippet;


void add(snippet input);
void delete(snippet input);
void modify(snippet input);
char* find(char* name);
void get_size(snippet* input);