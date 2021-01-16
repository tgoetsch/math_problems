from problem_generator import ProblemGenerator

def main():
    problems = ProblemGenerator(
        problem_type='a',
        num_questions=2,
        max_result=4,
        lowest_number=1
    )

    while problems.next_problem():
        print(f'{problems.get_problem()}\n   ', end='')
        while not problems.test_answer(int(input())):
            print(f'{problems.get_problem()}\n   ', end='')

    print(problems.get_current_score())
    print(problems.get_attempts())
    print(problems.get_attempts_score())


if __name__ == '__main__':
    main()
