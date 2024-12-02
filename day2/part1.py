def is_safe_report(report: list[int]):
    # set initial direction
    if report[0] < report[1]:
        direction = "+"
    elif report[0] > report[1]:
        direction = "-"
    elif report[0] == report[1]:
        return False
    for i in range(1, len(report)):
        # check that we dont invalidate direction
        if direction == "+" and report[i - 1] > report[i]:
            return False
        elif direction == "-" and report[i - 1] < report[i]:
            return False
        # check that we haven't failed the distance requirements
        if abs(report[i - 1] - report[i]) > 3:
            return False
        if abs(report[i - 1] - report[i]) < 1:
            return False
    return True


assert is_safe_report([7, 6, 4, 2, 1]) is True
assert is_safe_report([1, 2, 7, 8, 9]) is False
assert is_safe_report([9, 7, 6, 2, 1]) is False
assert is_safe_report([1, 3, 2, 4, 5]) is False
assert is_safe_report([8, 6, 4, 4, 1]) is False
assert is_safe_report([1, 3, 6, 7, 9]) is True

if __name__ == "__main__":
    with open("./day2/input.txt", "r") as f:
        reports = f.read().splitlines()
        reports = [[int(level) for level in report.split()] for report in reports]
    sum(is_safe_report(report) for report in reports)
