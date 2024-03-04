from flask import Flask
import RPi.GPIO as GPIO 
app = Flask (__name__)
LEDG = 3
LEDR = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDG,GPIO.OUT)
GPIO.setup(LEDR,GPIO.OUT)
@app.route('/<color>/<opt>')
def cul(color,opt):
    if color == 'red' and opt == 'on':
        ans = color + opt
        GPIO.output (LEDR,True)
    elif color == 'red' and opt == 'off':
        ans = color + opt
        GPIO.output (LEDR,False)
    elif color == 'green' and opt == 'on':
        ans = color + opt
        GPIO.output (LEDG,True)
    elif color == 'green' and opt == 'off':
        ans = color + opt
        GPIO.output (LEDR,False)
    
    return f'ans:{ans}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
