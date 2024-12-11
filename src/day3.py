import re

# instructions = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
instructions = []
f = open("data/day3.txt", "r+")
for line in f.readlines():
    instructions.append(line)

def one_star(instruction):
    """Compute total of multiplications."""
    RE_MUL = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    total = 0
    for instruction in instructions:
        for x,y in RE_MUL.findall(instruction):
            total += int(x)*int(y)
    return total

def two_star(instruction):
    """Compute total of multiplications with do/don't instructions."""
    RE_MUL = re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)")
    total = 0
    do = True
    for instruction in instructions:
        for match in RE_MUL.finditer(instruction):
            if match.group(0) == "do()":
                do = True
            elif match.group(0) == "don't()":
                do = False
            else:
                if do:
                    total += int(match.group(1))*int(match.group(2))
    return total

print(one_star(instructions))
print(two_star(instructions))