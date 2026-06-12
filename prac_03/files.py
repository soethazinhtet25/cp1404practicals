# 1.
# name = input("Name: ")
# out_file = open("name.txt", "w")
# out_file.write(name)
# out_file.close()

# 2.
# in_file = open("name.txt", "r")
# text = in_file.read()
# print(f"Hi {text}!")
# in_file.close()

# 3.
# with open("numbers.txt", "r") as in_file:
#     first_number = int(in_file.readline())
#     second_number = int(in_file.readline())
#
# print(first_number + second_number)

# 4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)