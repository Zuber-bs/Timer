import time
from winsound import MB_ICONQUESTION

counter = 0
secs = int(input("Enter number of seconds: "))

def countdownTimer(secs):
    while secs > 0:
        mins = int(secs/60)
        seconds = int(secs%60)
        timer = f'{mins}:{seconds}'   

        time.sleep(1)
        secs-=1
        print(timer)
    print("Time Up!")

countdownTimer(secs)