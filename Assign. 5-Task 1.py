students={'Mike':78,'Nick':66,'Celin':77,'Alice':85}
n=input("Enter the student's name: ")
if n in students:
    print("{}'s marks: {}".format(n,students[n]))
else:
    print("Student not found")