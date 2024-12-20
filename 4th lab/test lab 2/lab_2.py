def weights_equilibrium(weights):

    for i in range(len(weights)):
        left_moment = 0
        right_moment = 0

        for j in range(i):
            left_moment += weights[j] * (i - j)

        for j in range(i + 1, len(weights)):
            right_moment += weights[j] * (j - i)

        if left_moment == right_moment:
            return i

    return -1

def main():
    print(weights_equilibrium([6, 6, 9]))
    print(weights_equilibrium([43, 51, 35, 4]))
    print(weights_equilibrium([19, 25, 5, 42, 38, 8, 34, 16, 14, 8, 47, 42, 4, 20, 23]))
    print(weights_equilibrium([7, 24, 3, 38]))

if __name__ == '__main__':
    main()