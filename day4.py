with open("/Users/jlefeuvr/Documents/DEV/adventcalendar/day4.in", "r") as f:
    data = [row.strip().split(',') for row in f.readlines()]
complete_overlap=0
partial_overlap=0
for pair in data:
    first_elf=set(range(int(pair[0].split("-")[0]),int(pair[0].split("-")[1])+1,1))
    second_elf=set(range(int(pair[1].split("-")[0]),int(pair[1].split("-")[1])+1,1))
    intersection=(first_elf).intersection(second_elf)       
    if intersection in (first_elf, second_elf):
        complete_overlap+=1
    elif (len(intersection)) is not 0:
        partial_overlap+=1
print('answer 1:',complete_overlap)
print('answer 2:',partial_overlap + complete_overlap)