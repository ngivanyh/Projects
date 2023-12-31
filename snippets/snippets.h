typedef struct
{
    char* name;
    char* content;
} snippet;


void add(snippet input);
void delete(snippet input);
void modify(snippet input);
snippet find(char* name);