a, b = 10, 'ae'

try:
    print (a + b)
except TypeError as e:
    print(f'enter a valid number as an integer or a float')
except Exception as e:
    print(f'sumn else went wrong...')

    print('Continuing...')