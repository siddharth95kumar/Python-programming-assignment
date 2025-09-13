# Read a File and Handle Errors

try:
    with open("sample.txt", "r") as file1:
        line_no = 1
        print("Reading file contents: ")
        for i in file1:
            print("Line " , str(line_no) , ": " + i, end="")
            line_no = line_no + 1

except FileNotFoundError:
    print(f"The file 'sample.txt' was not found.")



