from machine import Pin
import utime


led = [5, 4, 2, 15, 18, 19, 21, 22]
leds_pin = [Pin(pin, Pin.OUT) for pin in led]

btn1 = Pin(34, Pin.IN)
btn2 = Pin(35, Pin.IN)

counter = 0

def update_leds_pin(val2):
    for i in range(8):
        leds_pin[i].value(1 if i < val2 else 0)

while True:
    
    if btn1.value() == 1:
        utime.sleep_ms(20) 
        if btn1.value() == 1:  
            while btn1.value() == 1:
                utime.sleep_ms(10)  
            if counter < 8:
                counter += 1
                print("Increased to", counter)
                update_leds_pin(counter)

    
    if btn2.value() == 1:
        utime.sleep_ms(20) 
        if btn2.value() == 1:  
            while btn2.value() == 1:
                utime.sleep_ms(10)  
            if counter > 0:
                counter -= 1
                print("Decreased to", counter)
                update_leds_pin(counter)

    utime.sleep_ms(10)  
