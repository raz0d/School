# f = open("f.txt")
# q = open("q.txt", "w")
# s = f.readline()
# for i in s:
#     if i in "aA":
#         q.write(s)
#         s.replace()
# f.close()
# q.close()


# file_with_content = open("myfile.txt", "r+")
# line = file_with_content.readline()
# a_wali_lines = []
# while line:
#     location = file_with_content.tell()
#     if "a" in line or "A" in line:
#         file_with_content.seek(0)
#         file_with_content.write("")
#         a_wali_lines.append(line)
#     line = file_with_content.readline()
# file_with_content.close()
#
# empty_file = open("new_file.txt", "w")
# empty_file.writelines(a_wali_lines)
# empty_file.close()


f = open("myfile.txt", "r+")
q = open("new_file.txt", "w")
s = f.readline()
while s:
    if "a" in s.lower():
        q.write(s)
    s = f.readline()
f.close()
q.close()
