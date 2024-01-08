from machine import Pin
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

count = 0

while count < 10:
    print(count)
    red.value(1)
    time.sleep(.5)
    red.value(0)
    amber.value(1)
    time.sleep(.5)
    amber.value(0)
    green.value(1)
    time.sleep(.5)
    green.value(0)
    count += 1

time.sleep(5)

red.value(0)
amber.value(0)
green.value(0)