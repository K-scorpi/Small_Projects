def getSevSegStr(num, minWidth=0):
    num = str(num).zfill(minWidth)
    rows = ['', '', '']
    for i, numeral in enumerate(num):
        if numeral == '.':  # Write point
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue
        elif numeral == '-':  # Write mines
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':  # Write null
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':  # Write 1
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':  # Write 2.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':  # Write 3.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':  # Write 4.
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':  # Write 5.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':  # Write 6.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':  # Write 7.
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':  # Write 8.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':  # Write 9.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'
        if i != len(num) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
    return '\n'.join(rows)


if __name__ == '__main__':
    # example
    myNumber = getSevSegStr(42, 3)
    print(myNumber)
