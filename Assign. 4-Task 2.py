n=input("Enter text to write to the file: ")
print("Data successfully written to output.txt. \n")
file=open('output.txt','w')
file.write(n)

n1=input("Enter additional text to append: ")
appending_file=file.write(n1)
print("Data successfully appended. \n")

reading_file=open('output.txt','r')
print("Final content of output.txt: \n",n)
print(n1)

file.close()
