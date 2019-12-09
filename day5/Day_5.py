# --- Day 5: Sunny with a Chance of Asteroids ---


def modes(instructions):
    nr_chars = len(instructions)
    if nr_chars == 1 or nr_chars == 2:
        return int(instructions[0]), 0, 0, 0
    if nr_chars == 3:
        return int(instructions[nr_chars - 1]), int(instructions[nr_chars - 3]), 0, 0
    if nr_chars == 4:
        return int(instructions[nr_chars - 1]), int(instructions[nr_chars - 3]), int(instructions[nr_chars - 4]), 0
    if nr_chars == 5:
        return int(instructions[nr_chars - 1]), int(instructions[nr_chars - 3]), int(instructions[nr_chars - 4]), int(instructions[nr_chars - 5])


def value(parameter, program, mode):
    if mode == 0:
        return program[parameter]
    if mode == 1:
        return parameter


def ops_code():
    with open('input1.txt') as file:
        input = 1
        output = 0
        data = file.read()
        program = [int(x) for x in data.split(",")]

        index = 0
        program_length = len(program)
        print(f"What is the program length: {program_length}")

        while program[index] != 99:
            instructions = str(program[index])
            operator, mode1, mode2, mode3 = modes(instructions)

            if operator == 1:
                parameter1 = program[index + 1]
                parameter2 = program[index + 2]
                value1 = value(parameter1, program, mode1)
                value2 = value(parameter2, program, mode2)

                value3 = program[index + 3]

                if mode3 == 0:
                    program[value3] = value1 + value2
                else:
                    program[index + 3] = value1 + value2
                index += 4
            elif operator == 2:
                parameter1 = program[index + 1]
                parameter2 = program[index + 2]

                value1 = value(parameter1, program, mode1)
                value2 = value(parameter2, program, mode2)

                value3 = program[index + 3]
                if mode3 == 0:
                    program[program[index + 3]] = value1 * value2
                else:
                    program[index + 3] = value1 * value2
                index += 4
            elif operator == 3:
                program[program[index + 1]] = input
                index += 2
            elif operator == 4:
                output = program[program[index + 1]]
                index += 2
                print(f"output (1) is {output}")
            elif operator == 99:
                print("Ops 99")
                break
            else:
                print(f"Operator is {operator} and index is {index} ")
                break

        return output


if __name__ == '__main__':
    output1 = ops_code()

    print(f"What is value output:: {output1}")