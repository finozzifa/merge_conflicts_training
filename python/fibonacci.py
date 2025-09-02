from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """
    Generate a Fibonacci sequence of length `n`.

    Parameters
    ----------
    n : int
        The number of Fibonacci numbers to generate.

    Returns
    -------
    List[int]
        A list containing the first `n` Fibonacci numbers.
    """
    a: int = 0
    b: int = 1
    next_value: int = b
    count: int = 1
    result: List[int] = []

    while count <= n:
        result.append(next_value)
        count += 1
        a, b = b, next_value
        next_value = a + b

    return result


def main() -> None:
    """
    Main function to generate and print the Fibonacci sequence.
    """
    n: int = 10
    fibonacci_sequence: List[int] = generate_fibonacci(n)
    for num in fibonacci_sequence:
        print(num, end=" ")
    print()


if __name__ == "__main__":
    main()
