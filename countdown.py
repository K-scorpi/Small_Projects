import sys
import time
import base

# Can replace for any seconds
secondsLeft = 1000

try:
    while True:  # main cycle
        print('\n' * 60)

        # hours/minutes/seconds
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        h_digits = base.getSevSegStr(hours, 2)
        h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

        m_digits = base.getSevSegStr(minutes, 2)
        m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()

        s_digits = base.getSevSegStr(seconds, 2)
        s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

        # Show numerical
        print(h_top_row + '     ' + m_top_row + '     ' + s_top_row)
        print(h_middle_row + '     ' + m_middle_row + '     ' + s_middle_row)
        print(h_bottom_row + '     ' + m_bottom_row + '     ' + s_bottom_row)

        if secondsLeft == 0:
            print()
            print('     * * * * FINISH * * * *')
            break

        print()
        print('Press CTRL-C to quit')

        time.sleep(1)
        secondsLeft -= 1
except KeyboardInterrupt:
    sys.exit()
