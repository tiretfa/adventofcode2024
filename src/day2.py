f = open("data/day2.txt", "r+")
reports = []

for line in f.readlines():
    reports.append([int(level) for level in line.split()])


def is_safe(report):
    """Predicat to define if report is safe or not."""
    tendancy = ""
    for level, next_level in zip(report[:-1], report[1:]):
        # print(f"{i} {level} {next_level}")
        if not(1 <= abs(level - next_level) <= 3):
            return False
        if not tendancy:
            if level - next_level > 0:
                tendancy = "decr"
            else:
                tendancy = "incr"
        else:
            if ((level - next_level > 0 and tendancy == "incr") or 
                (level - next_level < 0 and tendancy == "decr")):
                return False
    return True


def one_star(reports):
    """Calculate how many reports are safe."""
    safe_report_count = 0
    for report in reports:
        if is_safe(report):
            safe_report_count += 1
    return safe_report_count


def two_star(reports):
    """Calculate how many report are safe too but with different rules."""
    safe_report_count = 0
    for report in reports:
        safe = is_safe(report)
        if safe:
            safe_report_count += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i+1:]):
                    safe_report_count += 1
                    break
            
    return safe_report_count

print(one_star(reports))
print(two_star(reports))