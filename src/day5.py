indexOf = lambda item, list_: list_.index(item) if item in list_ else -1
f = open('data/day5.txt', 'r+')
section_one = True
rules = []
updates = []
for line in f.readlines():
    line = line.strip()
    if not line:
        section_one = False
        continue
    if section_one:
        r1, r2 = line.split('|')
        rules.append((int(r1), int(r2)))
    else:
        updates.append([int(page) for page in line.split(',')])

def one_star(rules, updates):
    mid_pages = []
    for update in updates:
        for r1, r2 in rules:
            if indexOf(r1, update) == -1 or indexOf(r2, update) == -1:
                continue
            elif indexOf(r1, update) > indexOf(r2, update):
                break
        else:
            mid_pages.append(update[int(len(update)/2)])
    return sum(mid_pages)


def two_star(rules, updates):
    def correct_update(rules, update):
        correct = False
        while(not correct):
            for r1, r2 in rules:
                if indexOf(r1, update) == -1 or indexOf(r2, update) == -1:
                    continue
                elif (i1:=indexOf(r1, update)) > (i2:=indexOf(r2, update)):
                    update[i1] = r2
                    update[i2] = r1
                    break
            else:
                correct = True
        return update[int(len(update)/2)]
    
    mid_pages = []
    for update in updates:
        for r1, r2 in rules:
            if indexOf(r1, update) == -1 or indexOf(r2, update) == -1:
                continue
            elif indexOf(r1, update) > indexOf(r2, update):
                mid_pages.append(correct_update(rules, update))
                break
    return sum(mid_pages)

print(one_star(rules, updates))
print(two_star(rules, updates))
