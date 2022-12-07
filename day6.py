with open("/Users/jlefeuvr/Documents/DEV/adventcalendar/day6.in", "r") as f:
    data = [row.strip() for row in f.readlines()]
# print(data[0][0])
# print(len(data[0]))
answer_part1="init"
answer_part2="init"

for i in range(0,len(data[0])-3, 1):
    for l1,l2,l3,l4 in zip(*data[0][i:i+4]):
        if len(set([l1,l2,l3,l4])) == 4:
            answer_part1=i+4
            break
    if answer_part1 is not 'init':
        break
print ('answer part 1:', answer_part1)


for i in range(0,len(data[0])-13, 1):
    for l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14 in zip(*data[0][i:i+14]):
        if len(set([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14])) == 14:
            answer_part2=i+14
            break
    if answer_part2 is not 'init':
        break
print ('answer part 2:', answer_part2)