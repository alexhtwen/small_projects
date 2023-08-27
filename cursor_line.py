import time

def rand_draw():
    CURSOR_UP = '\033[1A'
    CLEAR = '\x1b[2K'
    CLEAR_LINE = CURSOR_UP + CLEAR
    # time.sleep(1)
    while True:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)


        print('1234567890'*5)
        time.sleep(2)
        print('.', end='')
        time.sleep(2)
        print(f'AB{CURSOR_UP*2}XY', end='')
        # print('AB')
        # time.sleep(2)
        print()

rand_draw()
