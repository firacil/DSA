def sum_first(n):
    count = 0
    for i in range(1, n + 1):
        count += i
    print(count)
        


if __name__ == "__main__":
    n = 5
    sum_first(n)