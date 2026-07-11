login = input()
parol = input()
if len(login) >= 3 and len(parol) >= 8 and login != parol:
    print(True)
else:
    print(False)