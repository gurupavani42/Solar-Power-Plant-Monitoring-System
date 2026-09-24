# Solar Power Plant Monitoring System
# EEE Python Mini Project

# Safe operating limits
MIN_VOLTAGE = 200
MAX_VOLTAGE = 250
MAX_CURRENT = 100
MIN_BATTERY = 20
MAX_TEMPERATURE = 70


def monitor_solar_plant(voltage, current, battery, temperature, sunlight):
    print("\n======================================")
    print("     SOLAR POWER PLANT MONITOR")
    print("======================================")

    print(f"Voltage       : {voltage:.2f} V")
    print(f"Current       : {current:.2f} A")
    print(f"Battery Level : {battery:.2f} %")
    print(f"Temperature   : {temperature:.2f} °C")
    print(f"Sunlight      : {sunlight:.2f} %")

    # Calculate generated power
    power = voltage * current
    print(f"Solar Power   : {power:.2f} W")

    faults = []

    # Voltage checking
    if voltage > MAX_VOLTAGE:
        faults.append("Over-Voltage")
    elif voltage < MIN_VOLTAGE:
        faults.append("Under-Voltage")

    # Current checking
    if current > MAX_CURRENT:
        faults.append("Over-Current")

    # Battery checking
    if battery < MIN_BATTERY:
        faults.append("Low Battery")

    # Temperature checking
    if temperature > MAX_TEMPERATURE:
        faults.append("High Temperature")

    # Sunlight checking
    if sunlight < 20:
        faults.append("Low Sunlight")

    print("\n----------- SYSTEM STATUS -----------")

    if len(faults) > 0:
        print("⚠ WARNING / FAULT DETECTED")

        for fault in faults:
            print(" -", fault)

        print("\nPlant Status : NEEDS ATTENTION")
    else:
        print("✓ SYSTEM NORMAL")
        print("Plant Status : OPERATING NORMALLY")

    print("======================================")


# Main program
print("======================================")
print("   SOLAR POWER PLANT MONITORING")
print("======================================")

voltage = float(input("Enter Solar Voltage (V): "))
current = float(input("Enter Solar Current (A): "))
battery = float(input("Enter Battery Level (%): "))
temperature = float(input("Enter Temperature (°C): "))
sunlight = float(input("Enter Sunlight Level (%): "))

monitor_solar_plant(
    voltage,
    current,
    battery,
    temperature,
    sunlight
)
