# 1.
# name = input("Name: ")
# out_file = open("name.txt", "w")
# out_file.write(name)
# out_file.close()

# 2.
in_file = open("name.txt", "r")
text = in_file.read()
print(f"Hi {text}!")
in_file.close()
