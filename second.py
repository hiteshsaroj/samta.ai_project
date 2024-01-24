def gen_fib(n):
    fsequence = [0, 1]
    for i in range(2, n):
        next_term = fsequence[-1] + fsequence[-2]
        fsequence.append(next_term)
    return fsequence
def main():
    n = int(input("enter number : "))
    if n <= 0:
        print("Please enter positive number")
        return
    fibonacci_sequence = gen_fib(n)
    print(fibonacci_sequence)
if __name__ == "__main__":
    main()
