secret_word="giraffe"
guess = ""

attempt = 0
attempt_limit = 3
while guess != secret_word and attempt < attempt_limit:
    guess = input("Enter guess : ")
    attempt+=1

if guess == secret_word:
    print("You win!")
else:
    print("You lose!")