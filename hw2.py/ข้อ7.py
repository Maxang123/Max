import time
t_start = time.time()
empty= []
def krn(z,p):
    for fool_number in range(137690,1,-1):
        if z % fool_number == 0 and p % fool_number == 0:
            empty.append(fool_number)
    print(empty)
krn(137690,298)
t_end = time.time()
duration = t_end - t_start
print(duration)



