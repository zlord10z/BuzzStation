import RPi.GPIO as GPIO
import time


class Keypad():
    GPIO.setmode(GPIO.BCM)
    cols = [21, 19, 6]
    rows = [26, 13, 5, 20]


    # Pins setup:
    for i in range(len(cols)):
        GPIO.setup(cols[i], GPIO.OUT)

    for i in range(len(rows)):
        GPIO.setup(rows[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
       

    keys = [
    ['2', '1', '3'],
    ['0', '*', '#'],
    ['8', '7', '9'],
    ['5', '4', '6']
    ]


    def check_keys(self):
        try:
            key = ""
            for i in range(len(self.cols)):
                GPIO.output(self.cols[i], GPIO.LOW)
                time.sleep(0.01)
                for j in range(len(self.rows)):
                    if not GPIO.input(self.rows[j]):
                        time.sleep(0.01)
                        if not GPIO.input(self.rows[j]):
                            key = self.keys[j][i]
                            #print(key)
                        while not GPIO.input(self.rows[j]):
                            pass
                GPIO.output(self.cols[i], GPIO.HIGH)
                time.sleep(0.01)
            return key
        except Exception as e:
            print(e)
            GPIO.cleanup()

