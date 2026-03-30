src = open("one.txt", "r") 
data = src.read() 
src.close() 

dst = open("hello.txt", "w")
dst.write(data)
dst.close()
print("File copied successfully.")