n=int(input("Enter the number of elemenets you want in the list : "))
list1=[]
for i in range (0,n):
    a=int(input())
    list1.append(a)
print("The entered list is : ",end="")
print (list1)
print("The positive numbers in the list are : ",end="")
for i in list1:
    if(i>0):
        print(i, end=" ")
