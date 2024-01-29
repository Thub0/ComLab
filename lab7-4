import RPi.GPIO as GPIO
from time import sleep

SW1 = 17 
SW2 = 27

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
            lcd_position += 1
            if lcd_position == 1:
                display.lcd_clear()
                display.lcd_display_string("Sorawit srisun", 1)
                display.lcd_display_string("116510400525-1", 2)
            elif lcd_position == 2:
                display.lcd_clear()
                display.lcd_display_string("Chatdanai", 1)
                display.lcd_display_string("116510462029-9", 2)
            elif lcd_position == 3:
                display.lcd_clear()
                display.lcd_display_string("Sirachat", 1)
                display.lcd_display_string("116510462043-0", 2)
                lcd_position = 0
        elif GPIO.event_detected(SW2):
            display.lcd_clear()
            GPIO.cleanup()
            print("\nBye...")
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye...")
