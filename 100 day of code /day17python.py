while True:
    print("left or right?")
    d = input("Pick a direction:")
    if d == "right":
        print("You death")
        break
    elif d == "left":
        continue
    else:
        print("You won")
        exit()
print("Game over")