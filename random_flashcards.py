questions = [];
answers = [];
import random
randomRange = range(len(questions))
random.shuffle(randomRange)
i=0;
score = 0;
while i < len(questions):
    correct = False;
    print questions[randomRange[i]];
    var = raw_input();
    if(var == answers[randomRange[i]]):
        correct = True;
        print("\nCorrect \n")
        i=i+1;
        score = score + 1;
    else:
        var = raw_input();
        if(var == answers[randomRange[i]]):
            correct = True;
            print("\nCorrect \n")
            i=i+1;
        else:
            print("\nWrong \n")
            print("The correct answer was " + answers[randomRange[i]]);
            print("You got " + str(score) + " points out of " + str(len(questions)))
            score = 0;
            i = 0;
    if(i == len(questions)):
        print("Congratulations, you scored " + str(score) + "/" + str(len(questions)))
