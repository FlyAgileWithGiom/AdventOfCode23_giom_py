from logic import score_stack

if __name__ == '__main__':
    # print scores from input file
    with open('input_day4.txt') as f:
        print(score_stack(f.read()))
