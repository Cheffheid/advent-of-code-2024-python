import re

def main() :
    memory_string = get_memory_string()

    # Use a regex to find any instance of mul(digits,digits) in the memory string:
    # mul\( matches "mul("
    # ( starts a capture group
    # \d+,\d+ matches any comma separated pair of one or more digits
    # ) closes the capture group
    # \) matches ")" to capture the end of a mul() statement
    multiplications_part_one = get_multiplications(memory_string, "mul\((\d+,\d+)\)")

    # This regex is similar, except it also captures dos and donts as markers for which multiplications should be run.
    multiplications_part_two = get_valid_part_two_multiplications(get_multiplications(memory_string, "mul\((\d+,\d+)\)|(don't\(\))|(do\(\))"))

    multiplication_sum_part_one = run_multiplications(multiplications_part_one)
    multiplication_sum_part_two = run_multiplications(multiplications_part_two)

    print(f"answer for part 1: {multiplication_sum_part_one}")
    print(f"answer for part 2: {multiplication_sum_part_two}")

def get_memory_string() :
    input = open('input.txt', 'r')
    memory_string = input.read()
    input.close()

    return memory_string

def get_multiplications(memory, regex) :
    return re.findall(regex, memory)

def get_valid_part_two_multiplications(multiplications_list) :
    valid = True
    valid_list = []

    for hits in multiplications_list:
        if "don't()" in hits:
            valid = False
            continue

        if "do()" in hits:
            valid = True
            continue

        if valid:
            valid_list.append(hits[0])

    return valid_list

# Get answer for part 1
def run_multiplications(multiplications) :
    sum = 0

    for multiplication in multiplications:
        digits = multiplication.split(',')
        sum += int(digits[0]) * int(digits[1])

    return sum

if __name__ == "__main__":
    main()
