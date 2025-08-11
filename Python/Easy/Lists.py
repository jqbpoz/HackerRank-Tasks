if __name__ == '__main__':
    N = int(input())
    # results = list(range(N))
    results = []
    instructions = []

    for _ in range(N):
        instruction = input()
        l = instruction.strip().split(" ")
        instructions.append(l)


    def execute(ins):
        global results
        match ins[0]:
            case 'insert':
                results.insert(int(ins[1]), int(ins[2]))
            case 'print':
                print(results)
            case 'remove':
                results.remove(int(ins[1]))
            case 'append':
                results.append(int(ins[1]))
            case 'sort':
                results.sort()
            case 'pop':
                results.pop()
            case 'reverse':
                results = results[::-1]
        # print(f"res{results}")

for ins in instructions:
    execute(ins)