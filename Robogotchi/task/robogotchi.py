import random
import sys

MIN = 0
MAX = 1000000

RULES = {'rock': 'scissors',
         'paper': 'rock',
         'scissors': 'paper'}


def play_rock_game():
    stats = {"User": 0,
             "Robot": 0,
             "Draws": 0}
    while True:
        user_weapon = input('What is your move?\n')
        robot_weapon = random.choice(list(RULES.keys()))
        if user_weapon == 'exit game':
            print()
            print(f"You won: {stats.get('User')},\n"
                  f"The robot won: {stats.get('Robot')}, \n"
                  f"Draws: {stats.get('Draws')}.")
            break
        elif user_weapon not in RULES.keys():
            print('No such option! Try again!')

        else:
            print(f'The robot chose {robot_weapon}')
            if user_weapon == robot_weapon:
                print("It's a draw!\n")
                stats['Draws'] += 1
            elif robot_weapon == RULES.get(user_weapon):
                print('You won!\n')
                stats['User'] += 1

            elif user_weapon == RULES.get(robot_weapon):
                print('The robot won!\n')
                stats['Robot'] += 1


def play_number_game():
    stats = {"User": 0,
             "Robot": 0,
             "Draws": 0}
    while True:
        random_num = random.randint(MIN, MAX)
        robot_num = random.randint(MIN, MAX)
        user_num = input('What is your number?\n')
        if user_num == 'exit game':
            print()
            print(f"You won: {stats.get('User')},\n"
                  f"The robot won: {stats.get('Robot')}, \n"
                  f"Draws: {stats.get('Draws')}.")
            break

        if user_num[0] == '-':
            print("The number can't be negative!\n")

        elif user_num.isnumeric():

            if int(user_num) > MAX:
                print(f"Invalid input! The number can't be bigger "
                      f"than {MAX}\n")
            else:
                print(f'The robot entered the number {robot_num}.')
                print(f'The goal number is {random_num}.')
                if abs(random_num - int(user_num)) < abs(random_num - robot_num):
                    print('You won!\n')
                    stats["User"] += 1
                elif abs(random_num - int(user_num)) > abs(random_num - robot_num):
                    print('The robot won!\n')
                    stats['Robot'] += 1
                elif all((robot_num in range(random_num), int(user_num) in range(random_num),
                          random_num == int(user_num))):
                    print("It's a draw!\n")
                    stats['Draws'] += 1
        else:
            print('A string is not a valid input!')


def main():
    available_games = {'Numbers': play_number_game,
                       'Rock-paper-scissors': play_rock_game}
    while True:
        game_choice = input("Which game would you like to play?\n")
        if game_choice in available_games.keys():
            available_games.get(game_choice)()
            sys.exit()
        else:
            while True:
                if game_choice not in available_games.keys():
                    game_choice = input('Please choose a valid option: Numbers or Rock-paper-scissors?\n')
                else:
                    available_games.get(game_choice)()
                    sys.exit()




if __name__ == '__main__':
    main()
