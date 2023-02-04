"""                          MINI PROJECT OF QUIZ GAME                        """

s = "Welcome to my computer quiz game !!!"
print(s.capitalize())

playing = input("Do you want to play the game: ").lower()
print(playing)

if playing != "yes":
    quit()

print("Ok! \n Lets play the game \n :>>>(●'◡'●)")

print("YOUR QUESTIONS ARE :> ")
score = 0

ans = input(" when did india is indpendent ? \n :>>> ")
if ans.strip() == "1947":
    print("Correct ! ")
    score += 1
else:
    print("Incorrect ")


ans = input(
    " python is object oriented programming language is true or false ? \n :>>> "
)
if ans == "true":
    print("Correct ! ")
    score += 1
else:
    print("Incorrect ")

ans = input("how many data types are present in python ? \n :>>> ")
if ans == "14":
    print("Correct ! ")
    score += 1
else:
    print("Incorrect ")

ans = input("In which year python is inventer ? \n :>>> ")
if ans == "1991":
    print("Correct ! ")
    score += 1
else:
    print("Incorrect ")

ans = input("For data science which programming languages are important ? \n :>>> ")
if ans == "python":
    print("Correct ! ")
    score += 1
else:
    print("Incorrect ")


print("CONGRATUALATIONS !!!🎉\n YOUR SCORE IS " + str(score) + " OUT OF 5 QUESTIONS ")

print("CONGRATUALATIONS !!! YOU GOT " + str(score / 5 * 100) + "%.")










