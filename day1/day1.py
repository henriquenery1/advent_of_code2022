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

part1()
