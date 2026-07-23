import time

seconds = int(input("Quantos segundos? "))

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("Acabou o tempo!")
