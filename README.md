# Flashcards

Python application where you can input flashcards and then given one side you
have to type what the other side is. I made this to study for some of my classes.
The program will randomize the deck and if you make a mistake you have to start
over from the start of the deck. To shuffle again just run the program again.
It's useful for memorizing definitions or having multiple choice questions.

## Tutorial

You just put questions in the question array, and the answers in the answer array.

```
questions = ["what is 1+1?", "what is 2*1?"];
answers = ["1", "2"];
```
Run the program in terminal
```
python random_flashcard.py
```
Then the program will look like
```
what is 1+1?
> 1

Correct

what is 2*1?
> 2

Correct

Congratulations, you scored 2/2
```

### Note

the ```inorder_flashcard.py``` program works essentially the same way, but it doesn't 
shuffle the deck and you can change the variable ```tries``` in the file to
give you more than one attempt
