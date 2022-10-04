import os
from time import sleep


def cls():
    """ clears the screen """
    os.system('cls' if os.name == 'nt' else 'clear')


cls()


def stop(is_running):
    """ handles stop """
    if not is_running:
        print_error('The car is already stop.')
        return

    print('''
          ______
         /|_||_\`.__
        (   _    _ _\\
         `-(_)--(_)-'

    ''')
    print('\tBooyay! The car stopped.')


def start(is_running):
    """ handles start """
    if is_running:
        print_error('The car is already running.')
        return

    way = 0

    while True:
        way += 1
        cls()
        car = f'''   
        {'  ' * way} ______
        {'  ' * way}/|_||_\`.__
        {'  ' * way}(   _    _ _\\
        {'==' * way}=`-(_)--(_)-'''

        print(f'''
                  {car}

            ''')
        print('\tBooyay! The car started...')
        sleep(0.28)
        if way == 12:
            break


def print_error(err):
    """ prints errors """
    print(f'\n\twarn: {err}')


def main():
    """ main function """
    print('''
                            ______  __   __   ______  ______   _____   _   _   _____  ______ 
                            | ___ \ \ \ / /   |  _  \ | ___ \ |_   _| | | | | |  ___| | ___ \\
                            | |_/ /  \ V /    | | | | | |_/ /   | |   | | | | | |__   | |_/ /
                            |  __/    \ /     | | | | |    /    | |   | | | | |  __|  |    / 
                            | |       | |_    | |/ /  | |\ \   _| |_  \ \_/ / | |___  | |\ \ 
                            \_|       \_(_)   |___/   \_| \_|  \___/   \___/  \____/  \_| \_|


                                                     ▐▀▀▀▀▀▀▀▀▀▀▀▌
                                                   ▄▄▌░░░░░░░░░░░▐▄▄
                                                  ▄▄██▄▄▄▄▄▄▄▄▄▄▄██▄▄
                                                 ▐█▄█┼┼█▓█▓█▓█▓█┼┼█▄█▌
                                                ─█▓▓█▀███_6969_███▀█▓▓─
                                                ─█▓▓█▀▀───▀▀▀▀──▀▀█▓▓█─
                                                ─█▓▓█─────────────█▓▓█─

    ''')

    print('''

            INSTRUCTIONS
            ────────────
            Type 'start' to start the car.
            Type 'stop' to stop the car.
            Type 'quit' to quit.
            Type 'instruct' to show instructions

    ''')

    # stores state of the car
    is_running = False

    # command loop
    while True:
        cmd = input('\n\t> ')
        cmd = cmd.lower().strip()
        if cmd == 'start':
            cls()
            start(is_running)
            is_running = True
        elif cmd == 'stop':
            cls()
            stop(is_running)
            is_running = False
        elif cmd == 'instruct':
            cls()
            print('''

            INSTRUCTIONS
            ────────────
            Type 'start' to start the car.
            Type 'stop' to stop the car.
            Type 'quit' to quit.
            Type 'instruct' to show instructions.

                ''')
        elif cmd == 'quit':
            if is_running:
                print_error('Can\'t quit while the car is running. Please stop the car to exit.')
                continue
            print('\n\tBye! Bye!\n')
            break
        elif cmd == '':
            continue
        else:
            print('\tInvalid Command. Try again...')


if __name__ == '__main__':
    main()
