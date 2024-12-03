import re

def main() :
    input = open('input.txt', 'r')

    multiplications_in_memory = get_multiplications(input.read())

    input.close()

    multiplication_sum = run_multiplications(multiplications_in_memory)

    print(f"answer for part 1: {multiplication_sum}")

# Use a regex to find any instance of mul(digits,digits) in memory:
# mul\( matches "mul("
# ( starts a capture group
# \d+,\d+ matches any comma separated pair of one or more digits
# ) closes the capture group
# \) matches ")" to capture the end of a mul() statement
def get_multiplications(memory) :
    return re.findall("mul\((\d+,\d+)\)", memory)

# Get answer for part 1
def run_multiplications(multiplications) :
    sum = 0

    for multiplication in multiplications:
        digits = multiplication.split(',')
        sum += int(digits[0]) * int(digits[1])

    return sum

if __name__ == "__main__":
    main()
