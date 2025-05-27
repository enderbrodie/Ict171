def choice():
    rep = input()
    if rep == '1':
        print(".")
    
    if rep == '2':
        print("You turn around and someone smashed a bottle over you head your DEAD")


L = 0
print("Welcome to the forest")
print("Use the number to help you navigate this game")
print("You off to side of the road and stare into the wood as if it wants you to enter. You get out of your car")
print("1.Forward 2.Go back to the car")
while L == 0:
    rep = input()
    if rep == '1':
        print("you move forward\n")
        print("There are still only tree blocking your path but you can still get around them")
    if rep == '2':
        print("You turn around and someone smashed a bottle over you head your DEAD")
        break
    print("1.Forward 2.walk round")