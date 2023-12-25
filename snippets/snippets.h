typedef struct
{
    char* name;
    char* content;
} snippet;


void add(snippet snippet);
void delete(snippet snippet);
void modify(snippet snippet);
snippet find(char* name);