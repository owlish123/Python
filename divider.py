grades = open('C:\\Users\\86152\\Desktop\\Project1\\grades.txt', encoding='UTF-8')
scores = grades.readlines()
grades.close()

GPA = {} # id - gpa
for line in scores:
    line = line.strip().split('\t')
    GPA[line[0]] = float(line[-1]) # key - value

lists = open('C:\\Users\\86152\\Desktop\\Project1\\students.txt', encoding='UTF-8')
students = lists.readlines()
lists.close()

con = [] # [id, name, gpa]
checker = {}
for line in students:
    line = line.strip().split('\t')
    id = line[0]
    gpa = 0.0
    if id not in checker.keys():
        checker[id] = True
        if id in GPA.keys():
            gpa = GPA[id]
        con.append([id, line[1], gpa])
    else:
        print (line)
    # print (con[-1])
    

print (len(con))

con = sorted(con, key = lambda t:t[-1], reverse=True)

from math import ceil
class_num = 21

classes = []
gap = 1
k = ceil(len(con)/class_num)
i = 0
for a in range(k):
    classes.append([None for b in range(class_num)])
    
    # print (classes[a])
    
    if gap == 1:
        head, tail = 0, class_num
        while head < tail:
            if i >= len(con):
                break
            classes[a][head] = con[i]
            
            # print("Student:", con[i])
            # print (classes[a])
            # input('Continue')
            
            head += gap
            i +=1
    else:
        head, tail = class_num - 1, -1
        while head > tail:
            if i >= len(con):
                break
            classes[a][head] = con[i]
            
            # print("Student:", con[i])
            # print (classes[a])
            # input('Continue')
            
            head += gap
            i +=1
    gap *= -1
    
    # print (classes[-1])
    # input('Continue?')
# print (classes)

out = open('C:\\Users\\86152\\Desktop\\Project1\\out.txt', 'w', encoding='UTF-8')

for a in range(k):
    for i in range(2):
        for j in range(class_num):
            if classes[a][j] is not None:
                out.write('%s\t' % classes[a][j][i])
        out.write('\n')
    for j in range(class_num):
        if classes[a][j] is not None:
            out.write('%.3f\t' % classes[a][j][2])
    out.write('\n')

out.close()