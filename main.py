import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# now, to clear the screen
cls()


# handles stop
def stop(is_running):
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


# handles start
def start(is_running):
    if is_running:
        print_error('The car is already running.')
        return

    print('''
          ______
         /|_||_\`.__
        (   _    _ _\\
      ===`-(_)--(_)-'

    ''')
    print('\tBooyay! The car started...')


# print errors
def print_error(err):
    print(f'\n\t{err}')


# main function
def main():
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

    ''')
    is_running = False
    while True:
        cmd = input('\n\t> ')
        cmd = cmd.lower().strip()
        if cmd == 'start':
            start(is_running)
            is_running = True
        elif cmd == 'stop':
            stop(is_running)
            is_running = False
        elif cmd == 'quit':
            print('\n\tBye! Bye!\n')
            break
        else:
            print('\tInvalid Command. Try again...')


if __name__ == '__main__':
    main()
