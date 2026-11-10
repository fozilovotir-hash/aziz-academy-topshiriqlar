secret = int(input())
score = 100
while True:
    guess = int(input())
    if guess == secret:
        print("TOPDINGIZ")
        break
    elif guess > secret:
        print("KATTA")
    else:
        print("KICHIK")
    score -= 10
    if score <0:
        score = 0
print(f"Ball: {score}")