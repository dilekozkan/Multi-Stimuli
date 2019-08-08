 # External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
valve1 = 3  # VALVE 1
valve3 = 5  # VALVE 3
valve2 = 7  # VALVE 2  
valve4 = 11 # VALVE 4 
valve5 = 13 # VALVE 5
valve6 = 15 # VALVE 6 
ttl_out= 16 # TTL Output

# Pin Setup:
GPIO.setmode(GPIO.BOARD)

GPIO.setup(valve1,GPIO.OUT)  # LED pin set as output
GPIO.setup(valve2,GPIO.OUT) # PWM pin set as output
GPIO.setup(valve3,GPIO.OUT)  # PWM pin set as output
GPIO.setup(valve4,GPIO.OUT) # LED pin set as output
GPIO.setup(valve5,GPIO.OUT) # PWM pin set as output
GPIO.setup(valve6,GPIO.OUT) # PWM pin set as output

GPIO.output(valve1,GPIO.LOW)
GPIO.output(valve2,GPIO.LOW)
GPIO.output(valve4,GPIO.LOW)
GPIO.output(valve5,GPIO.LOW) 
GPIO.output(valve3,GPIO.HIGH)
GPIO.output(valve6,GPIO.HIGH)
GPIO.setup(ttl_out,GPIO.IN)

airTime    = 20; # 29.75
odorTime   = 1;
sleepTime3 = 5;
delayTime  = 1;

time.sleep(2)

print("Here we go STIMULUS! Press CTRL+C to exit")

try:
    var1=GPIO.input(ttl_out)
    print var1
    while True:
            var1=GPIO.input(ttl_out)
            if var1 == True:
                print var1
                time.sleep(delayTime)
                
                GPIO.output(valve1,GPIO.LOW)
                GPIO.output(valve2,GPIO.HIGH)
                GPIO.output(valve4,GPIO.HIGH)
                GPIO.output(valve5,GPIO.HIGH) 
                
                GPIO.output(valve3,GPIO.LOW)
                GPIO.output(valve6,GPIO.LOW)
                
                time.sleep(odorTime)
                
                GPIO.output(valve1,GPIO.LOW)
                GPIO.output(valve2,GPIO.LOW)
                GPIO.output(valve4,GPIO.LOW)
                GPIO.output(valve5,GPIO.LOW) 
                GPIO.output(valve3,GPIO.HIGH)
                GPIO.output(valve6,GPIO.HIGH)
                
                time.sleep(airTime)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:

            GPIO.output(valve1,GPIO.LOW)
            GPIO.output(valve2,GPIO.LOW)
            GPIO.output(valve4,GPIO.LOW)
            GPIO.output(valve5,GPIO.LOW) 
            GPIO.output(valve3,GPIO.HIGH)
            GPIO.output(valve6,GPIO.HIGH)
            
            GPIO.cleanup() # cleanup all GPIO
