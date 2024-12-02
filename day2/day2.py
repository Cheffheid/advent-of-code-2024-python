
def main() :
    input = open('input.txt', 'r')

    reports = get_reports(input)
    dampener = True # To get the answer for part 1, set to False
    safe_reports = get_safe_reports(reports, dampener)

    print(f"safe reports: {len(safe_reports)}, used dampener: {dampener}")

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

# Solution for both parts starts here.
# Part 1 can be run as-is, ie. get_safe_reports(reports)
# Part 2 introduces a dampener to mark additional reports as safe if levels are removed to make it so.
def get_safe_reports(reports, dampener=False) :
    safe_reports = []

    for report in reports:
        safe_report = report_is_safe(report)

        if (not safe_report and dampener) :
            safe_report = can_report_be_made_safe(report)

        if safe_report:
            safe_reports.append(report)

    return safe_reports

# Part 1 - Test the report, given the requirements.
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

# Part 2 - Re-try the report as many times as it takes to get a safe report when one value is removed from it.
def can_report_be_made_safe(report) :
    for index, level in enumerate(report):
        dampened_report = report.copy()
        dampened_report.pop(index)
        dampened_report_is_safe = report_is_safe(dampened_report)

        if dampened_report_is_safe :
            return True

    return False

# Helper functions
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
