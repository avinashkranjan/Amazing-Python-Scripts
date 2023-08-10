import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the servo motor
servo_pin = 18

# Set up the GPIO pin for PWM
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz PWM frequency


def set_servo_position(angle):
    duty_cycle = angle / 18 + 2  # Map angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Give time for the servo to move


if __name__ == "__main__":
    try:
        pwm.start(0)  # Start with 0% duty cycle (0 degrees)
        print("Servo motor control started. Press Ctrl+C to stop.")

        while True:
            angle = float(input("Enter angle (0 to 180 degrees): "))
            if 0 <= angle <= 180:
                set_servo_position(angle)
            else:
                print("Invalid angle. Angle must be between 0 and 180 degrees.")

    except KeyboardInterrupt:
        print("\nServo motor control stopped.")
        pwm.stop()
        GPIO.cleanup()
