import RPi.GPIO as GPIO
from time import sleep

#setting something as BCM
GPIO.setmode(GPIO.BCM)
#and turn of warnings
GPIO.setwarnings(False)




class Motor():
    #Pyton constructor with 3 arguments to set pins on the rpi
    def __init__(self, Enable, input1, input2):
        self.ena = Enable
        self.in1 = input1
        self.in2 = input2
        #Set Rpi IO-pins to output with an unknown function/method
        GPIO.setup(self.ena,GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        #setting PWM function to pin number and value
        self.PWMA = GPIO.PWM(self.ena, 100);
        self.PWMA.start(0);

    def moveForward(self,speed = 50, time=0):
        self.PWMA.changeDutyCycle(speed)
        #Set pins to high or low
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.outpu(self.in2, GPIO.HIGH)
        sleep(time)
    def stopMotor(self, time =0):
        self.PWMA.changeDutyCycle(0)
        sleep(time)


#create main function to run if this file is run alone
main()

#Create a motor from motor class and set pin numbers
motor1 = Motor(1,2,3)

#run function moveForward
motor1.moveForward(70,5)
#run funstion stop()

motor1.stopMotor(2)

#tell to run main() if file is runned alone
if __name__ == '__main__'
    #lag motor og kjør main()
    motor = Motor(1,2,3)
    main()