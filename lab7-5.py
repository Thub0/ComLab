import drivers
import RPi.GPIO as GPIO
from time import sleep
my_array = ["Lab 7"," Lab 7","  Lab 7","   Lab 7","    Lab 7",\
    "     Lab 7","      Lab 7","       Lab 7","        Lab 7",\
        "         Lab 7","          Lab 7","           Lab 7"]
SW1 = 17 
SW2 = 27
i = 0
lcd_position = 0

display = drivers.Lcd()
display.lcd_clear()
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)


try:
    while True:
        if GPIO.event_detected(SW1):
            i += 1
            display.lcd_clear()
            display.lcd_display_string(my_array[i], 1)
            if(i == 11):
                i = 10  
        elif GPIO.event_detected(SW2):
            i -= 1
            display.lcd_clear()
            display.lcd_display_string(my_array[i], 1)
            if(i == 0):
                i = 1
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye...")
