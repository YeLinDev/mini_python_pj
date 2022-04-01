def display(message):
    print(message)

def display_uppercase(message):
    new_message = message.upper()
    print(new_message)

def display_lowercase(message):
    new_message = message.lower()
    print(new_message)

user_message = input('What is your message? : ')

display(user_message)
display_uppercase(user_message)
display_lowercase(user_message)

