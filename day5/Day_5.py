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


def calc(operator, value1, value2):
    return value1 + value2 if operator == 1 else value1 * value2


def ops_code():
    with open('input1.txt') as file:
        # input = 1  --> part 1
        input = 5
        output = 0
        data = file.read()
        program = [int(x) for x in data.split(",")]

        index = 0

        while program[index] != 99:
            instructions = str(program[index])
            operator, mode1, mode2, mode3 = modes(instructions)

            if operator == 1 or operator == 2:
                print("Ops1")
                parameter1 = program[index + 1]
                parameter2 = program[index + 2]
                value1 = value(parameter1, program, mode1)
                value2 = value(parameter2, program, mode2)

                if mode3 == 0:
                    program[program[index + 3]] = calc(operator, value1, value2)
                else:
                    program[index + 3] = calc(operator, value1, value2)
                index += 4
            elif operator == 3:
                print("Ops3")
                program[program[index + 1]] = input
                index += 2
            elif operator == 4:
                print("Ops4")
                output = program[program[index + 1]]
                # index += 2
                print(f"output (1) is {output}")
                break
            elif operator == 5:
                print("Ops5")
                if mode1 == 0 and program[program[index + 1]] != 0:
                    index = program[program[index + 2]] if mode2 == 0 else program[index + 2]
                elif mode1 == 1 and program[index + 1] != 0:
                    index = program[program[index + 2]] if mode2 == 0 else program[index + 2]
                else:
                    index += 3
            elif operator == 6:
                print("Ops6")
                if mode1 == 0 and program[index + 1] == 0:
                    index = program[program[index + 2]] if mode2 == 0 else program[index + 2]
                elif mode1 == 1 and program[index + 1] == 0:
                    index = program[program[index + 2]] if mode2 == 0 else program[index + 2]
                else:
                    index += 3
            elif operator == 7:
                print("Ops7")
                if program[index + 1] < program[index + 2]:
                    program[index + 3] = 1
                else:
                    program[index + 3] = 0
                index += 4
            elif operator == 8:
                print("Ops8")
                if program[index + 1] == program[index + 2]:
                    program[index + 3] = 1
                else:
                    program[index + 3] = 0
                index += 4
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