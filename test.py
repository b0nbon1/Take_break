import webbrowser
import time


def take_break():
    print('one break comes after two hours\n')
    num_breaks = int(input('how many breaks do you want?: '))
    break_duaration = int(
        input('After how many hours do you need the break?: '))
    breaks = 0
    while (num_breaks > breaks):
        uin = break_duaration
        when_to_stop = abs(int(uin))

        while when_to_stop > 0:
            m, s = divmod(when_to_stop, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + \
                str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left + "\r", end="")
            time.sleep(1)
            when_to_stop -= 1
            while when_to_stop == 0:
                accept = input("accept the break(Y/N): ")
                if accept.upper() == 'Y':
                    print("when done with break hit enter\n")
                    webbrowser.open(
                        "https://www.youtube.com/watch?v=m7Bc3pLyij0",
                        new=0, autoraise=True)
                else:
                    break
        num_breaks -= 1
    print("No more breaks for you today, Goodbye. See you again")


take_break()
