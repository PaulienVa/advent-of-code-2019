# --- Day 4: Secure Container ---

def nr_correct_password_in_range(range):
    total_valid_passwords = 0
    start_range = range[0]
    end_range = range[1]
    potential_password = start_range
    while potential_password < end_range:
        if is_correct_password(str(potential_password)):
            print('Found correct password ! ' + str(potential_password))
            total_valid_passwords += 1
        potential_password += 1
    return total_valid_passwords


def is_correct_password(input):
    return two_adjacent_number_same(input) and digits_never_decrease(input)


def digits_never_decrease(input):
    i = 0
    while i < len(input) - 1:
        current_char = int(input[i])
        next_char = int(input[i + 1])
        if i < len(input) - 1 and current_char > next_char:
            return False
        i += 1
    return True


def two_adjacent_number_same(input):
    res = {i: input.count(i) for i in set(input)}
    for key in res.keys():
        if res[key] == 2:
            first_index = input.find(key)
            next_index = input.find(key, first_index + 1, len(input))
            return next_index - first_index == 1
    return False


if __name__ == '__main__':
    # digits_never_decrease('134660')
    correct_passwords = nr_correct_password_in_range([134564, 585159])
    print("the number of correct passwords are: " + str(correct_passwords))
