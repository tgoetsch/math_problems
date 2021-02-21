import sys

from problem_generator import ProblemGenerator

def main():
    problems = ProblemGenerator(
        problem_type=(sys.argv[1] if len(sys.argv) >= 2 else 'a'),
        num_questions=(int(sys.argv[2]) if len(sys.argv) >= 3 else 2),
        max_result=(int(sys.argv[3]) if len(sys.argv) >= 4 else 1000),
        lowest_number=(int(sys.argv[4]) if len(sys.argv) >= 5 else 1),
        no_carry=(bool(sys.argv[5]) if len(sys.argv) >= 6 else True)
    )

    while problems.next_problem():
        print(f'{problems.get_problem_with_guide()}\n\n\n')
        # while not problems.test_answer(int(input())):
        #     print(f'{problems.get_problem()}\n   ', end='')

    # print(problems.get_current_score())
    # print(problems.get_attempts())
    # print(problems.get_attempts_score())


if __name__ == '__main__':
    main()
