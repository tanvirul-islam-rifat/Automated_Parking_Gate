from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, AngularServo, DistanceSensor

from time import sleep

Device.pin_factory = PiGPIOFactory()

servo = AngularServo(17, min_angle=0, max_angle=180,
                     min_pulse_width=0.5/1000,
                     max_pulse_width=2.5/1000)

sensor = DistanceSensor(echo=24, trigger=23, max_distance=1)

while True:
    distance_cm = sensor.distance * 100
    print(f"Distance: {distance_cm:.2f} cm")

    if distance_cm < 5:
        print("Car detected! Opening gate...")
        servo.angle = 180   # Open gate
    else:
        print("No car. Gate closed.")
        servo.angle = 90    # Closed position

    sleep(0.5)
