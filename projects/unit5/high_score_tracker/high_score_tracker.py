
while True:

    high_score = input("please enter your game score: ").strip()

    if high_score.lower() == "stop":
        print("Game Session ended: ")
        break

    else:
        if int(high_score) >= 100:
            print("wow, you're on a roll !!!")
        else:
            print("Good try, keep playing")

