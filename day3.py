import string
with open("/Users/jlefeuvr/Documents/DEV/adventcalendar/day3.in", "r") as f:
    data = [row.strip() for row in f.readlines()]

priority_mapping=list(string.ascii_letters)
priority_list_answer_1=[]
priority_list_answer_2=[]

##part 1
for rucksack in data:
    priority_list_answer_1.append(priority_mapping.index(list(set(rucksack[:(len(rucksack)//2)]).intersection(set(rucksack[(len(rucksack)//2):])))[0])+1)
print('answer 1:',sum(priority_list_answer_1))

##part 2

for r1, r2, r3 in (data[i:i+3] for i in range(0, len(data)-1, 3)):
    priority_list_answer_2.append(priority_mapping.index((list(set(r1).intersection(set(r2)).intersection(set(r3))))[0])+1)
print('answer 2:',sum(priority_list_answer_2))
