filename = input("filename: ")

while filename != "":
    print(filename)
    filename = input("filename: ")

def get_file_size(filename):
    line_count = 0
    with open(filename, "r") as in_file:
        for line in in_file:
            line_count += 1
    return line_count