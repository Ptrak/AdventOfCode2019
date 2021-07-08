
# Courtesy of http://paulbourke.net/geometry/pointlineplane/
def intersect_2(x1,y1,x2,y2,x3,y3,x4,y4):
    # Check if none of the lines are of length 0
    if (x1 == x2 and y1 == y2) or (x3 == x4 and y3 == y4):
        return

    denominator = ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))

    # Lines are parallel
    if denominator == 0 :
        return

    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator

    # is the intersection along the segments
    if ua < 0 or ua > 1 or ub < 0 or ub > 1:
        return

    # Return a object with the x and y coordinates of the intersection
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)

    return (int(x), int(y))

def convert_to_xsegments(points):
    xsegments = [0]
    i = 0
    x = 0
    while i < len(points):
        if points[i][0] == 'R':
            x += int(points[i][1:])
        if points[i][0] == 'L':
            x -= int(points[i][1:])
        i += 1
        xsegments.append(x)
    return xsegments

def convert_to_ysegments(points):
    ysegments = [0]
    i = 0
    y = 0
    while i < len(points):
        if points[i][0] == 'U':
            y += int(points[i][1:])
        if points[i][0] == 'D':
            y -= int(points[i][1:])
        i += 1
        ysegments.append(y)
    return ysegments

#f = open('test_input.txt', 'r')
f = open('input.txt', 'r')
points1 = f.readline().split(',')
points2 = f.readline().split(',')
f.close()

segments1x = convert_to_xsegments(points1)
segments1y = convert_to_ysegments(points1)


i = 0
while i < len(segments1x):

    i+=1

segments2x = convert_to_xsegments(points2)
segments2y = convert_to_ysegments(points2)

i = 0
while i < len(segments2x):

    i+= 1

# foreach every segment, cross reference with each other segment
shortest_timing = 0
smallest_distance = 0
i = 0
while i < len(segments1x) - 1:
    j = 0
    while j < len(segments2x) - 1:
        s0 = [(segments1x[i],segments1y[i]), (segments1x[i+1],segments1y[i+1])]
        s1 = [(segments2x[j],segments2y[j]), (segments2x[j+1],segments2y[j+1])]
        point = intersect_2(segments1x[i],segments1y[i],segments1x[i+1],segments1y[i+1],segments2x[j],segments2y[j],segments2x[j+1],segments2y[j+1])

        # intersection found
        if point :
            # calculate distance traveled by each wire to this point
            steps1 = 0
            i_2 = 0
            while i_2 < i:
                intermediate = abs(segments1x[i_2] - segments1x[i_2+1]) + abs(segments1y[i_2] - segments1y[i_2+1])
                steps1 += intermediate
                i_2 += 1
            # calculate to point
            edge = abs(segments1x[i_2] - point[0]) + abs(segments1y[i_2] - point[1])
            steps1 += edge
            print("steps1:{}".format(steps1))

            steps2 = 0
            j_2 = 0
            while j_2 < j:
                steps2 += abs(segments2x[j_2] - segments2x[j_2+1]) + abs(segments2y[j_2] - segments2y[j_2+1])
                j_2 += 1
            edge = abs(segments2x[j_2] - point[0]) + abs(segments2y[j_2] - point[1])
            steps2 += edge
            print("steps2:{}".format(steps2))

            distance = abs(point[0]) + abs(point[1])
            timing = steps1 + steps2
            print('Point: {} Distance: {} Steps: {}'.format(point, distance, timing))
            if smallest_distance == 0 or distance < smallest_distance:
                smallest_distance = distance
            if shortest_timing == 0 or timing < shortest_timing:
                shortest_timing = timing
        j+=1
    i+=1

print('closest intersection is distance: {}'.format(smallest_distance))
print('shortest timing steps are {}'.format(shortest_timing))


