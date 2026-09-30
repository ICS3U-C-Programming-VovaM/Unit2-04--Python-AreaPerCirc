#!/usr/bin/env python3
# Created By: Vova M
# Date: Sep 21, 2026
# calculates the area and perimeter of a circle

import math


def main():
    print("--- Circle Area and Circumference Calculator ---\n")

    # Get input from the user
    radius = float(input("Enter the radius of the circle (in cm): "))

    # Calculations using math.pi
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius

    # Display results formatted to 2 decimal places with cm units
    print(f"\nRadius: {radius} cm")
    print(f"Area: {area:.2f} cm²")
    print(f"Circumference: {circumference:.2f} cm")


if __name__ == "__main__":
    main()
