// "extra points" C version, but why not
#include <stdio.h>

int collatz(int n, int iterations);

int main(void)
{
    int constraints[2], ranges[2];
    while (1)
    {
        // scanf will return the values scanned
        if (scanf("%d %d", constraints, constraints + 1) != 2) break;

        ranges[0] = constraints[0];
        ranges[1] = constraints[1];

        if (ranges[0] > ranges[1])
        {
            // swap & sort
            ranges[0] ^= ranges[1];
            ranges[1] ^= ranges[0];
            ranges[0] ^= ranges[1];
        }

        int iterations = 0, most_iterations = 0;
        for (int i = ranges[0]; i <= ranges[1]; ++i)
        {
            iterations = collatz(i, 1);

            if (iterations > most_iterations)
                most_iterations = iterations;
        }

        printf("%d %d %d\n", constraints[0], constraints[1], most_iterations);
    }
}

int collatz(int n, int iterations)
{
    if (n == 1)
        return iterations;

    ++iterations;

    if (n & 1)
        return collatz(3*n + 1, iterations);

    return collatz(n / 2, iterations);
}