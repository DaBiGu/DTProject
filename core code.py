import random
empty_respirtory = {}
for i in range(1,31):
    empty_respirtory[i] = 0
user_list =[{"username":"root","password":"123456","drop_count":0,"respirtory":{}}]
running = True
while running:
    choice = str(input("Welcome! Enter R to register, L to login, E to exit\n"))
    if choice == "R":
        creating_username = True
        username_available = True
        while creating_username:
            username = str(input("Welcome new user! Please enter your username, available characters are a~z, A~Z, 0~9 and _.\n"))
            for c in username:
                if not ('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9' or c == '_'):
                    print('Error: Username is invalid!\n')
                    username_available = False
            for user in user_list:
                if user["username"] == username:
                    print('Error: Username already exists!\n')
                    username_available = False
            if username_available == False:
                continue
            else:
                creating_username = False
        creating_password = True
        password_available = True
        while creating_password:
            password = str(input("Welcome new user! Please enter your password, available characters are a~z, A~Z, 0~9 and _.\n"))
            for c in password:
                if not ('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9' or c == '_'):
                    print('Error: Password is invalid!\n')
                    password_available = False
            if password_available == False:
                continue
            else:
                creating_password = False
        new_user = {}
        new_user["username"] = username
        new_user["password"] = password
        new_user["drop_count"] = 0
        new_user["respirtory"] = empty_respirtory
        user_list.append(new_user)
        continue
    elif choice == "L":
        username = str(input("Welcome! Please enter your username to continue.\n"))
        username_legal = False
        for user in user_list:
            if user["username"] == username:
                print(f"Welcome back, {username}!")
                username_legal = True
                break
        if not username_legal:
            print("Please enter a legal username!\n")
            continue
        password = str(input("Welcome! Please enter your password to continue.\n"))
        if user["password"] != password:
            print("Password Incorrect.\n")
    elif choice == "E":
        running = False

    drawn_cards = []
    new_cards = []
    for i in range(1,31):
        if user["respirtory"][i] == 0:
            new_cards.append(i)
        else:
            drawn_cards.append(i)
    random.shuffle(drawn_cards)
    random.shuffle(new_cards)
    if user["drop_count"] == 0:
        current_card = random.randomint(1,30)
        if current_card in drawn_cards:
            user["drop_count"] += 1
            user["respirtory"][current_card] += 1
    elif user["drop_count"] == 1:
        choice = random.randomint(1,10)
        if choice <= 4:
            current_card = new_cards[0]
            user["respirtory"][current_card] += 1
            user["drop_count"] = 0
        else:
            current_card = drawn_cards[0]
            user["respirtory"][current_card] += 1
            user["drop_count"] += 1
    elif user["drop_count"] == 2:
        current_card = new_cards[0]
        user["respirtory"][current_card] += 1
        user["drop_count"] = 0






