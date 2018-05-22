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

    start_time = datetime.datetime.now()

    print('Welcome to Pomodoro Timer! It is currently {}.'.format(
        start_time.strftime("%A, %B %d %Y %H:%M:%S")
    ))

    print()


def timer_loop():

    completed_tasks = 0

    option = 's'

    while option != 'q':

        print()
        print('You have completed {} tasks'.format(completed_tasks))

        option = input('Enter any key to start task timer or q to quit: ')

        if option != 'q':

            task_timer()

            completed_tasks += 1

            break_timer(completed_tasks)

    print('Exiting...')


def task_timer(task_time=25):

    task_end = datetime.datetime.now() + datetime.timedelta(minutes=task_time)

    print('Task timer started. You have until {} to finish your task.'.format(
        task_end.strftime("%A, %B %d %Y %H:%M:%S")
    ))

    time.sleep(task_time*60)

    task_end_message = "Task time is up! Good Work! Go have a break."

    print(task_end_message)

    os.system('say "{}" '.format(task_end_message))


def break_timer(completed_tasks=0):

    break_time = get_break_time(completed_tasks)

    break_end = datetime.datetime.now() + datetime.timedelta(minutes=break_time)

    print('Break timer started. You have until {} for your break.'.format(
        break_end.strftime("%A, %B %d %Y %H:%M:%S")
    ))

    time.sleep(break_time*60)

    break_end_message = "Break time is up! Your break is over. Get back to work!"

    print(break_end_message)

    os.system('say "{}" '.format(break_end_message))


def get_break_time(completed_tasks=0):

    r = completed_tasks % 4

    if r == 0:
        break_time = 30
    else:
        break_time = 5

    return break_time


if __name__ == '__main__':
    main()
