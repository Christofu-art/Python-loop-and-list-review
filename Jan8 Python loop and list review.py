#Chris Sullivan
#while loop to print the numbers 50-0 counting down by 5s
num = 50 #starting point
while num>0: #goes down so it prints
    print(num, end = " ")
    num -= 5 #what you countdown by
    
#while loop to print "hehe monkey doesn't wear any pants" until the user types "bannana"
UserInput = "something" #dummy value
while UserInput != "bannana":
    UserInput = input("hehe monkey doesn't wear any pants")


Warhammer = ["Dark Angels", "Blood Angels", "Ultramarines"]
print(Warhammer)
Warhammer.append("Blood Ravens")
print(Warhammer)
Warhammer.sort()
print(Warhammer)
Warhammer.remove("Blood Angels")
print(Warhammer)
