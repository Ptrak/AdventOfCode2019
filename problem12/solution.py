import itertools
import math

def main():
    states = [{},{},{}]
    cycleTimes = [-1,-1,-1]
    moons = []
    stepsTaken = 1

    f = open('input.txt', 'r')
    moon_input = f.readlines()
    f.close()
    for moon in moon_input:
        raw_coords = moon.rstrip().split(',')
        moon = {}
        for coordinate in raw_coords:
            split_coord = coordinate.removeprefix('<').removesuffix('>').split('=')
            moon[split_coord[0].strip()] = int(split_coord[1])
        moons.append(moon)

    # set initial values for the moons
    for moon in moons:
        moon['v_x'] = 0
        moon['v_y'] = 0
        moon['v_z'] = 0

    # store initial state
    xmoonshash = moonsHash(moons, 'x')
    ymoonshash = moonsHash(moons, 'y')
    zmoonshash = moonsHash(moons, 'z')
    states[0] [xmoonshash] = 1
    states[1] [ymoonshash] = 1
    states[2] [zmoonshash] = 1

    moonCombinations = []
    for i,j in itertools.combinations(moons, 2):
        moonCombinations.append((i,j))


    # perform time steps
    #steps = 1000

    #print("After 0 steps")
    #for moon in moons:
    #    print(moon)

    # assume we are in the middle of a cycle. How long until the cycle repeats?
    # Take cycle and look for moons returning to their original position

    #for _ in itertools.repeat(None, steps):
    while True:
        #step(moons)
        step2(moons, moonCombinations)

        # hash the x,y,z values
        xmoonshash = moonsHash(moons, 'x')
        ymoonshash = moonsHash(moons, 'y')
        zmoonshash = moonsHash(moons, 'z')

        if xmoonshash not in states[0]:
            states[0][xmoonshash] = 1
        else:
            if cycleTimes[0] < 0:
                print("X cycles in ", stepsTaken)
                cycleTimes[0] = stepsTaken

        if ymoonshash not in states[1]:
            states[1][ymoonshash] = 1
        else:
            if cycleTimes[1] < 0:
                print("Y cycles in ", stepsTaken)
                cycleTimes[1] = stepsTaken

        if zmoonshash not in states[2]:
            states[2][zmoonshash] = 1
        else:
            if cycleTimes[2] < 0:
                print("Z cycles in ", stepsTaken)
                cycleTimes[2] = stepsTaken

        if min(cycleTimes) >= 0:
            break
        stepsTaken += 1

    stepsToCycle = math.lcm(cycleTimes[0], math.lcm(cycleTimes[1], cycleTimes[2]))
    print ("Took {} steps until we had a hash collision".format(stepsToCycle))

    #print("After {} steps".format(steps))
    #for moon in moons:
    #   print (moon)

    # calculate energy
    #totalEnergy = 0
    #for moon in moons:
    #    moonEnergy = calcualteEnergy(moon)
    #    print("Moon Energy: ", moonEnergy)
    #    totalEnergy += moonEnergy
    #print("total Energy", totalEnergy)

# performs a single time step on the array of moons
def step(moons):
    # apply gravity
    for i,j in itertools.combinations(moons, 2):
        applyGravity(i, j, 'x')
        applyGravity(i, j, 'y')
        applyGravity(i, j, 'z')

    # update velocity
    for moon in moons:
        moon['x'] += moon['v_x']
        moon['y'] += moon['v_y']
        moon['z'] += moon['v_z']


def step2(moons, moonCombinations):

    # unroll this loop
    applyGravity(moonCombinations[0][0], moonCombinations[0][1], 'x')
    applyGravity(moonCombinations[0][0], moonCombinations[0][1], 'y')
    applyGravity(moonCombinations[0][0], moonCombinations[0][1], 'z')

    applyGravity(moonCombinations[1][0], moonCombinations[1][1], 'x')
    applyGravity(moonCombinations[1][0], moonCombinations[1][1], 'y')
    applyGravity(moonCombinations[1][0], moonCombinations[1][1], 'z')

    applyGravity(moonCombinations[2][0], moonCombinations[2][1], 'x')
    applyGravity(moonCombinations[2][0], moonCombinations[2][1], 'y')
    applyGravity(moonCombinations[2][0], moonCombinations[2][1], 'z')

    applyGravity(moonCombinations[3][0], moonCombinations[3][1], 'x')
    applyGravity(moonCombinations[3][0], moonCombinations[3][1], 'y')
    applyGravity(moonCombinations[3][0], moonCombinations[3][1], 'z')

    applyGravity(moonCombinations[4][0], moonCombinations[4][1], 'x')
    applyGravity(moonCombinations[4][0], moonCombinations[4][1], 'y')
    applyGravity(moonCombinations[4][0], moonCombinations[4][1], 'z')

    applyGravity(moonCombinations[5][0], moonCombinations[5][1], 'x')
    applyGravity(moonCombinations[5][0], moonCombinations[5][1], 'y')
    applyGravity(moonCombinations[5][0], moonCombinations[5][1], 'z')

    # unroll loop
    moons[0]['x'] += moons[0]['v_x']
    moons[0]['y'] += moons[0]['v_y']
    moons[0]['z'] += moons[0]['v_z']
    moons[1]['x'] += moons[1]['v_x']
    moons[1]['y'] += moons[1]['v_y']
    moons[1]['z'] += moons[1]['v_z']
    moons[2]['x'] += moons[2]['v_x']
    moons[2]['y'] += moons[2]['v_y']
    moons[2]['z'] += moons[2]['v_z']
    moons[3]['x'] += moons[3]['v_x']
    moons[3]['y'] += moons[3]['v_y']
    moons[3]['z'] += moons[3]['v_z']

def applyGravity(moon1, moon2, direction):
    if moon1[direction] < moon2[direction]:
        moon1["v_" + direction] += 1
        moon2["v_" + direction] -= 1
    elif moon1[direction] > moon2[direction]:
        moon1["v_" + direction] -= 1
        moon2["v_" + direction] += 1

def calcualteEnergy(moon):
    potentialEnergy = abs(moon['x'])   + abs(moon['y'])   + abs(moon['z'])
    kineticEnergy   = abs(moon['v_x']) + abs(moon['v_y']) + abs(moon['v_z'])
    return potentialEnergy * kineticEnergy

def getHash(moons):
    moonHash = ''
    for moon in moons:
        moonHash += getMoonHash(moon)
    return moonHash

def getMoonHash(moon):
    return str(moon['x']) + str(moon['y']) + str(moon['z']) + str(moon['v_x']) + str(moon['v_y']) + str(moon['v_z'])

def moonsHash(moons, direction):
    return str(moons[0][direction]) + str(moons[0]["v_" + direction]) + str(moons[1][direction]) + str(moons[1]["v_" + direction]) + str(moons[2][direction]) + str(moons[2]["v_" + direction]) + str(moons[3][direction]) + str(moons[3]["v_" + direction])


main()
