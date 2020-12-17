import random
import sys


def new_addition_problem(max_result: int, lowest_number):
    input1 = random.randint(lowest_number, max_result)
    input2 = random.randint(lowest_number, max_result)

    while input1 + input2 > max_result:
        input1 = random.randint(lowest_number, max_result)
        input2 = random.randint(lowest_number, max_result)

    return input1, input2


def new_multiplication_problem(max_result: int, lowest_number):
    input1 = random.randint(lowest_number, max_result)
    input2 = random.randint(lowest_number, max_result)

    while input1 * input2 > max_result:
        input1 = random.randint(lowest_number, max_result)
        input2 = random.randint(lowest_number, max_result)

    return input1, input2


def new_subtraction_problem(max_result: int, lowest_number):
    input1 = random.randint(lowest_number, max_result)
    input2 = random.randint(lowest_number, max_result)

    while input1 - input2 < lowest_number:
        input1 = random.randint(lowest_number, max_result)
        input2 = random.randint(lowest_number, max_result)

    return input1, input2


def new_division_problem(max_result: int, lowest_number):
    input1 = random.randint(lowest_number, max_result)
    input2 = random.randint(lowest_number, max_result)

    while input2 == 0 or input1 == 0 or input1 % input2 > 0 or input1 == input2:
        input1 = random.randint(lowest_number, max_result)
        input2 = random.randint(lowest_number, max_result)

    return input1, input2


def solve_addition(input1: int, input2: int):
    return input1 + input2

def solve_subtraction(input1: int, input2: int):
    return input1 - input2

def solve_multiplication(input1: int, input2: int):
    return input1 * input2

def solve_division(input1: int, input2: int):
    return input1 / input2

def new_random_problem(max_result: int, lowest_number: int):
    global SELECTION
    SELECTION = 'asmd'[random.randint(0,3)]
    return function_types[SELECTION]['generation'](max_result, lowest_number)

def solve_random(input1: int, input2: int):
    global SELECTION
    return function_types[SELECTION]['solution'](input1, input2)

def sign_random():
    global SELECTION
    return function_types[SELECTION]['sign']



function_types = {
    'a': {
        'generation': new_addition_problem,
        'solution': solve_addition,
        'sign': '+'
    },
    's': {
        'generation': new_subtraction_problem,
        'solution': solve_subtraction,
        'sign': '-'
    },
    'm': {
        'generation': new_multiplication_problem,
        'solution': solve_multiplication,
        'sign': '*'
    },
    'd': {
        'generation': new_division_problem,
        'solution': solve_division,
        'sign': '/'
    },
    'r': {
        'generation': new_random_problem,
        'solution': solve_random,
        'sign': '?'
    }
}

math_type = sys.argv[1]
num_questions = int(sys.argv[2])
max_result = int(sys.argv[3])
lowest_number = int(sys.argv[4])

SELECTION = math_type

correct_answers = 0

for i in range(num_questions):
    input1, input2 = function_types[math_type]['generation'](max_result, lowest_number)
    number_provided = False

    while not number_provided:
        print(f'{input1} {function_types[SELECTION]["sign"]} {input2} = ', end="")
        answer = input()

        try:
            solution = function_types[math_type]['solution'](input1, input2)
            correct = solution == int(answer)
            number_provided = True

            if correct:
                print('Correct!\n')
                correct_answers += 1
            else:
                print(f'The correct answer was {solution}\n')

        except:
            print('umm, that wasn\'t a number')

print(f'You scored {(correct_answers/num_questions)*100}%')
