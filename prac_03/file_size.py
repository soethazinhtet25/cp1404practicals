def get_file_size(filename):
    line_count = 0
    with open(filename, "r") as in_file:
        for line in in_file:
            line_count += 1
    return line_count

filename = input("filename: ")

while filename != "":
    try:
        print(f"{filename} has {get_file_size(filename)} lines.")
    except FileNotFoundError:
        print(f"ERROR: {filename} does not exist.")
    filename = input("filename: ")