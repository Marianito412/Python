import time

progress = "█"
left = "|"
bar = ""
piston_ver = 9
piston_hor = 2
max = 10
i = 0
for i in range(max):
    if piston_ver >= i:
        bar = bar + progress
    if piston_ver < i:
        bar = bar + left
    print(bar)
    time.sleep(1)
