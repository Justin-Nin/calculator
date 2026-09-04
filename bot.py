bot_name: str = 'Verity'
print(f'{bot_name}: Hello, I\'m {bot_name}, your personal helper friend!')

while True:
    user_input: str = input ('You: ').lower()

    if user_input in ['hi', 'hello', 'hello!' 'hey', 'yo', 'wsp']:
        print(f'{bot_name}: Hey, its me, its {bot_name}, ask me anything!')
    elif user_input in ['bye', 'goodbye', 'see you later', 'cya', 'peace']:
        print(f'{bot_name}: Goodbye! Feel free to come back anytime!')
    elif user_input in ['+', 'add']:
        print(f'{bot_name}: Sure! let\'s do some addition! Enter the number that  you would like!')
        try:
            num1: float = float(input('First Number: '))
            num2: float = float(input('Second Number: '))
            print(f'{bot_name}: The sum is {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: I\'m sorry, that doesn\'t seem to work, try a valid number!')
    else:
             print(f'{bot_name}: I\'m sorry I don\'t understand that!')
