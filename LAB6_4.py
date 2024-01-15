import RPi.GPIO as GPIO
import time
SW = 14
R = 3
G = 2
B = 15
LED = [R, G ,B]
state_color = [ 0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111]
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for pin in LED:
    GPIO.setup(pin,GPIO.OUT)
def color(State):
     for i in range(2,-1,-1):
        if State & 0X01:
            GPIO.output(LED[i],1)
        else:
            GPIO.output(LED[i],0)
        State >>= 1
try:
    for pin in LED:
        GPIO.output(pin,0)
    while True:
            if GPIO.wait_for_edge(SW, GPIO.FALLING):
                count = (count + 1) % len(state_color)
                color(state_color[count])
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye…")