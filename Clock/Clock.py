import sys
import time
import base

try:
    while True:  # main
        print('\n' * 60)

        current_time = time.localtime()
        hours = str(current_time.tm_hour % 12)
        if hours == '0':
            hours = '12'
        minutes = str(current_time.tm_min)
        seconds = str(current_time.tm_sec)

        h_digits = base.getSevSegStr(hours, 2)
        h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

        m_digits = base.getSevSegStr(minutes, 2)
        m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()

        s_digits = base.getSevSegStr(seconds, 2)
        s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

        # Show timer
        print(h_top_row + '     ' + m_top_row + '     ' + s_top_row)
        print(h_middle_row + '     ' + m_middle_row + '     ' + s_middle_row)
        print(h_bottom_row + '     ' + m_bottom_row + '     ' + s_bottom_row)
        print()
        print('Press CTRL-C to quit')

        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != current_time.tm_sec:
                break
except KeyboardInterrupt:
    sys.exit()

