from random import randint
n=randint(1,100)
while True:
    x=int(input("Guess the number between 1 and 100: "))
    if x==n:
        print("You guessed it right!")
        break
    elif x<n:
        print("Try a bigger number")
    else:
        print("Try a smaller number")