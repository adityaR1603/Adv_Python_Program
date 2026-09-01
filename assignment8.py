File1 = open("app.txt","r")
lines = File1.readlines()
File1.close()
print("Total Number of lines in app.txt : ", len(lines))
first_two_lines = lines[0 : 2]
print(" \nFirst two lines of file : ")
for i in first_two_lines :
    print(i)
File2 = open("Output.txt","w")
File2.writelines(first_two_lines)
print("\n First two lines of app.txt file are written to Output.txt file\n")
File2.close()