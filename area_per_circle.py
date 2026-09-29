#!/usr/bin/env python3
# Created By: Vova M
# Date: Sep 21, 2026

import math


def main():
    print("--- Circle Area and Circumference Calculator ---\n")

    try:
        radius = float(input("Enter the radius of the circle: "))
    except ValueError:
        print("Invalid input! Please enter a numerical value.")
        return

    # Calculations using math.pi
    area = math.pi * (radius**2)
    circumference = 2 * math.pi * radius

    # Display results
    print(f"\nRadius: {radius}")
    print(f"Area: {area:.2f}")
    print(f"Circumference: {circumference:.2f}")


if __name__ == "__main__":
    main()
