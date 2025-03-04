print("MATH QUIZ")
print("Make sure you answer it right")
ready = input("Are you ready?")
if ready == "yes":
    ques1 = input("what is 1+1?")
    if ques1 == "2":
        print(" you are correct")
        ques2 = input("what is 2+2?")
        if ques2 == "4":
            print("good job")
            print("your mark is 100%")
            print("you have done the quiz")
        else:
            print("you are wrong, your mark is 5/10")
    else:
        print("you are wrong, your mark is 0/10")
elif ready == "maybe":
    maybe = input("make sure you ready for the test")
    if maybe == "sure":
        print("lets do it")
        ques1 = input("what is 1+1?")
        if ques1 == "2":
            print(" you are correct")
            ques2 = input("what is 2+2?")
            if ques2 == "4":
                print("good job")
                print("you have done the quiz")
                print("your mark is 100%")
            else:
                print("you are wrong, your mark is 5/10")
                print("why you do the quiz why u not ready yet?")
        else:
            print("you are wrong, your mark is 0/10")
            print("why you do the quiz why u not ready yet?")
    else:
        print("its ok, i let you have more time to study")
        
else:
    print("go study then")