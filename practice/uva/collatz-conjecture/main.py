# UVa: The 3n+1 Problem

def collatz(n, iterations):
    if n == 1:
        # total iterations excluding starting number
        return iterations

    iterations += 1

    if n & 1:
        return collatz(3*n + 1, iterations)

    return collatz(n >> 1, iterations)

while True:
    try:
        constraints = [int(n) for n in input().split(" ")]
        ranges = sorted(constraints)
    except Exception:
        break

    iterations = []
    for n in range(ranges[0], ranges[1] + 1):
        iterations.append(collatz(n, 1))
    print(constraints[0], constraints[1], max(iterations))
