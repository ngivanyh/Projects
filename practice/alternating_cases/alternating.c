#include <stdio.h>
#include <string.h>

/* Finds the longest alternating continuous case switching string which alternates every k as an input */
/* eg: 3\nDDaasAAbbCC -> out: 3 (bc of "aas") */

#define CHAR_BUF_MAX 1000000
#define UPPERCASE 1
#define LOWERCASE 0

int find_seq_length(char* str, int starting_index, int alternation);
int case_state(char eval_char);

int main(void)
{
    char str[CHAR_BUF_MAX];
    int alternatation_freq;
    int max_seq_length = 0;

    scanf("%d", &alternatation_freq);
    scanf("%s", str);

    int seq_len;
    for (int i = 0; i < strlen(str); ++i)
    {
        seq_len = find_seq_length(str, i, alternatation_freq);

        if (seq_len > max_seq_length)
            max_seq_length = seq_len;
    }

    printf("%d\n", max_seq_length);

    return 0;
}

int find_seq_length(char* str, int starting_index, int alternation)
{
    int expected_case_state = case_state(str[starting_index]);
    int repeat_amount = 1;
    int total_seq_length = 0;

    int char_case_state;
    for (int i = starting_index + 1; i < strlen(str); ++i)
    {
        char_case_state = case_state(str[i]);

        repeat_amount = repeat_amount % alternation;

        if (repeat_amount == 0)
        {
            total_seq_length += alternation;
            expected_case_state = (expected_case_state) ? LOWERCASE : UPPERCASE;
        }

        if (char_case_state != expected_case_state)
            return total_seq_length;

        repeat_amount++;
    }

    // in case the whole loop doesn't break midway
    if ((repeat_amount % alternation) == 0)
        total_seq_length += alternation;

    return total_seq_length;
}

int case_state(char eval_char)
{
    // rudimentary case checker that expects an english character
    int return_val;

    if ((eval_char >= 'A') && (eval_char <= 'Z'))
        return_val = UPPERCASE;
    else if ((eval_char >= 'a') && (eval_char <= 'z'))
        return_val = LOWERCASE;

    return return_val;
}
