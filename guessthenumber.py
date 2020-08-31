i = 1
print ("THE GAME OF GUESS THE NUMBER\n")
print ("This is the list of number\n")
print (15,34,6,9,67,66,32,67,14,89,53,99,43,88,)

print ("You have only 3 time to choose the number\n")
while(i<=3) :

    i = i+1
    inp = input("Enter your guess Number\n")
    if inp==89:
         print ("You are WINNER\n")
         break

    if inp<89:
         print("Real value is Bigger then this number\n")

    if inp>89:
         print("Real value is Smaller then this  Number\n")
         continue
else:
         print("Real value is 89\n")
print("!!!!!!GAME OVER!!!!!!\n")
