import os


def alter(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


def doubleChar(file):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if "CHAR(" in line:
                number = line[line.upper().find("CHAR(") + 5:line.find(")")]
                doubled = int(number) * 2 if 3 < int(number) < 100 else int(number)
                line = line.replace(number, str(doubled), 1)
            if "VARCHAR2" in line:
                # print(line.find("VARCHAR2")+9)
                # print(line.find(")"))
                number = line[line.upper().find("VARCHAR2") + 9:line.find(")")]
                doubled = int(number) * 2 if 3 < int(number) < 500 else int(number)
                # print(line)
                line = line.replace(number, str(doubled), 1)
                # print("change to:\n"+line)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)
    # print(file_data)


g = os.walk(r"D:\new")

for path, dir_list, file_list in g:
    for file_name in file_list:
        filename = os.path.join(path, file_name)
        print(filename)
        doubleChar(filename)
