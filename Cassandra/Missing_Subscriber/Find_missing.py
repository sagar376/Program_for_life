import csv


def find_missing(lst):
    # start = lst[0]
    start = 31800000000
    print(start)
    # end = lst[-1]
    end = 31800300000
    print(end)
    return sorted(set(range(start, end + 1)).difference(lst))


userId_list = []
with open("total_subscribers.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        userId_list.append(lines[0])
userId_list.sort()
userId_list = list(map(int, userId_list))
file = open("out.txt", "w")
# print(len(userId_list), file=file)
# print("Example:", userId_list[0])
# start_num = int(input("Start ID: "))
# last_num = int(input("End ID: "))
# print(userId_list.index(start_num), userId_list.index(last_num))
# print(type(start_num),type(last_num))
# print(len(find_missing(userId_list[userId_list.index(start_num):userId_list.index(last_num)])), file=file)
print(len(find_missing(userId_list)), file=file)
print(find_missing(userId_list), file=file)
# print(len(find_missing(userId_list[300000:360000])), file=file)
# print(find_missing(userId_list[300000:360000]), file=file)
