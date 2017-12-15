def valid_time(t):
    # check if the time format is correct
    try:
        h = int(t.split(":")[0])
        m = int(t.split(":")[1])
        s = int(t.split(":")[2])
        if h < 0 or m < 0 or s < 0:
            return False
        if h > 23:
            return False
        elif m > 59 or s > 59:
            return False
        return [s % 2 == 0, h // 5, h % 5, m // 5, m % 5]
    except:
        return False


def berlin_clock(time):
    print("\n### Berlin Clock ###\n")
    print("-----\nEntered time: {}".format(time))
    vt = valid_time(time)
    if vt:
        if vt[0]:
            print('Y')
        else:
            print('O')
        print(vt[1]*'R' + (4-vt[1])*'O')
        print(vt[2]*'R' + (4-vt[2])*'O')
        l_line = list(vt[3]*'Y' + (11-vt[3])*'O')
        if l_line[2] == 'Y':
            l_line[2] = 'R'
        if l_line[5] == 'Y':
            l_line[5] = 'R'
        if l_line[8] == 'Y':
            l_line[8] = 'R'
        print("".join(l_line))
        print(vt[4]*'Y' + (4-vt[4])*'O')
    else:
        print("Wrong time format! Use this one hh:mm:ss")
    print("-----")


def simple_berlin_clock(time):
    # simple version
    print("\n\n---Simple version---")
    print("\nEntered time: {}".format(time))
    vt = valid_time(time)
    if vt:
        for i in vt:
            print(i * '|#|')
    else:
        print("Wrong time format! Use this one hh:mm:ss")
    print("-----")


def current_time_berlin_clock():
    # current time version
    print("\n\n---Current time version---")
    import datetime
    cur_time = datetime.datetime.now()
    print("\nCurrent time is: {}:{}:{}".format(cur_time.hour, cur_time.minute, cur_time.second))
    vt = valid_time(cur_time.strftime("%H:%M:%S"))
    for i in vt:
        print(int(i) * '|#|')
    print("-----")


def main():
    time = "17:15:57"
    berlin_clock(time)
    simple_berlin_clock(time)
    current_time_berlin_clock()


main()

