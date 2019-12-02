# Day 2: 1202 Program Alarm


def ops_code(noun = 12, verb =2):
    with open('input1.txt') as file:
        data = file.read()
        program = [int(x) for x in data.split(",")]

        index = 0

        program[1] = noun
        program[2] = verb

        while True:
            operator = int(program[index])
            if operator == 1:
               program[program[index + 3]] = program[program[index + 1]] + program[program[index + 2]]
               index += 4
            elif operator == 2:
               program[program[index + 3]] = program[program[index + 1]] * program[program[index + 2]]
               index += 4
            elif operator == 99:
                break
            else:
                break

        return program

if __name__ == '__main__':
    output1 = new_program = ops_code()

    print("What is value at 0:: " + str(output1[0]))

    for noun in range(0, 100):
        for verb in range(0, 100):
            if ops_code(noun, verb)[0] == 19690720:
                outcome2 = 100 * noun + verb
                print("What is the output: " + str(outcome2))