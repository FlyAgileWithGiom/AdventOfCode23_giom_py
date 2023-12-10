from logic import sum_part_numbers

if __name__ == '__main__':
    # print sum from input file
    with open('input_day3.txt') as f:
        print(sum_part_numbers(f.read()))