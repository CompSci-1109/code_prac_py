import time

my_time= int(input("Enter the time you want to start from in seconds: "))

for x in reversed(range(0, my_time +1 )): #+1 includes the input no. too in the output bcos the last limit is often ignored.
     seconds= x % 60
     minutes= int(x/60) % 60
     hours= int(x / 3600)
     print(f"{hours:02}:{minutes:02}:{seconds:02}")
     time.sleep(1)
print("HAPPY NEW YEAR!!🥳🥳💃")