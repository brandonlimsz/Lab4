from hal import hal_led as LED
import time

def blink_LED():
    LED.set_output(99,1)
    time.sleep(0.5)
    LED.set_output(99,0)
    time.sleep()


def main():
    while True:
        blink_LED()


if __name__=="__main__":
    main()