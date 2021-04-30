import random

MIN = 0
MAX = 1000000


def play_game():
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


if __name__ == '__main__':
    play_game()
