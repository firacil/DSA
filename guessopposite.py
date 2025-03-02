def guess_opposite(n):
    for i in range(1, 7):
        if (i + n == 7):
            return i
    return "Out of Dice"


if __name__ == "__main__":
    print(guess_opposite(0))