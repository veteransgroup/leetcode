import datetime
start=datetime.datetime.timestamp(datetime.datetime.now())
# file = open('passwords.txt', 'r')
# # newfile = open('testext.txt', 'w')
# # print(file.readline(3))  # Dog
# # print(file.readline(3))  # 2 empty lines
# # print(file.readline(3))  # Cat
# # print(file.readline(3))  # 2 empty lines
# # print(file.readline(3))  # Rab
# # print(file.readline(3))  # bit
# # print(file.readlines())
# for line in file.readlines():
#     print(line)
#
# file.close()


with open("E:\\files\\passwordDictionary\\realuniq.lst","r",encoding="utf-8",errors="ignore") as f:
    for line in f:
        print(line.strip())

finish = datetime.datetime.timestamp(datetime.datetime.now())
print(finish - start)