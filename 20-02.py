#На первой строке вводится количество классов.
#Затем для каждого класса вводится блок информации вида:
#На первой строке – N – количество учеников в классе.
#Далее вводится N строк вида: «Фамилия Оценка»

marks = list()
count_people = int(input())
for num in range(count_people):
    prom = set()
    for i in range(int(input())):
        part = input().split()
        if part[1] == '5':
            prom.add(part[1])
    marks.append(prom)
print(marks)
if all(map(lambda x: x == {'5'}, marks)) and len(marks) == count_people:
    print('ДА')
else:
    print('НЕТ')