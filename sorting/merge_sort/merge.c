#include <stdio.h>
#include <stdlib.h>

/*
rough merge sort that has a whole host of problems, improvments:
    - either use pointers to pass the splitted lists to the functions, so only the pointers are passed, no new arrays
    - or use caller free() techniques (i.e. divide() frees former and latter by calling divide() on former and latter separately and then calling merge())
*/

int* divide(int* list, size_t length);
int* merge(int* former, int* latter, size_t former_length, size_t latter_length);

int main(int argc, char *argv[])
{
    const size_t sort_elements = argc - 1;

    int sort_list[sort_elements];

    for (int i = 0; i < sort_elements; ++i)
        sort_list[i] = atoi(argv[i + 1]);

    int* sorted_list = divide(sort_list, sort_elements);

    for (int i = 0; i < sort_elements; ++i)
        printf("%d ", sorted_list[i]);
    printf("\n");

    free(sorted_list);

    return 0;
}

int* divide(int* list, size_t length)
{
    // i don't expect someone would be as stupid as passing NULL but we never know
    if (list == NULL || length == 0)
        return NULL;

    // recursion finished
    if (length == 1)
    {
        int* return_list = malloc(sizeof(int));
        if (return_list == NULL) return NULL;
        return_list[0] = list[0];
        return return_list;
    }

    // will auto floor as the result has to be int
    int split_index = length / 2;

    size_t former_length = split_index;
    size_t latter_length = length - split_index;

    int* former = malloc(sizeof(int) * former_length);
    int* latter = malloc(sizeof(int) * latter_length);

    for (int i = 0; i < former_length; ++i)
        former[i] = list[i];

    for (int i = split_index; i < length; ++i)
        latter[i - split_index] = list[i];

    return merge(divide(former, former_length), divide(latter, latter_length), former_length, latter_length);
}

int* merge(int* former, int* latter, size_t former_length, size_t latter_length)
{
    // i don't expect someone would be as stupid as passing NULL but we never know
    if (former == NULL || latter == NULL)
        return NULL;

    const size_t total_size = former_length + latter_length;
    int* out = malloc(sizeof(int) * (former_length + latter_length)); // times the total length

    if (out == NULL)
        return NULL;

    // merge
    int l1i = 0, l2i = 0;
    while (l1i < former_length && l2i < latter_length)
    {
        if (former[l1i] > latter[l2i])
        {
            out[l1i + l2i] = latter[l2i];
            ++l2i;
        }
        else
        {
            out[l1i + l2i] = former[l1i];
            ++l1i;
        }
    }

    // add back stuff that hasn't been merged
    int* remaining = (l1i != former_length) ? &(former[l1i]) : &(latter[l2i]);
    int* end = (l1i != former_length) ? &(former[former_length - 1]) : &(latter[latter_length - 1]);

    for (int append_start_index = l1i + l2i; remaining <= end; ++remaining, ++append_start_index)
        out[append_start_index] = *remaining;

    // free former and latter (i am sure since by design it should be invoked by divide only)
    free(former);
    free(latter);

    return out;
}