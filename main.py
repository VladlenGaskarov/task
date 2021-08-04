import sys


def main():
    arrayInput = [int(i) for i in sys.argv[1:]]
    print(findMaxProduction(arrayInput))


def findMaxProduction(array):
    if len(array) < 3:
        print('недостаточно значений в массиве')
        return
    array.sort()
    result1 = array[0] * array[1] * array[-1]
    result2 = array[-1] * array[-2] * array[-3]
    return max(result1, result2)


if __name__ == '__main__':
    main()
