#!/bin/env python3

import random
import sys
import logging
import json

class ProblemGenerator:
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
                 lowest_number: int = 0,
                 no_carry: bool = False,
                 max_number: int = None):

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
        self._no_carry = no_carry
        print(no_carry)
        print(type(no_carry))

        if not max_number:
            max_number = max_result

        self._max_number = max_number

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


    def get_problem_with_guide(self, problem_index: int = None) -> str:
        if not problem_index:
            problem_index = self.current_problem

        input1 = str(self._assigned_problems[problem_index]['input1'])
        input2 = str(self._assigned_problems[problem_index]['input2'])

        num_pad = len(str(input1)) if len(str(input1)) > len(str(input2)) else len(str(input2))
        full_pad = num_pad * 2 + 1

        sign = self._function_types[self._assigned_problems[problem_index]['type']]['sign']

        input1_str = f"|{'|'.join(list(input1.rjust(num_pad, ' ')))}|"
        input2_str = f"|{'|'.join(list(input2.rjust(num_pad, ' ')))}|"

        return '\n'.join((f'{input1_str.rjust(full_pad + 3, " ")}',
                f' {sign} {input2_str.rjust(full_pad, " ")}',
                '   '.ljust(full_pad + 3, '-')))


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
        return correct / attempts if attempts > 0 else 0


    def get_attempts(self) -> int:
        return sum([problem['attempts'] for problem in self._assigned_problems])


    def _assign_problems(self):
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
        input1 = random.randint(self._lowest_number, self._max_number)
        input2 = random.randint(self._lowest_number, self._max_number)

        acceptable_problem = input1 + input2 <= self._max_result

        if self._no_carry:
            acceptable_problem = (acceptable_problem and
                                 not self._test_addition_carry(input1, input2))


        while not acceptable_problem:
            input1 = random.randint(self._lowest_number, self._max_number)
            input2 = random.randint(self._lowest_number, self._max_number)

            acceptable_problem = input1 + input2 <= self._max_result

            if self._no_carry:
                acceptable_problem = (acceptable_problem and
                                     not self._test_addition_carry(input1, input2))

        return input1, input2, (input1 + input2)


    def _test_addition_carry(self, input1: int, input2: int):
        numplaces = len(str(input1)) if len(str(input1)) > len(str(input2)) else len(str(input2))
        working_input1 = input1
        working_input2 = input2

        for _ in range(numplaces):
            input1_ones_place = working_input1 % 10
            input2_ones_place = working_input2 % 10

            if input1_ones_place + input2_ones_place >= 10:
                print(f'Carry found for {input1} + {input2}')
                return True

            working_input1 = (working_input1 - input1_ones_place) / 10
            working_input2 = (working_input2 - input2_ones_place) / 10

        return False

    def _new_multiplication_problem(self):
        input1 = random.randint(self._lowest_number, self._max_number)
        input2 = random.randint(self._lowest_number, self._max_number)

        while input1 * input2 > self._max_result:
            input1 = random.randint(self._lowest_number, self._max_number)
            input2 = random.randint(self._lowest_number, self._max_number)

        return input1, input2, (input1 * input2)


    def _new_subtraction_problem(self):
        input1 = random.randint(self._lowest_number, self._max_number)
        input2 = random.randint(self._lowest_number, self._max_number)

        while input1 - input2 < self._lowest_number:
            input1 = random.randint(self._lowest_number, self._max_number)
            input2 = random.randint(self._lowest_number, self._max_number)

        return input1, input2, (input1 - input2)


    def _new_division_problem(self):
        input1 = random.randint(self._lowest_number, self._max_number)
        input2 = random.randint(self._lowest_number, self._max_number)

        while input2 == 0 or input1 == 0 or input1 % input2 > 0 or input1 == input2:
            input1 = random.randint(self._lowest_number, self._max_number)
            input2 = random.randint(self._lowest_number, self._max_number)

        return input1, input2, (input1 / input2)


    def _new_random_problem(self):
        self.SELECTION
        self.SELECTION = 'asmd'[random.randint(0,3)]
        return self._function_types[self.SELECTION]['generation']()


    def _sign_random(self):
        self.SELECTION
        return self._function_types[self.SELECTION]['sign']
