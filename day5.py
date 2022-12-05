with open("/Users/jlefeuvr/Documents/DEV/adventcalendar/day5.in", "r") as f:
    # data = [row.split('\n') for row in f.readlines()]
    data = f.read().splitlines()

#separating initial stack from instuctions
raw_stack_input=data[:data.index('')]
raw_instructions=data[data.index('')+1:]
raw_starting_stack=[]
# zip gives list of iterables (i1,n1),(i2,n2), i and n are row in the input file, so we get list of colum with all characters
column_list=list(zip(*raw_stack_input))

#We keep only file char column that correspond to a stack
for column in column_list:
    if column[len(column_list[0])-1] is not ' ':
        raw_starting_stack.append(list(column[:-1]))
print(raw_starting_stack)

#we create a clean stack list (deleting " " and putting the top container at the end of the list)
stack_list=[' '.join(stack[::-1]).strip().split() for stack in raw_starting_stack]

#we create the list of instruction (list of ("move","x","...")
instructions =[instruction.split() for instruction in raw_instructions]

#part1
for instruction in instructions:
    stack_list[int(instruction[5])-1]= stack_list[int(instruction[5])-1] + stack_list[int(instruction[3])-1][-int(instruction[1]):][::-1]
    stack_list[int(instruction[3])-1]= stack_list[int(instruction[3])-1][:-int(instruction[1])]
print("answer1","".join([stack[-1] for stack in stack_list]))

#part2, please comment previous section
for instruction in instructions:
    stack_list[int(instruction[5])-1]= stack_list[int(instruction[5])-1] + stack_list[int(instruction[3])-1][-int(instruction[1]):]
    stack_list[int(instruction[3])-1]= stack_list[int(instruction[3])-1][:-int(instruction[1])]

print("answer2","".join([stack[-1] for stack in stack_list]))
