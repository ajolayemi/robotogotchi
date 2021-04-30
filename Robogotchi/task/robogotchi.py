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


class TheRobot:
    def __init__(self):
        self.robot_name = None
        self.battery = 100
        self.overheat = 0
        self.skills = 0
        self.boredom = 0

    def game_player(self):
        switch = {'info': self.robot_current_stats,
                  'recharge': self.recharge_robot,
                  'sleep': self.put_to_sleep,
                  'play': self.game_decider}
        self.robot_name = input('How will you call your robot?\n')
        while True:
            self.available_interactions()
            choice = input('Choose:\n')
            print()
            if choice == 'exit':
                print('Game over')
                sys.exit()

            elif choice not in switch.keys():
                print('Invalid input, try again!\n')
                continue

            else:
                switch.get(choice)()

    def available_interactions(self):
        print(f'Available interactions with {self.robot_name}:\n'
              f'exit - Exit\n'
              f'info - Check the vitals\n'
              f'recharge - Recharge\n'
              f'sleep - Sleep mode\n'
              f'play - Play\n')

    def check_on_robot(self):
        print(f'The level of overheat reached 100, {self.robot_name} '
              f'has blown up! Game over. Try again?')
        sys.exit()

    def robot_current_stats(self):
        """ Prints the current information about TheRobot
        as well as it's current vitals. """
        print(f"{self.robot_name}'s stats are:\n"
              f"battery is {self.battery},\n"
              f"overheat is {self.overheat},\n"
              f"skill level is {self.skills},\n"
              f"boredom is {self.boredom}.\n")

    def put_to_sleep(self):
        """ Puts robot to sleep. """

        if self.overheat == 0:
            print(f'{self.robot_name} is cool!\n')
        else:
            print(f'{self.robot_name} cooled off!')
            print(f"{self.robot_name}'s level of overheat was {self.overheat}."
                  f" Now it is "
                  f"{self.overheat - 20 if self.overheat - 20 > 0 else self.overheat - self.overheat}.\n")
            self.overheat = self.overheat - 20 if self.overheat - 20 > 0 else self.overheat - self.overheat
            if self.overheat == 0:
                print(f'{self.robot_name} is cool!\n')

    def recharge_robot(self):
        """ Recharges TheRobot """
        if self.battery == 100:
            print(f'{self.robot_name} is charged!\n')
        else:
            print(f"{self.robot_name}'s level of overheat was {self.overheat}."
                  f" Now it is {self.overheat - 5 if self.overheat - 5 > 0 else 0}.\n"
                  f"{self.robot_name}'s level of the battery was {self.battery}."
                  f" Now it is {self.battery + 10 if self.battery + 10 <= 100 else 100}.\n"
                  f"{self.robot_name}'s level of boredom was {self.boredom}."
                  f" Now it is {self.boredom + 5 if self.boredom + 5 <= 100 else 100}.\n"
                  f"{self.robot_name} is recharged!\n")
            self.overheat = self.overheat - 5 if self.overheat - 5 > 0 else 0
            self.battery = self.battery + 10 if self.battery + 10 <= 100 else 100
            self.boredom = self.boredom + 5 if self.boredom + 5 <= 100 else 100

    def robot_stat_after_play(self):
        possible_overheat = self.overheat + 10 if self.overheat + 10 <= 100 else 100

        if possible_overheat == 100:
            self.check_on_robot()

        else:
            print(f"{self.robot_name}'s level of boredom was {self.boredom}."
                  f" Now it is "
                  f"{self.boredom - 20 if self.boredom - 20 >= 0 else self.boredom - self.boredom}."
                  f"\n"
                  f"{self.robot_name}'s level of overheat was {self.overheat}."
                  f" Now it is "
                  f"{self.overheat + 10 if self.overheat + 10 <= 100 else 100 }")
            if self.boredom == 0:
                print(f'{self.robot_name} is in a great mood!\n')

            else:
                pass

        self.boredom = self.boredom - 20 if self.boredom - 20 >= 0 else self.boredom - self.boredom
        self.overheat = self.overheat + 10 if self.overheat + 10 else 100

    def game_decider(self):
        available_games = {'Numbers': play_number_game,
                           'Rock-paper-scissors': play_rock_game}
        while True:
            game_choice = input("Which game would you like to play?\n")
            if game_choice in available_games.keys():
                print()
                available_games.get(game_choice)()
                self.check_on_robot()
                self.robot_stat_after_play()
                break
            else:
                while True:
                    if game_choice not in available_games.keys():
                        game_choice = input('Please choose a valid option: Numbers or Rock-paper-scissors?\n')
                    else:
                        print()
                        available_games.get(game_choice)()
                        self.check_on_robot()
                        self.robot_stat_after_play()
                        break
                break


def main():
    robot_cls = TheRobot()
    robot_cls.game_player()


if __name__ == '__main__':
    main()
