# Dictionary creation

mydict = {
          'Wolf':99,
          'Raizel':98,
          'Slayer':97,
          'Samar':96,
          'Fiction':95,
}
n = input("Enter the student's name: ")
if n in mydict:
    print(f"{n}'s marks: ",mydict[n])
else:
    print(f"Student not found. ")

