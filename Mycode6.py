import csv
file = open(r'C:\Users\86138\Desktop\student_score.csv','r')
a = csv.DictReader(file)
list1 = []
list2 = []
for i in a:
    list1.append(i)
def math():
    for i in range(0,len(list1)):
        list2.append(int(list1[i]['高数']))
    list2.sort()
    for i in range(0, len(list1)):
        if int(list1[i]['高数']) == list2[-1]:
            print("高数: "+list1[i]['学号'] , list2[-1])
        elif int(list1[i]['高数']) == list2[0]:
            print("高数: " + list1[i]['学号'], list2[0])
    print("平均分：" + sum(list2) / len(list2))
def english():
    for i in range(0,len(list1)):
        list2.append(list1[i]['英语'])
    list2.sort()
    for i in range(0, len(list1)):
        if int(list1[i]['英语']) == list2[-1]:
            print("英语: "+list1[i]['学号'] , list2[-1])
        elif int(list1[i]['英语']) == list2[0]:
            print("英语: " + list1[i]['学号'], list2[0])
    print("平均分：" + sum(list2) / len(list2))
def python():
    for i in range(0,len(list1)):
        list2.append(list1[i]['Python'])
    list2.sort()
    for i in range(0, len(list1)):
        if int(list1[i]['Python']) == list2[-1]:
            print("Python:" +list1[i]['学号'] , list2[-1])
        elif int(list1[i]['Python']) == list2[0]:
            print("Python: " + list1[i]['学号'], list2[0])
    print("平均分：" + sum(list2) / len(list2))
def sorce():
    AD = {}
    for i in range(0, len(list1)):
        AD[int(list1[i]['学号'])] = int(list1[i]['高数'])+int(list1[i]['英语'])+int(list1[i]['Python'])
    print(AD)
    print(sorted(AD.values()))