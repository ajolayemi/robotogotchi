import random
import sys

MIN = 0
MAX = 1000000

RULES = {'rock': 'scissors',
         'paper': 'rock',
         'scissors': 'paper'}

DANGEROUS_SUBSTANCES = {'puddle': 10,
                        'sprinkler': 30,
                        'swimming pool': 50,
                        'lucky': 0}


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
                  f"Draws: {stats.get('Draws')}.\n")
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
            print('A string is not a valid input!\n')


class TheRobot:
    def __init__(self):
        self.robot_name = None
        self.battery = 100
        self.overheat = 0
        self.skills = 0
        self.boredom = 0
        self.rust = 0

    def game_player(self):
        switch = {'info': self.robot_current_stats,
                  'recharge': self.recharge_robot,
                  'sleep': self.put_to_sleep,
                  'play': self.game_decider,
                  'oil': self.oil_robot,
                  'learn': self.learn,
                  'work': self.work,
                  }
        self.robot_name = input('How will you call your robot?\n')
        while True:

            if self.overheat == 100:
                self.check_on_robot(overheated=True)

            if self.rust == 100:
                self.check_on_robot(rusted=True)

            self.available_interactions()
            choice = input('Choose:\n')
            print()
            if choice == 'exit':
                print('Game over')
                sys.exit()

            elif choice not in switch.keys():
                print('Invalid input, try again!\n')
                continue

            elif self.battery == 0 and choice != 'recharge':
                self.check_on_robot(low_battery=True)

            elif self.boredom == 100 and choice != 'play':
                self.check_on_robot(bored=True)

            else:
                switch.get(choice)()

    def available_interactions(self):
        print(f'Available interactions with {self.robot_name}:\n'
              f'exit - Exit\n'
              f'info - Check the vitals\n'
              f'work - Work\n'
              f'play - Play\n'
              f'oil - Oil\n'
              f'recharge - Recharge\n'
              f'sleep - Sleep mode\n'
              f'learn - Learn skills\n')

    def check_on_robot(self, overheated=False, rusted=False, low_battery=False,
                       bored=False):
        """ Checks on robot's vitals among which:\n
        1. overheat_level, if the robot is overheated, it informs the user of such
        and exits the program.\n
        2. rust level, if the robot is too rust, it informs user of such and exits
        the program.\n
        3. battery level, checks to see that robots battery level <= 0 \n
        4. boredom level, keeps track of robots boredom level"""
        if overheated:
            print(f'The level of overheat reached 100, {self.robot_name} '
                  f'has blown up! Game over. Try again?')
            sys.exit()

        elif rusted:
            print(f'{self.robot_name} is too rusty! Game over. Try again?')
            sys.exit()

        elif low_battery:
            print(f'The level of the battery is 0, {self.robot_name} needs recharging!\n')

        elif bored:
            print(f'{self.robot_name} is too bored! {self.robot_name} needs '
                  f'to have fun!\n')

    def oil_robot(self):
        """ Oil robot decreasing it's level of rust. """
        new_rust = self.rust - 20 if self.rust - 20 >= 0 else 0

        if self.rust == 0:
            print(f'{self.robot_name} is fine, no need to oil!\n')
        else:
            print(f"{self.robot_name}'s level of rust was {self.rust}. "
                  f"Now it is {new_rust}. {self.robot_name} is less rusty!\n")
            self.rust = new_rust

    def work(self):

        new_battery = self.battery - 10 if self.battery - 10 > 0 else self.battery - self.battery
        new_overheat = self.overheat + 10 if self.overheat + 10 <= 100 else 100
        new_boredom = self.boredom + 10 if self.boredom + 10 <= 100 else 100
        if self.skills < 50:
            print(f'{self.robot_name} has got to learn before working!\n')
        else:
            random_mishap = random.choice(list(DANGEROUS_SUBSTANCES.keys()))
            if random_mishap == 'lucky':
                print(f"{self.robot_name}'s level of overheat was {self.overheat}. "
                      f"Now it is {new_overheat}.\n"
                      f"{self.robot_name}'s level of boredom was {self.boredom}. "
                      f"Now it is {new_boredom}.\n"
                      f"{self.robot_name}'s level of the battery was {self.battery}. "
                      f"Now it is {new_battery}. \n"
                      f"\n"
                      f"{self.robot_name} did well!\n")
            else:
                deducted = DANGEROUS_SUBSTANCES.get(random_mishap)
                new_rust = self.rust + deducted if self.rust + deducted <= 100 else 100
                if random_mishap == 'puddle':
                    print(f'Oh no, {self.robot_name} stepped into a puddle!\n')
                elif random_mishap == 'sprinkler':
                    print(f'Oh, {self.robot_name} encountered a sprinkler!\n')
                else:
                    print(f'Guess what! {self.robot_name} fell into the pool!\n')

                print(f"{self.robot_name}'s level of overheat was {self.overheat}. "
                      f"Now it is {new_overheat}.\n"
                      f"{self.robot_name}'s level of boredom was {self.boredom}. "
                      f"Now it is {new_boredom}.\n"
                      f"{self.robot_name}'s level of the battery was {self.battery}. "
                      f"Now it is {new_battery}. \n"
                      f"{self.robot_name}'s level of rust was {self.rust}. "
                      f"Now it is {new_rust}.\n"
                      f"\n"
                      f"{self.robot_name} did well!\n")
                self.rust = new_rust

            self.overheat = new_overheat
            self.boredom = new_boredom
            self.battery = new_battery

    def learn(self):
        """ Helps robot acquire new skills. """
        new_skills = self.skills + 10 if self.skills + 10 <= 100 else 100
        new_battery = self.battery - 10 if self.battery - 10 >= 0 else self.battery - self.battery
        new_overheat = self.overheat + 10 if self.overheat + 10 <= 100 else 100
        new_boredom = self.boredom + 5 if self.boredom + 5 <= 100 else 100

        if self.skills == 100:
            print(f"There's nothing for {self.robot_name} to learn!")
        else:
            print(f"{self.robot_name}'s level of skill was {self.skills}. "
                  f"Now it is {new_skills}.\n"
                  f"{self.robot_name}'s level of overheat was {self.overheat}. "
                  f"Now it is {new_overheat}.\n"
                  f"{self.robot_name}'s level of the battery was {self.battery}. "
                  f"Now it is {new_battery}.\n"
                  f"{self.robot_name}'s level of boredom was {self.boredom}. "
                  f"Now it is {new_boredom}.\n\n"
                  f"{self.robot_name} has become smarter!\n")
            self.skills = new_skills
            self.battery = new_battery
            self.overheat = new_overheat
            self.boredom = new_boredom

    def robot_current_stats(self):
        """ Prints the current information about TheRobot
        as well as it's current vitals. """
        print(f"{self.robot_name}'s stats are:\n"
              f"battery is {self.battery},\n"
              f"overheat is {self.overheat},\n"
              f"skill level is {self.skills},\n"
              f"boredom is {self.boredom},\n"
              f"rust is {self.rust}.\n")

    def put_to_sleep(self):
        """ Puts robot to sleep. """
        new_overheat = self.overheat - 20 if self.overheat - 20 > 0 else self.overheat - self.overheat

        if self.overheat == 0:
            print(f'{self.robot_name} is cool!\n')
        else:
            print(f"{self.robot_name}'s level of overheat was {self.overheat}."
                  f" Now it is "
                  f"{new_overheat}.\n")
            print(f'{self.robot_name} cooled off!')
            self.overheat = new_overheat
            if self.overheat == 0:
                print(f'{self.robot_name} is cool!\n')

    def recharge_robot(self):
        """ Recharges TheRobot """
        new_overheat = self.overheat - 5 if self.overheat - 5 > 0 else 0
        new_battery = self.battery + 10 if self.battery + 10 <= 100 else 100
        new_boredom = self.boredom + 5 if self.boredom + 5 <= 100 else 100
        if self.battery == 100:
            print(f'{self.robot_name} is charged!\n')
        else:
            print(f"{self.robot_name}'s level of overheat was {self.overheat}."
                  f" Now it is {new_overheat}.\n"
                  f"{self.robot_name}'s level of the battery was {self.battery}."
                  f" Now it is {new_battery}.\n"
                  f"{self.robot_name}'s level of boredom was {self.boredom}."
                  f" Now it is {new_boredom}.\n"
                  f"{self.robot_name} is recharged!\n")
            self.overheat = new_overheat
            self.battery = new_battery
            self.boredom = new_boredom

    def robot_stat_after_play(self):
        new_overheat = self.overheat + 10 if self.overheat + 10 <= 100 else 100
        new_boredom = self.boredom - 20 if self.boredom - 20 >= 0 else self.boredom - self.boredom

        if new_overheat == 100:
            self.check_on_robot(overheated=True)
        else:
            random_mishap = random.choice(list(DANGEROUS_SUBSTANCES.keys()))
            if random_mishap == 'lucky':
                print(f"{self.robot_name}'s level of boredom was {self.boredom}."
                      f" Now it is {new_boredom}.\n"
                      f"{self.robot_name}'s level of overheat was {self.overheat}."
                      f" Now it is {new_overheat}.\n")
            else:
                if random_mishap == 'puddle':
                    print(f'Oh no, {self.robot_name} stepped into a puddle!\n')
                elif random_mishap == 'sprinkler':
                    print(f'Oh, {self.robot_name} encountered a sprinkler!\n')
                else:
                    print(f'Guess what! {self.robot_name} fell into the pool!\n')
                deducted = DANGEROUS_SUBSTANCES.get(random_mishap)
                new_rust = self.rust + deducted if self.rust + deducted <= 100 else 100
                print(f"{self.robot_name}'s level of rust was {self.rust}. "
                      f"Now it is {new_rust}. \n"
                      f"{self.robot_name}'s level of boredom was {self.boredom}."
                      f" Now it is {new_boredom}.\n"
                      f"{self.robot_name}'s level of overheat was {self.overheat}."
                      f" Now it is {new_overheat}.\n")
                self.rust = new_rust
            self.boredom = new_boredom
            self.overheat = new_overheat

        if new_boredom == 0:
            print(f'{self.robot_name} is in a great mood!\n')

        else:
            pass

    def game_decider(self):
        available_games = {'Numbers': play_number_game,
                           'Rock-paper-scissors': play_rock_game}
        while True:
            game_choice = input("Which game would you like to play?\n")
            if game_choice.capitalize() in available_games.keys():
                print()
                available_games.get(game_choice.capitalize())()
                self.check_on_robot()
                self.robot_stat_after_play()
                break
            else:
                while True:
                    if game_choice.capitalize() not in available_games.keys():
                        game_choice = input('Please choose a valid option: Numbers or Rock-paper-scissors?\n')
                    else:
                        print()
                        available_games.get(game_choice.capitalize())()
                        self.check_on_robot()
                        self.robot_stat_after_play()
                        break
                break


def main():
    robot_cls = TheRobot()
    robot_cls.game_player()


if __name__ == '__main__':
    main()
