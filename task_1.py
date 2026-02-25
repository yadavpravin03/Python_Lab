#Print numbers 1 to 5
i=1 
while i<=5:
    print(i)
    i=i+1

#Sum of numbers 
n=int(input("Enter number :"))
i=1
sum=0
while i<=n:
    sum=sum+1
    i=i+1
    print(sum)

#print odd numbers between 1 to 20
i=0
while i<20:
    i=i+1
    if i % 2 !=0:
        print(i)

#print table of four
num=4
i=1
while i<=10:
    print(num," X", i," = ",num*i)
    i=i+1

#print reverse numbers
i=10
while i>=1:
    print(i)
    i=i-1

#print largest number
num=[10,20,30,40]   
largest=max(num)
print(largest)

#print even numbers between 1 to 20
i=0
while i<20:
    i=i+1
    if i % 2 ==0:
        print(i)