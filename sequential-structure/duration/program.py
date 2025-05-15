Dins = int(input("Duration in seconds: "))

hours = Dins // 3600
rest = Dins % 3600
minutes = rest // 60
seconds = rest % 60

print(f"{hours}:{minutes}:{seconds}")