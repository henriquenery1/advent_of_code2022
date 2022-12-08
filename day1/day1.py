def part1():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    current_results = 0
    max_result = 0
    for i in lines:
        if i != '\n':
            current_results += int(i)
        else:
            if current_results > max_result:
                max_result = current_results
            current_results = 0
    return print(max_result)

def part2():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    one, two, three = 0, 0, 0
    current_results = 0
    for i in lines:
        if i != '\n':
            current_results += int(i)
        else:
            if current_results > three:
                if current_results < two:
                    three = current_results
                elif current_results < one:
                    two, three = current_results, two
                else:
                    one, two, three = current_results, one, two
            current_results = 0

    return print(sum([one, two, three]))

part1()
part2()