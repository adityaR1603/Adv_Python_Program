#Required argument
def student(Rollno,name):
    return (Rollno,name)
S1 = student(1,"Amit")
print (S1)

#Keyword
def student(Rollno, name):
    return (Rollno, name)
S2 = student(name = "Aditya", Rollno = 2)
print (S2)

#default
def student(Rollno,name,Class = 5):
    return (Rollno,name,Class)
S3 = student(3,"Yash")
print (S3)

#variable length
def subject(*sub):
    return (sub)
S4 = subject("Mathematics", "Python")
print (S4)