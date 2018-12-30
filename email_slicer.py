email = input("Please enter your email : \n").strip()

user_name = email[email.index("") : email.index("@")]

domain = email[email.index("@") : ]

print(f"Your user name is {user_name}\n Your domain is {domain}")


