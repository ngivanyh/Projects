#include <stdio.h>
#include <ctype.h>

/* Finds the longest alternating continuous case switching string which alternates every k as an input */
/* eg: 3\nDDaasAAbbCC -> out: 3 (bc of "aas") */

#define CHAR_BUF_MAX 1000000

int find_seq_length(char* str, int starting_index, int alternation);

int main(void)
{
    char str[CHAR_BUF_MAX];
    int alternatation_freq;
    int max_seq_len = 0;

    scanf("%d", &alternatation_freq);
    scanf("%s", str);

    printf("alternatation fequency: %d\ninput string: %s\n", alternatation_freq, str);

    int seq_len;
    for (int i = 0; str[i] != '\0'; i++)
    {
        seq_len = find_seq_length(str, i, alternatation_freq);

        if (seq_len > max_seq_len)
            max_seq_len = seq_len;
    }

    printf("%d\n", max_seq_len);

    return 0;
}

int find_seq_length(char* str, int starting_index, int alternation)
{
    for (int i = starting_index; str[i] != '\0'; i++)
    {

    }

    return 0;
}
