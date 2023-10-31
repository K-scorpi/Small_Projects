import time, sys

try:
    import bext
except ImportError:
    sys.exit()

print('RainBow')
print('Press Ctrl-C to stop')
time.sleep(3)

space = 0
spaceIncreasing = True

try:
    while True:  # Main cycle
        print(' ' * space, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if spaceIncreasing:  # add number of space
            space += 1
            if space == 60:  # 10 or 30 // and change rotation
                spaceIncreasing = False
        else:  # mines number of space
            space -= space
            if space == 0:  # change rotation
                spaceIncreasing = True

        time.sleep(0.02)  # small pause

except KeyboardInterrupt:
    sys.exit()  # If punch button Ctrl+C // stop programm
