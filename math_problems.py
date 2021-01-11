#!/bin/env python3

import random
import sys
import logging
import json

class MathProblems:
    _assigned_problems = []
    _problem_type = 'r'
    _num_questions = 0
    _max_result = 0
    _lowest_number = 0
    current_problem = -1

    def __init__(self,
                 problem_type: str = 'r',
                 num_questions: int = 10,
                 max_result: int = 100,
                 lowest_number: int = 0):

        self._function_types = {
            'a': {
                'generation': self._new_addition_problem,
                'sign': '+'
            },
            's': {
                'generation': self._new_subtraction_problem,
                'sign': '-'
            },
            'm': {
                'generation': self._new_multiplication_problem,
                'sign': '×'
            },
            'd': {
                'generation': self._new_division_problem,
                'sign': '÷'
            },
            'r': {
                'generation': self._new_random_problem,
                'sign': '?'
            }
        }
        self._problem_type = problem_type
        self._num_questions = num_questions
        self._max_result = max_result
        self._lowest_number = lowest_number
        self._assign_problems()


    def get_problem(self, problem_index: int = None) -> str:
        if not problem_index:
            problem_index = self.current_problem

        num_pad = len(str(self._max_result))
        input1 = str(self._assigned_problems[problem_index]['input1'])
        input2 = str(self._assigned_problems[problem_index]['input2'])
        sign = self._function_types[self._assigned_problems[problem_index]['type']]['sign']
        return '\n'.join((f'{input1.rjust(num_pad + 3, " ")}',
                f' {sign} {input2.rjust(num_pad, " ")}',
                '   '.ljust(num_pad + 3, '-')))


    def next_problem(self) -> str:
        if self.current_problem < self._num_questions - 1:
            self.current_problem += 1
            return self.get_problem()


    def test_answer(self, answer: int) -> bool:
        self._assigned_problems[self.current_problem]['answer_given'].append(answer)
        self._assigned_problems[self.current_problem]['attempts'] += 1

        if answer == self._assigned_problems[self.current_problem]['answer']:
            logging.debug("Correct")
            self._assigned_problems[self.current_problem]['solved'] = True
            return True

        logging.debug("wrong")
        return False


    def get_current_score(self) -> float:
        correct = len([correct for correct in self._assigned_problems if correct['solved']])
        return correct / self._num_questions


    def get_attempts_score(self) -> float:
        correct = len([correct for correct in self._assigned_problems if correct['solved']])
        attempts = self.get_attempts()
        return correct / attempts


    def get_attempts(self) -> int:
        return sum([problem['attempts'] for problem in self._assigned_problems])


    def _assign_problems(self):
        print("hello")
        for i in range(self._num_questions):
            new_problem = {}
            self.SELECTION = self._problem_type[random.randint(0,len(self._problem_type)-1)]
            new_problem['input1'], new_problem['input2'], new_problem['answer'] = self._function_types[self.SELECTION]['generation']()
            new_problem['type'] = self.SELECTION
            new_problem['attempts'] = 0
            new_problem['solved'] = False
            new_problem['answer_given'] = []
            self._assigned_problems.append(new_problem)

        logging.debug(json.dumps(self._assigned_problems, indent=4))


    def _new_addition_problem(self):
        input1 = random.randint(self._lowest_number, self._max_result)
        input2 = random.randint(self._lowest_number, self._max_result)

        while input1 + input2 > self._max_result:
            input1 = random.randint(self._lowest_number, self._max_result)
            input2 = random.randint(self._lowest_number, self._max_result)

        return input1, input2, (input1 + input2)


    def _new_multiplication_problem(self):
        input1 = random.randint(self._lowest_number, self._max_result)
        input2 = random.randint(self._lowest_number, self._max_result)

        while input1 * input2 > self._max_result:
            input1 = random.randint(self._lowest_number, self._max_result)
            input2 = random.randint(self._lowest_number, self._max_result)

        return input1, input2, (input1 * input2)


    def _new_subtraction_problem(self):
        input1 = random.randint(self._lowest_number, self._max_result)
        input2 = random.randint(self._lowest_number, self._max_result)

        while input1 - input2 < self._lowest_number:
            input1 = random.randint(self._lowest_number, self._max_result)
            input2 = random.randint(self._lowest_number, self._max_result)

        return input1, input2, (input1 - input2)


    def _new_division_problem(self):
        input1 = random.randint(self._lowest_number, self._max_result)
        input2 = random.randint(self._lowest_number, self._max_result)

        while input2 == 0 or input1 == 0 or input1 % input2 > 0 or input1 == input2:
            input1 = random.randint(self._lowest_number, self._max_result)
            input2 = random.randint(self._lowest_number, self._max_result)

        return input1, input2, (input1 / input2)


    def _new_random_problem(self):
        self.SELECTION
        self.SELECTION = 'asmd'[random.randint(0,3)]
        return self._function_types[self.SELECTION]['generation']()


    def _sign_random(self):
        self.SELECTION
        return self._function_types[self.SELECTION]['sign']





# math_type = sys.argv[1]
# num_questions = int(sys.argv[2])
# max_result = int(sys.argv[3])
# lowest_number = int(sys.argv[4])

# num_pad = len(str(max_result))

# SELECTION = math_type

# correct_answers = 0

# for i in range(num_questions):
#     input1, input2 = self._function_types[math_type]['generation'](max_result, lowest_number)
#     number_provided = False

#     while not number_provided:
#         print(str(input1).rjust(num_pad + 3), '')
#         print(f' {self._function_types[self.SELECTION]["sign"]} {str(input2).rjust(num_pad)}')
#         print(''.rjust(num_pad + 3, '-'))
#         print('   ', end="")
#         # print(f'{input1} {self._function_types[self.SELECTION]["sign"]} {input2} = ', end="")
#         answer = input()

#         try:
#             solution = self._function_types[math_type]['solution'](input1, input2)
#             correct = solution == int(answer)
#             number_provided = True

#             if correct:
#                 print('Correct!\n')
#                 correct_answers += 1
#             else:
#                 print(f'The correct answer was {solution}\n')

#         except:
#             print('umm, that wasn\'t a number')

# print(f'You scored {(correct_answers/num_questions)*100}%')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

math_problems = MathProblems(
    problem_type='a',
    num_questions=2,
    max_result=4,
    lowest_number=1
)

while math_problems.next_problem():
    print(f'{math_problems.get_problem()}\n   ', end='')
    while not math_problems.test_answer(int(input())):
        print(f'{math_problems.get_problem()}\n   ', end='')

print(math_problems.get_current_score())
print(math_problems.get_attempts())
print(math_problems.get_attempts_score())
