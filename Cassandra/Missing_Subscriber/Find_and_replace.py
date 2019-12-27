def listToString(s):
    # initialize an empty string
    str1 = []

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


f = open("Test_file.txt", 'r')
filedata = f.read()
# replace_list = [31800009785, 31800019785, 31800029785, 31800039785, 31800049785, 31800059785, 31800069785, 31800079785,
#                 31800089785, 31800099785, 31800109785, 31800119785, 31800129785, 31800139785, 31800149785, 31800159785,
#                 31800169785, 31800179785, 31800189785, 31800199785, 31800209785, 31800219785, 31800229785, 31800239785,
#                 31800249785, 31800259785, 31800269785, 31800279785, 31800289785, 31800299785]

replace_list = [31806009785, 31806019785, 31806029785, 31806039785, 31806049785, 31806059785]

replace_list1 = [str(i) for i in replace_list]

index = 0
for i in replace_list1[0:]:
    str1 = str(replace_list[index] + 1)
    index = index + 1
    print(str1)
    newdata = filedata.replace("31800019786", i, 4)
    # str2=str(i+"-"+i)
    # print(str2)
    # str3=str(i + "-" + str1)
    # print(str3)
    # newdata = filedata.replace(str2, str3)
    f = open("out_replace_slam.txt", "a")
    f.write(newdata)
    f.close()
