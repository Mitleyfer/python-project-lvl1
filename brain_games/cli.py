import prompt

def welcome_user():
    name = prompt.string('Enter your name, please: ')
    print(f'Hello, {name}!')
    return name
