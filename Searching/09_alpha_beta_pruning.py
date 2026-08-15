# Question 9: Alpha-Beta Pruning
# Shakti Raj Devkota

def alpha_beta(values, depth, alpha, beta, maximizing):

    if depth == 0:
        return values[0]

    if maximizing:

        best = float("-inf")

        for i in range(0, len(values), 2):

            value = alpha_beta(
                values[i:i + 2],
                depth - 1,
                alpha,
                beta,
                False
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:

        best = float("inf")

        for i in range(0, len(values), 2):

            value = alpha_beta(
                values[i:i + 2],
                depth - 1,
                alpha,
                beta,
                True
            )

            best = min(best, value)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


# User Input

n = int(input("Enter number of terminal values: "))

values = list(
    map(int, input("Enter values: ").split())
)

if len(values) != n:

    print("Number of values does not match.")

elif n < 2 or (n & (n - 1)) != 0:

    print("Number of values must be a power of 2.")

else:

    depth = n.bit_length() - 1

    result = alpha_beta(
        values,
        depth,
        float("-inf"),
        float("inf"),
        True
    )

    print("Alpha-Beta Value:", result)