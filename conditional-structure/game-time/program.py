startingTime = int(input("Starting time: "))
finalTime = int(input("Final time: "))

if finalTime > startingTime:
    duration = finalTime - startingTime
else:
    duration = 24 - startingTime + finalTime
print(f"THE GAME LASTED {duration} HOUR(S)")
