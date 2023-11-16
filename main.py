import machine
import time

# Define the GPIO pin connected to the OUT pin of the PIR sensor
pir_sensor_pin = machine.Pin(7, machine.Pin.IN)

def motion_detected(pin):
    print("Motion detected!")

# Set up an interrupt on the GPIO pin for detecting motion
pir_sensor_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

try:
    while True:
        # Your main code can continue here
        # For example, you can perform other tasks or sleep
        time.sleep(1)
except KeyboardInterrupt:
    # Handle Ctrl+C to stop the code
    pir_sensor_pin.irq(trigger=0)  # Disable the interrupt
    print("Stopped by user")
