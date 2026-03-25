
#Read 
f=open("one.txt","r")
data =f.read()
print("File content :",data)
f.close()

# Reading specific number of Characters
f=open("one.txt","r")
data =f.read(5)
print("first 5 characters:",data)
f.close()

#Readline
f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
print("Line1",line1)
print("Line2",line2)
f.close()

#readlines
f=open("one.txt","r")
data =f.readlines()
print("List of lines :",data)
print("Number of lines :",len(data))
f.close()

#Read specific line 
f=open("one.txt","r")
data =f.readlines()
print(data[0].strip())
f.close()