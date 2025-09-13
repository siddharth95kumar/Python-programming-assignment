#  Write and Append Data to a File

# Writing data to the file
text1= input("Enter text to write to the file: ")
with open("output.txt","w") as file:
    file.write(text1 + "\n")
    print(f"Data successfully written to file 'output.txt'.")

# Appending data in file
text2 = input("Enter text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(text2 + "\n")
    print(f"Data successfully appended")

# Reading data in file
with open("output.txt", "r") as file:
    data = file.read()
    print(f"Final content of output.txt:")
    print(data)
