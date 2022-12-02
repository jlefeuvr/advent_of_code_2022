with open("/Users/jlefeuvr/Documents/DEV/adventcalendar/day2.in", "r") as f:
    data = [row.strip() for row in f.readlines()]
mapping_dict_answer1={"A X":4, "A Y":8, "A Z":3, "B X":1, "B Y":5,"B Z":9,"C X":7, "C Y":2, "C Z":6}
mapping_dict_answer2={"A X":3, "A Y":4, "A Z":8, "B X":1, "B Y":5,"B Z":9,"C X":2, "C Y":6, "C Z":7}
answer_1=0
answer_2=0
for result in data:
    answer_1= answer_1 + mapping_dict_answer1[result]
    answer_2=answer_2 + mapping_dict_answer2[result]

print('answer 1:', answer_1)
print('answer 2:', answer_2)