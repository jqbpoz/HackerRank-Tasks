def swap_case(s):
    l = [char.lower() if char != char.lower() else char.upper() for char in list(s)]
    return "".join(l)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)