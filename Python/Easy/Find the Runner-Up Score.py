if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s = set(arr)
    l_sorted = sorted(list(s))
    print(l_sorted[-2])
