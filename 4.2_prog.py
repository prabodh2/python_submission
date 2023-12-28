def get_user_info(*args, **kwargs):
    if args:
        name = args[0]
    else:
        name = kwargs.get('name', input("Enter your name: "))

    if len(args) > 1:
        email = args[1]
    else:
        email = kwargs.get('email', input("Enter your email: "))

    if len(args) > 2:
        age = args[2]
    else:
        age = kwargs.get('age', input("Enter your age: "))

    return {'name': name, 'email': email, 'age': age}

user_info = get_user_info(name="John", age=25)
print("User Info:", user_info)
