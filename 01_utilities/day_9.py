"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time
import winsound # for beep sound

while True:
    try:
        seconds =int(input(" ⏰ Enter the time in seconds: "))
        if seconds <= 0:
            print("Please enter a number greater than zero.")
            continue
        else:
            break
    except ValueError:
        print("Invalid input, please enter a whole number")

print("\n Timer started! 🕐")
for remaining in range(seconds, -1, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}" # 02 signifies 2 digits
    print(f" 🕰️ Time remaining: {time_format}", end="\r") # \r sends the cursor back to the start of the line.
    time.sleep(1) # sleep for 1 second

print("\n Time's up! 🔔 Take a break or move on to next task.")    
print("\a")  # Beep sound (not supported on all terminals)

for _ in range(10):
    winsound.Beep(1200, 500) # Beep sound (optional) 

#  ⏰ Enter the time in seconds: 70

#  Timer started! 🕐
#  🕰️ Time remaining: 00:00
#  Time's up! 🔔 Take a break or move on to next task.    