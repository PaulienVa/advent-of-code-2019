# Day 1: The Tyranny of the Rocket Equation

def simple_requirements():
    with open('input1.txt') as file:
        sum = 0
        for line in file:
            sum += rocket_fuel(line)
    file.close()
    return sum

def iterative_requirements():
    with open('input1.txt') as file:
        sum = 0
        for line in file:
            print("what is the line " + line)
            sum += recursive_rocket_fuel(line, 0)
        file.close()
        return sum

def recursive_rocket_fuel(fuel, sum):
    rest_fuel = rocket_fuel(fuel)
    if rest_fuel == 0 or rest_fuel < 0:
        return sum
    else:
        sum += rest_fuel
        return recursive_rocket_fuel(rest_fuel, sum)

def rocket_fuel(line) :
    module = int(line)
    return int(module / 3) - 2

if __name__ == '__main__':
    fuel_req = iterative_requirements()
    print("The sum is " + str(fuel_req))




