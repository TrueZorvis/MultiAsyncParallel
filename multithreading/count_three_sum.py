def read_ints(path):
    lst = []
    with open(path, 'r') as f:
        while line := f.readline():
            lst.append(int(line))
    return lst


def count_three_sum(ints, thread_name='t'):
    print(f'started count_three_sum in thread {thread_name}')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found in thread {thread_name}: {ints[i]}, {ints[j]}, {ints[k]}')
    print(f'ended count_three_sum in thread {thread_name}. triplets count: {counter}')
    return counter
