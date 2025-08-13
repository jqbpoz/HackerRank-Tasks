def count_substring(string, sub_string):
    i = string.find(sub_string)
    counter = 0
    while (i != -1):
        counter += 1
        string = string[i + 1:]
        i = string.find(sub_string)
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)