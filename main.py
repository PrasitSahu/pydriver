import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# now, to clear the screen
cls()


# handles stop
def stop():
    if not car['is_running']:
        print_error('The car is already stop.')
        return

    print('''
          ______
         /|_||_\`.__
        (   _    _ _\\
         `-(_)--(_)-'

    ''')
    car['is_running'] = False
    print('\tBooyay! The car stopped.')


# handles start
def start():
    if car['is_running']:
        print_error('The car is already running.')
        return

    print('''
          ______
         /|_||_\`.__
        (   _    _ _\\
      ===`-(_)--(_)-'

    ''')
    car['is_running'] = True
    print('\tBooyay! The car started...')


# print errors
def print_error(err):
    print(f'\n\t{err}')


# main function
def main():
    while True:
        cmd = input('\n\t> ')
        cmd = cmd.lower().strip()
        if cmd == 'start':
            start()
        elif cmd == 'stop':
            stop()
        elif cmd == 'quit':
            print('\n\tBye! Bye!\n')
            break
        else:
            print('\tInvalid Command. Try again...')


print('''
                         _____   _   _   _____   ______  ______   _____   _   _   _____  ______ 
                        |_   _| | | | | |  ___|  |  _  \ | ___ \ |_   _| | | | | |  ___| | ___ \\
                          | |   | |_| | | |__    | | | | | |_/ /   | |   | | | | | |__   | |_/ /
                          | |   |  _  | |  __|   | | | | |    /    | |   | | | | |  __|  |    / 
                          | |   | | | | | |____  | |/ /  | |\ \   _| |_  \ \_/ / | |___  | |\ \ 
                          \_/   \_| |_/ \____(_) |___/   \_| \_|  \___/   \___/  \____/  \_| \_|


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

car = {
    'is_running': False,
}

main()
