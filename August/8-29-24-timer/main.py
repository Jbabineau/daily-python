import time
# get the user input in seconds
timer_length = "a"
while not timer_length.isdecimal():
    timer_length = input("Enter the time in seconds:")

waited_time = 0.00
timer_length = int(timer_length)
while waited_time < int(timer_length):
    time.sleep(1)
    print(f"{timer_length - waited_time}")
    waited_time = waited_time + 1

print("Time's Up\a")