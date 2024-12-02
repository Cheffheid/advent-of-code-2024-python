
def main() :
    input = open('input.txt', 'r')

    reports = get_reports(input)
    safe_reports = get_safe_reports(reports)

    print(f"safe reports: {len(safe_reports)}")

# Formats each report from the input file to ensure all the reported levels are integers.
def get_reports(input) :
    reports = []

    for line in input:
        levels = [ int(x) for x in line.split() ]
        reports.append(levels)

    return reports

# Used this to debug the processes with a smaller dataset that I can control.
def debug_reports():
    test_report = [[1, 2, 5, 8, 11, 12, 15]]

    return get_safe_reports(test_report)

# Solution for part 1 starts here.
def get_safe_reports(reports) :
    safe_reports = []

    for report in reports:
        if (report_is_safe(report)) :
            safe_reports.append(report)

    return safe_reports

def report_is_safe(report) :
    if (not difference_is_safe(report[0], report[1])) :
        return False

    direction = 'increasing'
    prev_level = report[1]

    if (report[0] > report[1]) :
        direction = 'decreasing'

    for level in report[2:] :
        difference = level - prev_level

        safe_difference = difference_is_safe(prev_level, level)
        safe_direction = direction_is_safe(direction, difference)

        if safe_difference and safe_direction :
            prev_level = level
            continue
        else :
            return False

    return True

def difference_is_safe(level1, level2) :
    difference = level1 - level2

    return abs(difference) > 0 and abs(difference) <= 3

def direction_is_safe(direction, difference) :
    if (direction == 'increasing' and difference < 0) :
        return False

    if (direction == 'decreasing' and difference > 0) :
        return False

    return True

if __name__ == "__main__":
    main()
