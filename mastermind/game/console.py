class Console:
    #This class has the code to create a template for a computer console. The responsibility of this is to get text or numerical input and display text output.

    def read(self, prompt):
        #This function/method gets text input from the user through the screen.
        return input(prompt)

    def read_number(self, prompt):
        #This function/method gets numerical input from the user through the screen.
        return int(input(prompt))
        
    def write(self, text):
        #This function/method displays the given text on the screen. 
        print(text)

    def ask_guess(self, code_lenght):
        #This function/method asks and validates the guess received from the user
        invalid_guess = True

        while invalid_guess:

            #Creating the question
            guess = input("What is your guess? ")

            if guess.isnumeric():
                if len(guess) == code_lenght:
                    # If there is no error
                    invalid_guess = False
                    return guess
                else:
                    #Error 2: Guess is more than the code_lenght
                    self.write_error(f'My friend, your guess needs to have {code_lenght} digits')
            else:
                #Error 1: The guess contains letters
                self.write_error('My friend,your guess needs to be numeric')

    def write_error(self, text):
        #This is a very important function/method that will display the given error on the screen
        print(f'\033[1;31;40m{text}\033[0;37;40m')