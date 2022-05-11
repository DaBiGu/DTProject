import random
history = {}
for i in range(1,11):
    history[i] = 0
playing = True
while playing:
    current_card = random.randrange(1,10)
    if history[current_card] < 2:
        history[current_card] += 1
        print(current_card)
    else:
        continue
    status = str(input("Draw Again? Y/N\n"))
    if status == "N":
        playing = False

