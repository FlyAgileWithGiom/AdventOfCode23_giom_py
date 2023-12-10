from logic import score_pile

if __name__ == '__main__':
    # print scores from input file
    with open('input_day4.txt') as f:
        print(score_pile(f.read()))
