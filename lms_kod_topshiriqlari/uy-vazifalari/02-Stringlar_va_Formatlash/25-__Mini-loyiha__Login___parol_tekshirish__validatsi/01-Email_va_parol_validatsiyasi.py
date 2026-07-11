email = input()
parol = input()
yaroqli = (
    ("@" in email)
    and ("." in email)
    and (8 <= len(parol) <= 16)
    and (email == email.lower())
)
print(yaroqli)