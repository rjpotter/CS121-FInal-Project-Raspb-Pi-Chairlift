from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

# Set up the GPIO pins for the motor control
ENA = 17
IN1 = 27
IN2 = 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Initialize all pins to output low
GPIO.output(ENA, GPIO.LOW)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)

# Create a PWM object to control the speed of the motor
pwm = GPIO.PWM(ENA, 1000)

# Start the PWM with 0 duty cycle
pwm.start(0)

# Function to spin the motor forward
def motor_forward():
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN1, GPIO.HIGH)
    pwm.ChangeDutyCycle(100)

# Function to spin the motor backward
def motor_backward():
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    pwm.ChangeDutyCycle(30)

# Function to slow down the motor to 30% speed
def motor_slow():
    pwm.ChangeDutyCycle(30)

# Function to stop the motor
def motor_stop():
    pwm.ChangeDutyCycle(0)

@app.route("/forward_on", methods=["POST"])
def forward_on():
    print("Spinning Forward")
    motor_forward()
    return "ok"

@app.route("/forward_off", methods=["POST"])
def forward_off():
    print("Stopping Forward")
    motor_stop()
    return "ok"

@app.route("/reverse_on", methods=["POST"])
def reverse_on():
    print("Spinning Reverse")
    motor_backward()
    return "ok"

@app.route("/reverse_off", methods=["POST"])
def reverse_off():
    print("Stopping Reverse")
    motor_stop()
    return "ok"

@app.route("/slow", methods=["POST"])
def slow():
    print("Slowing Down")
    motor_slow()
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("button.html", title="Button", name="Ryan Potter")
