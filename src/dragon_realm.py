from time import sleep

choice2 = 'y'

while(choice2 == 'y'):
    print('''You are in a land full of dragons. In front of you,
    you see two caves. asd;flkjas;dlkfj
    ljkasjdflkjsdf
    jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj\n''')
    
    print('Which cave will you go into? (1 or 2)')
    choice1 = input()
    
    if choice1 == 1:
        print('asdf cave 1')
    else:
        print('asdf cave 2')
        sleep(0.5)
        print('dragon comes out...')
        sleep(1)
        print('eats you or something!')
        sleep(2)
        
    choice2 = input('Play again? (y/n)')