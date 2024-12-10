import copy


f = open('day1/day1.txt', 'r+')
left = []
right = []
for line in f.readlines():
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

def one_star(left_list, right_list):
    distance = []
    left = copy.deepcopy(left_list)
    right = copy.deepcopy(right_list)
    while len(left) > 0:
        min_l = min(left)
        min_r = min(right)
        distance.append(abs(min_r - min_l))
        left.remove(min_l)
        right.remove(min_r)   

    print(sum(distance))

def two_star(left, right):
    similarity = []
    for l in left:
        similarity.append(l*right.count(l))
    
    print(sum(similarity))

one_star(left, right)
two_star(left, right)