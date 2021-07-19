import math

f = open('input.txt', 'r')
lines = f.readlines()
f.close()

asteroids = []

y = 0
for line in lines:
    x = 0
    for character in line:
        if character == '#':
            asteroids.append((x,y))
        x += 1
    y += 1

most_asteroids = -1
best_asteroid = (-1,-1)
best_asteroid_index = -1

for i, asteroid in enumerate(asteroids):
    visible_asteroids = 0
    angles = []
    for j, test_asteroid in enumerate(asteroids):
        if i != j:
            angle = math.atan2(asteroid[1] - test_asteroid[1], asteroid[0] - test_asteroid[0])
            if angle not in angles:
                angles.append(angle)
                visible_asteroids += 1
    #print("Asteroid: {} Visible Asteroids: {}".format(asteroid, visible_asteroids))
    if visible_asteroids > most_asteroids:
        most_asteroids = visible_asteroids
        best_asteroid = asteroid
        best_asteroid_index = i

print ("Best Asteroid located at: {}, can see {} other asteroids".format(best_asteroid, most_asteroids))

# begin vaporizing asteroids
asteroid_destory = asteroids.copy()
asteroid_destory.remove(best_asteroid)

destoyed = []
count = 1
while len(asteroid_destory) > 0:
    angles = []
    asteroids_to_destory = {}
    for i, asteroid in enumerate(asteroid_destory):
        angle = (math.degrees(math.atan2(asteroid[1] - best_asteroid[1], asteroid[0] - best_asteroid[0])) + 90) % 360 # rotate by 90 degrees
        if angle not in angles:
            angles.append(angle)
            asteroids_to_destory[angle] = asteroid
        else:
            # if the asteroid we are testing is _closer_ it is destoyed first, even if the angle exists
            asteroid_to_test = asteroids_to_destory[angle]
            curr_distance = abs(best_asteroid[0] - asteroid[0]) + abs(best_asteroid[1] - asteroid[1])
            test_distance = abs(best_asteroid[0] - asteroid_to_test[0]) + abs(best_asteroid[1] - asteroid_to_test[1])
            if curr_distance < test_distance:
                asteroids_to_destory[angle] = asteroid


    angles.sort()
    for angle in angles:
        #print("{} Destoying Asteroid:".format(count), asteroids_to_destory[angle], angle)
        count += 1
        destoyed.append(asteroids_to_destory[angle])
        asteroid_destory.remove(asteroids_to_destory[angle])

print("200th asteroid destoyed:", destoyed[199])
