from random import randint

def guess_pass():
    password = input('Enter your password: ')
    char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    program = ''
    
    while program != password:
        program = ""
        for i in range(len(password)):
            guess = char[randint(0, len(char) - 1)]  
            program += guess  
        print(program)
        print("Breaking pass. Please wait...")

    print(f'The password is: {program}')
        
guess_pass()


