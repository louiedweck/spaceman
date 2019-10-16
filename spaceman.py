import random


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('/usr/share/dict/words', 'r')
    words_list = f.read().splitlines()
    f.close()

    # comment this line out if you use a words.txt file with each word on a new line
    # words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

        'hello'
        ['f', 'e', 't', 'l']

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # create an array with blanks ('_') of size of secret word
    blanks = ['_'] * len(secret_word)
    # iterate through the letters in letters_guessed
    for letter in letters_guessed:
        # check if the guess is in the word
        if is_guess_in_word(letter, secret_word):
            # if so we should find the indicies where the letter appears in the secret word
            indicies = find_indicies(secret_word, letter)
            # Go through the indicies in our index list
            for index in indicies:
                # update blanks with the letter at those indicies
                blanks[index] = letter
    # return a string version of our blanks list
    return ''.join(blanks)


def find_indicies(word, target):
    '''
    A function that iterates through a string called word and returns an array of indicies where a target (letter) appears.

    Args:
        word (string): the word we're searching through
        target (string): the letter we're searching for

    Returns:
        array of integers. These are the positions (indicies) of the letter in our word.
     '''

    #  create an empty array of indicies
    indicies = []
    # go over every index of the word
    for i in range(len(word)):
        # check if the word at that index equals the taget
        if word[i] == target:
            # if so add that index to our indicies list
            indicies.append(i)
    # return our list of indicies
    return indicies


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    if guess in secret_word:
        # if so return True
        return True
    # otherwise (guess not in secret_word)
    else:
        return False


def handle_input(prompt):

    # ask the user for an input and save it to user_input
    user_input = input(prompt).lower()
    # while the user input has a length not equal one or the input is not a letter
    while len(user_input) != 1 or not user_input.isalpha():
        # ask the user for a new input
        user_input = input('Invalid input, please enter one letter: ')
    return user_input


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.
    '''
    secret_word = secret_word
    print("\n------------------------------------\n")
    print('Wecome to Spaceman! Here are your blanks: ')
    print('_' * len(secret_word))
    print()

    lives = 7
    letters_guessed = []
    # while the secret word hasnt been guessed and lives are greater than 0 we continue to run the game
    while not is_word_guessed(secret_word, letters_guessed) and lives > 0:
        # prompt the user for a guess
        guess = handle_input('Enter a letter: ')
        # add the guess to letters_guessed
        letters_guessed.append(guess)
        # check if the guess is in the secret word
        if is_guess_in_word(guess, secret_word):
            # if so let the user know they answered correctly!
            print('Congrats! The letter ' + guess + ' was found!')
        # otherwise, the user guessed incorrectly
        else:
            lives -= 1
            # tell the user they were wrong
            print('Boohoo! The letter ' + guess + ' was not found!')
        # tell the user how many lives they have
        print('You have ' + str(lives) + ' lives left.')
        # show the user their guesses
        print('Letters guessed: ' + ', '.join(letters_guessed))
        # show the user the current word
        print(get_guessed_word(secret_word, letters_guessed))
        print()
    # check if lives is greater than 0 to see if the user won
    if lives > 0:
        # the user won! congradulate them.
        print('Congratulations! You win! You only used ' +
              str(7 - lives) + ' lives!')
    # otherwise, the player lost
    else:
        # tell the user they lost and tell them what the word was
        print('Too bad so sad! You lose! The word was: ' + secret_word)


if __name__ == '__main__':
    continue_playing = True
    while continue_playing:
        # These function calls that will start the game
        secret_word = load_word()
        spaceman(secret_word)
        yes_or_no = input('Type q to quit or anything else to play again: ')
        if yes_or_no == 'q' or yes_or_no == 'Q':
            continue_playing = False
