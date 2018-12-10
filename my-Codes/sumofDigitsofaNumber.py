#this line takes input as int showing "Enter a number" string to the user
n=int(input("Enter a number:"))
tot=0
while(n>0):
#the lines inside the while loop are shown using indentation
    dig=n%10
    tot=tot+dig
    n=n//10 #Previously this line had n/10. This resulted error. This has been fixed
#this line will print the total of the digits of the given number
print("The total sum of digits is:",tot)
