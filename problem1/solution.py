import sys

def calculate_fuel_for_fuel(fuel_mass):
    fuel = (int(fuel_mass/3) - 2)
    if fuel <= 0:
        # wishing really hard
        return 0
    fuel += calculate_fuel_for_fuel(fuel)
    return fuel

# main
if len(sys.argv) == 2:
    print ('Mass:', sys.argv[1])
    mass = int(sys.argv[1])
    total_fuel = int((mass/3) - 2)
    fuel_fuel = calculate_fuel_for_fuel(total_fuel)
    total_fuel += fuel_fuel
else:
    f = open('input.txt', 'r')
    lines = f.readlines()
    total_fuel = 0
    for line in lines:
        mass = int(line)
        module_fuel = int((mass/3) - 2)
        fuel_fuel = calculate_fuel_for_fuel(module_fuel)
        total_fuel += module_fuel + fuel_fuel

print ('Required fuel:', total_fuel)



