import os
import sys
import time
import machine
import gc

from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time    import sleep

I2C_ADDR = 0x27
totalRows = 4
totalColumns = 20
i2c = SoftI2C(scl=Pin(1), sda=Pin(0), freq=100000) #I2C for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000) #I2C for ESP8266
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)


# Recursive Fibonacci function for benchmarking
def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

# Function to display results on the LCD
def display_lines(lines, delay=2):
    lcd.clear()
    for i, line in enumerate(lines[:4]):  # Show only the first 4 lines at a time
        lcd.move_to(0, i)
        lcd.putstr(line[:20])  # Ensure each line fits within 20 characters
    time.sleep(delay)

# Function to display results
def ShowResults(hardware, version, MHz, result, elapsed):
    factor = 3.694282 / elapsed
    scale = factor / (MHz / 125.0)

    # Create lines for display
    lines = [
        f"HW: {hardware}",
        f"Version: {version}",
        f"Freq: {MHz} MHz",
        f"Result: {result}",
        f"Time: {elapsed:.6f}s",
        f"Multiplier: {int(factor + 0.5)}",
        f"Scale: {scale:.2f}",
    ]

    # Scroll through the lines
    for start in range(0, len(lines), 4):
        display_lines(lines[start:start + 4], delay=3)

    # Display failure message if result is incorrect
    if result != 46368:
        display_lines(["FAILED: Invalid", "Result!", f"Expected: 46368", f"Got: {result}"], delay=3)

# Benchmarking function
def Benchmark():
    # gc.disable()
    # Fetch system information
    uname = os.uname()
    hardware = uname[-1].split()[-1]
    version = uname[3].split(".")[:4]
    if version[2].find("preview") < 0:
        version = ".".join(version)[1:]
    else:
        version[1] = str(int(version[1]) - 1)
        version = ".".join(version)[1:].replace("preview.", "")

    # Benchmark for different CPU frequencies
    gc.disable()
    for MHz in [250, 125]:
        machine.freq(MHz * 1_000_000)  # Set the CPU frequency
        start_time = time.ticks_us()
        result = Fibonacci(24)  # Compute Fibonacci(24)
        end_time = time.ticks_us()
        elapsed = (end_time - start_time) / 1_000_000  # Convert to seconds
        ShowResults(hardware, version, MHz, result, elapsed)
        # hardware = ""  # Only show hardware name once
        # version = ""
    gc.enable()
# Display introductory text and run the benchmark
lcd.clear()
lcd.move_to(0,2)
lcd.putstr(" Starting Benchmark")
time.sleep(2)

Benchmark()

# Display completion message
lcd.clear()
lcd.move_to(0,1)
lcd.putstr(" Benchmark Complete")


