import time

def count_down(t):
    prev_len = 0
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\b' * prev_len + timer, end='', flush=True)
        prev_len = len(timer)
        time.sleep(1)
        t -= 1
    print("\nLets Go!")

t = input("Enter the time in seconds: ")
count_down(int(t))