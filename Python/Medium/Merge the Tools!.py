def merge_the_tools(string, k):

    words = [string[i:i + k] for i in range(0, len(string), k)]
    results = []

    for word in words:
        l_result = []
        for char in word:
            if char not in l_result:
                l_result.append(char)
        results.append("".join(l_result))
    [print(r) for r in results]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)