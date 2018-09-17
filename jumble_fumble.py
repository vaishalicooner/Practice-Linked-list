# Write your project code here
INSTRUCTIONS = """
*You will be given a Jumbled word.
*You have to guess the complete word.
*There are 10 words in total.
*For each correct answer you will get 10 points.
*You can use hint, but it will reduce your score by 2.
*Each wrong answer will reduce your score by 1.
*Each skip will reduce your score by 1.
*[H]int.
*[S]kip the word.
*[B]egin the game.
*[E]xit the game.
"""

data = [
    {'jword': 'OOTSPFTES', 'answer': 'FOOTSTEPS', 'hint': ['THE MORE YOU TAKE, THE MORE YOU LEAVE BEHIND.', 'A STEP TAKEN BY A PERSON IN WALKING.']},
    {'jword': 'ECACRAR', 'answer': 'RACECAR', 'hint': ['WORD IS SPELLED THE SAME WAY BACKWARDS AND FORWARDS.','SOMETHING THAT COMPETES IN RACES.']},
    {'jword': 'BTEAHPAL', 'answer': 'ALPHABET', 'hint': ['WORD CONTAINS ALL OF THE 26 LETTERS.','A SET OF LETTERS']},
    {'jword': 'CACIOGH', 'answer': 'CHICAGO', 'hint': ['3/7 CHICKEN, 2/3 CAT, 2/4 GOAT.',"IT'S A NAME OF A CITY."]},
    {'jword': 'SSLLEDEIMP', 'answer': 'MISSPELLED', 'hint': ['ONE WORD IN THIS SENTENCE IS MISSPELLED.', 'SPELLED INCORRECTLY']},
    {'jword': 'ESLIECN', 'answer': 'SILENCE', 'hint': ["SAY MY NAME AND I'M NO MORE.",'COMPLETE ABSENCE OF SOUND']},
    {'jword': 'GAYRNUH', 'answer': 'HUNGARY', 'hint': ['WHAT COUNTRY WOULD SEND A MAN TO FOR HIS APPETITE.', " IT'S A COUNTRY IN EUROPE."]},
    {'jword': 'VENPOELE', 'answer': 'ENVELOPE', 'hint': ['WORD BEGINS AND ENDS WITH E BUT ONLY HAS 1 LETTER.'," A FLAT PAPER CONTAINER WITH A SEALABLE FLAP."]},
    {'jword': 'SHMUOORM', 'answer': 'MUSHROOM', 'hint': ["A ROOM WITH NO DOORS AND WINDOWS", "IT'S A VEGETABLE."]},
    {'jword': 'DAHSOW', 'answer': 'SHADOW',
     'hint': ['THEY ARE DARK, AND ALWAYS ON RUN, WITHOUT THE SUN WOULD BE NONE.', "PARTIAL DARKNESS DUE TO OBSTRUCTION OF LIGHT RAYS."]}]



def greet_user():
  """ defining a function to ask username and greet the user."""
  print("-------Welcome!-------")
  name = input("What is your name ? ")
  print("Hello {}, Good to see you here!".format(name.capitalize()))
  print("Read the instructions carefully and start your game!")


score = 0  # initializing score to zero.




def evaluate(entry, i, challenge, hintcount):
    """ defining a function to calculate the score in all different cases like: wrong answer, using hint or skipping a question."""
    global score

    if entry == data[i]['answer']:
        score = score + 10
        print()
        print('Correct answer! Your SCORE is {}'.format(score))
        print("----------------------------------")
        challenge = False
        return [challenge, hintcount]

    elif entry == 'H':
        print()
        if hintcount == 0:
            print('Hint:{}'.format(data[i]['hint'][0]))
            hintcount = hintcount + 1
            score = score - 2

        elif hintcount == 1:
            print('Hint:{}'.format(data[i]['hint'][1]))
            hintcount = hintcount + 1
            score = score - 2

        elif hintcount > 1:
            print('You have used all the hints!')

        print()
        print('Used a hint! Your SCORE is {}'.format(score))
        print("----------------------------------")
        challenge = True
        return [challenge, hintcount]

    elif entry == 'E':
        print()
        print('Thanks for playing! Your SCORE is {}'.format(score))
        myexit()

    elif entry == 'S':
        score = score - 1
        print()
        print('Moving to next question! Your SCORE is {}'.format(score))
        print("----------------------------------")
        challenge = False
        return [challenge, hintcount]

    else:
        score = score - 1
        print()
        print('Wrong answer! Your SCORE is {}'.format(score))
        print("----------------------------------")
        challenge = True
        return [challenge, hintcount]


def myexit():
    print("Goodbye!")
    exit()


def play_game():
    """A function as main function for game."""
    greet_user()
    """Calling the function to greet the user """
    
    instruct = INSTRUCTIONS
    """ print instructions for the user."""
    print(instruct)
    # Ask user whether they want to continue or exit.
    while True:
      begin = input("Type begin or b to begin the game and e to exit the game:")
      begin = begin.lower()
      import time
      if begin == "begin" or begin == "b":
        print("YOUR GAME IS LOADING!")
        timer = 5  # setting timer for game loading
        while timer > 0:
          print(timer, "...")
          time.sleep(1)
          timer = timer - 1

        print("***START***")

        print("GOOD LUCK!")
            # looping words
        for i in range(len(data)):
          challenge = True
          hintcount = 0
          while challenge:
            print()
            print('Your challenge word is:{}'.format(data[i]['jword']))
            entry = input('Enter your guess:')
            entry = entry.upper()
            result = evaluate(entry, i, challenge, hintcount)
            challenge = result[0]
            hintcount = result[1]
            print()
        print("GAMEOVER!")
        print('Thanks for playing! Your SCORE is {}'.format(score))
        print()
      elif begin == "e" or begin == "exit":
        myexit()
      else:
        print("Choose to start or exit:")


play_game()

