import time

def pause():
    for i in range(10, 0, -1):
        print(f"The program will end in {i}..")
        time.sleep(1)

pause()

def current_time():
    t = time.strftime("%I:%M %p")  # 12-hour format with AM/PM
    return t

print(current_time())

def current_date():
    d = time.strftime("%b %d %Y")  # e.g. Mar 24 2026
    return d

print(current_date())
