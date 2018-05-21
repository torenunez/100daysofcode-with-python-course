import os
import time
import datetime

# https://en.wikipedia.org/wiki/Pomodoro_Technique


def main():
    print_header()
    timer_loop()


def print_header():
    print('--------------------------------')
    print('      POMODORO TIMER APP')
    print('--------------------------------')
    print()


def timer_loop():

    print(str(datetime.datetime.now()))

    completed_tasks = 0

    option = 's'

    while option != 'q':

        print('You have completed {} tasks'.format(completed_tasks))

        option = input('Enter any key to start task timer or q to quit: ')

        if option != 'q':

            task_timer()

            completed_tasks += 1

            break_timer(completed_tasks)

    print('Exiting...')


def task_timer(task_time=25):

    print('Task timer started.')

    time.sleep(task_time)

    os.system('say "Good Work! Go have a break."')


def break_timer(completed_tasks=0):

    break_time = get_break_time(completed_tasks)
    time.sleep(break_time)

    os.system('say "Time is up! Your break is over. Get back to work!"')


def get_break_time(completed_tasks=0):

    r = completed_tasks % 4

    if r == 0:
        break_time = 30
    else:
        break_time = 5

    return break_time


if __name__ == '__main__':
    main()
