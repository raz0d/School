#QUESTION - 6

# SIMPLE AND EASY LOGIC

def a_lines():
    f1 = open("myfile.txt", "r")
    f2 = open("to_write.txt", "w")
    f1_cnt = f1.readlines()
    cnt = []
    for i in f1_cnt:
        if "a" in i:
            f2.write(i)
        else:
            cnt.append(i)
    f1.close()
    f2.close()
    with open("myfile.txt", "w") as f:
        f.writelines(cnt)

a_lines()


#---------------------------------------------

# LOGIC - 2

read_file = open("myfile.txt")
content_list = read_file.readlines()
read_file.close()

def no_a_lines():
    new_list = []
    for line in content_list:
        if "a" not in line:
            new_list.append(line)
    return new_list

def a_lines():
    new_list = []
    for line in content_list:
        if "a" in line:
            new_list.append(line)
    return new_list

with open("myfile.txt", "w") as file:
    file.writelines(no_a_lines())

write_file = open("to_write.txt", "w")
for i in range(len(a_lines())):
    write_file.write(a_lines()[i])
write_file.close()