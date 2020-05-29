import random
import time


def selection_sort(list):
    comparisons = 0
    for i in range(len(list)):
        index = i
        for j in range(i + 1, len(list)):
            comparisons += 1
            if list[index] > list[j]:
                index = j
        list[i], list[index] = list[index], list[i]
    return comparisons


def insertion_sort(list):
    comparisons = 0
    for i in range(1, len(list)):

        key = list[i]

        j = i - 1

        while j >= 0:
            comparisons += 1
            if key < list[j]:
                list[j + 1] = list[j]
                j -= 1
            else:
                break
        list[j + 1] = key
    return comparisons


def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time()
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)


if __name__ == '__main__':
    main()
