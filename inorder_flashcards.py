i=0;
tries = 2; #change this one
tried = 0;
score = 0;
while i < len(questions):
    correct = False;
    print questions[i];
    var = raw_input();
    if(var == answers[i]):
        correct = True;
        print("\nCorrect \n")
        if(tried == 0):
            score = score + 1;
        i=i+1;
        tried = 0;
    else:
        print("\nWrong \n")
        if(tries == tried):
            print("The correct answer was " + answers[i]);
            print("You got " + str(score) + " points out of " + str(len(questions)))
            tried = 0;
            score = 0;
            i=0;
        else:
            tried = tried + 1
            i=i;
    if(i == len(questions)):
        print("Congratulations, you scored " + str(score) + "/" + str(len(questions)))
