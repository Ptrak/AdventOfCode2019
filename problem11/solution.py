
def add(program, pc, mode1, mode2, mode3):
    if mode1 == 0:
        lhs_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        lhs_val = int(program[pc+1])
    elif mode1 == 2:
        lhs_val = int(program[int(program[pc+1]) + offset])

    if mode2 == 0:
        rhs_val = int(program[int(program[pc+2])])
    elif mode2 == 1:
        rhs_val = int(program[pc+2])
    elif mode2 == 2:
        rhs_val = int(program[int(program[pc+2]) + offset])

    result = lhs_val + rhs_val
    #print("{} + {} = {}".format(lhs_val, rhs_val, result))
    if mode3 == 0 or mode3 == 1:
        program[int(program[pc+3])] = str(result)
    elif mode3 == 2:
        program[int(program[pc+3]) + offset] = str(result)

    return pc + 4

def multiply(program, pc, mode1, mode2, mode3):
    if mode1 == 0:
        lhs_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        lhs_val = int(program[pc+1])
    elif mode1 == 2:
        lhs_val = int(program[int(program[pc+1]) + offset])

    if mode2 == 0:
        rhs_val = int(program[int(program[pc+2])])
    elif mode2 == 1:
        rhs_val = int(program[pc+2])
    elif mode2 == 2:
        rhs_val = int(program[int(program[pc+2]) + offset])

    result = lhs_val * rhs_val
    if mode3 == 0 or mode3 == 1:
        program[int(program[pc+3])] = str(result)
    elif mode3 == 2:
        program[int(program[pc+3]) + offset] = str(result)
    return pc + 4

def read(program, pc, mode1):
    global robo_out
    if mode1 == 0:
        location = int(program[pc+1])
    elif mode1 == 1:
        location = pc + 1
        #print("Value: {}".format(program[pc+1]))
        ###
        robo_out = int(program[pc+1])
        ###
        return pc + 2
    elif mode1 == 2:
        location = int(program[pc+1]) + offset
        #print("location {} offset: {}".format(location, offset))

    #print("Value: {}".format(program[location]))
    ###
    robo_out = int(program[location])
    ###
    return pc + 2

def jit(program, pc, mode1, mode2):
    if mode1 == 0:
        test_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        test_val = int(program[pc + 1])
    elif mode1 == 2:
        test_val = int(program[int(program[pc+1]) + offset])

    if mode2 == 0:
        jump_val = int(program[int(program[pc+2])])
    elif mode2 == 1:
        jump_val = int(program[pc+2])
    elif mode2 == 2:
        jump_val = int(program[int(program[pc+2]) + offset])

    if test_val != 0:
        return jump_val
    return pc + 3

def jnt(program, pc, mode1, mode2):
    if mode1 == 0:
        test_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        test_val = int(program[pc + 1])
    elif mode1 == 2:
        test_val = int(program[int(program[pc+1]) + offset])

    if mode2 == 0:
        jump_val = int(program[int(program[pc+2])])
    elif mode2 == 1:
        jump_val = int(program[pc+2])
    elif mode2 == 2:
        jump_val = int(program[int(program[pc+2]) + offset])

    if test_val == 0:
        return jump_val
    return pc + 3

def lt(program, pc, mode1, mode2, mode3):
    if mode1 == 0:
        lhs_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        lhs_val = int(program[pc+1])
    elif mode1 == 2:
        lhs_val = int(program[int(program[pc+1]) + offset])

    if mode2 == 0:
        rhs_val = int(program[int(program[pc+2])])
    elif mode2 == 1:
        rhs_val = int(program[pc+2])
    elif mode2 == 2:
        rhs_val = int(program[int(program[pc+2]) + offset])

    result = int(lhs_val < rhs_val)
    if mode3 == 0 or mode3 == 1:
        program[int(program[pc+3])] = str(result)
    elif mode3 == 2:
        program[int(program[pc+3]) + offset] = str(result)
    return pc + 4

def eq(program, pc, mode1, mode2, mode3):
    if mode1 == 0:
        lhs_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        lhs_val = int(program[pc+1])
    elif mode1 == 2:
        lhs_val = int(program[int(program[pc+1]) + offset])

    if mode2 == 0:
        rhs_val = int(program[int(program[pc+2])])
    elif mode2 == 1:
        rhs_val = int(program[pc+2])
    elif mode2 == 2:
        rhs_val = int(program[int(program[pc+2]) + offset])

    result = int(lhs_val == rhs_val)
    if mode3 == 0 or mode3 == 1:
        program[int(program[pc+3])] = str(result)
    elif mode3 == 2:
        program[int(program[pc+3]) + offset] = str(result)
    return pc + 4

def rbo(program, pc, mode1):
    global offset
    if mode1 == 0:
        offset += int(program[int(program[pc+1])])
    elif mode1 == 1:
        offset += int(program[pc+1])
    elif mode1 == 2:
        offset += int(program[int(program[pc+1]) + offset])
    return pc + 2

## Problem 11 specific variables

def get_color(coord ,panels):
    if coord in panels:
        return 1 # painted white
    else:
        return 0 # painted black (default)

# (0,0) is the center of the painting
robot_x = 0
robot_y = 0

global robo_out
robo_out = 0

out_mode = 'color'

all_panels_painted = []

# Panels stored in this array are painted white, everything else is black
panels = [(0,0)]
direction = 'up'
##

global offset
offset = 0

global memory
memory = [0 for _ in range(100000)]

pc = 0
f = open('program.txt', 'r')
line = f.readline().rstrip()
program = line.split(',')
program.extend(memory)

while(1):
    instruction = program[pc]
    while(len(instruction) < 5) :
        instruction = "0" + instruction
    mode3  = int(instruction[0])
    mode2  = int(instruction[1])
    mode1  = int(instruction[2])
    opcode = int(instruction[3:])
    # add
    if opcode == 1:
        pc = add(program, pc, mode1, mode2, mode3)
    elif opcode == 2:
        pc = multiply(program, pc, mode1, mode2, mode3)
    elif opcode == 3:
        if mode1 == 0 or mode1 == 1:
            location = int(program[pc+1])
        elif mode1 == 2:
            location = int(int(program[pc+1]) + offset)
        color = get_color((robot_x,robot_y), panels)
        #print("Location: ({},{}) Color: {}".format(robot_x, robot_y, color))
        program[location] = color
        pc += 2
    elif opcode == 4:
        pc = read(program, pc, mode1)
        ###
        if out_mode == 'color':
            #print("Paint color {} at ({},{})".format(robo_out, robot_x, robot_y))
            if (robot_x, robot_y) not in all_panels_painted:
                #print("Adding new panel")
                all_panels_painted.append((robot_x, robot_y))
            if robo_out == 1:
                panels.append((robot_x, robot_y))
            else: # Panel painted back to white
                if (robot_x, robot_y) in panels:
                    panels.remove((robot_x, robot_y))
            out_mode = 'turn'
        else:
            out_mode = 'color'
            if direction == 'up':
                if robo_out == 1:
                    direction = 'right'
                    robot_x += 1
                else:
                    direction = 'left'
                    robot_x -= 1
            elif direction == 'down':
                if robo_out == 1:
                    direction = 'left'
                    robot_x -= 1
                else:
                    direction = 'right'
                    robot_x += 1
            elif direction == 'left':
                if robo_out == 1:
                    direction = 'up'
                    robot_y -= 1
                else:
                    direction = 'down'
                    robot_y += 1
            elif direction == 'right':
                if robo_out == 1:
                    direction = 'down'
                    robot_y += 1
                else:
                    direction = 'up'
                    robot_y -= 1
            print ("Turn: ", direction)
        ###
    elif opcode == 5:
        pc = jit(program, pc, mode1, mode2)
    elif opcode == 6:
        pc = jnt(program, pc, mode1, mode2)
    elif opcode == 7:
        pc = lt(program, pc, mode1, mode2, mode3)
    elif opcode == 8:
        pc = eq(program, pc, mode1, mode2, mode3)
    elif opcode == 9:
        pc = rbo(program, pc, mode1)
    elif opcode == 99:
        print ('done!')
        ##
        print("total number of panels painted: {}".format(len(all_panels_painted)))
        x_min_manual = 0
        y_min_manual = 0
        x_max_manual = 0
        y_max_manual = 0
        for i, panel in enumerate(panels):
            x = panel[0]
            y = panel[1]
            if (x > x_max_manual):
                x_max_manual = x
            if (x < x_min_manual):
                x_min_manual = x
            if (y > y_max_manual):
                y_max_manual = y
            if (y < y_min_manual):
                y_min_manual = y

        print("1DEBUG: x_min:", x_min_manual)
        print("1DEBUG: x_max:", x_max_manual)
        print("1DEBUG: y_min:", y_min_manual)
        print("1DEBUG: y_max:", y_max_manual)

        # x_min = int(min(panels)[0])
        # x_max = int(max(panels)[0])
        # y_min = int(min(panels)[1])
        # y_max = int(max(panels)[1])
        # print("DEBUG: x_min:", x_min)
        # print("DEBUG: x_max:", x_max)
        # print("DEBUG: y_min:", y_min)
        # print("DEBUG: y_max:", y_max)
        x_length = abs(x_max_manual - x_min_manual) + 1
        y_length = abs(y_max_manual - y_min_manual) + 1
        print("Final Image Dimensions: {} X {}".format(x_length, y_length))
        final_image = [[0 for _ in range(x_length)]for _ in range(y_length)]
        for i, columns in enumerate(final_image) :
            for j, rows in enumerate(columns) :
                final_image[i][j] = '.'

        for i, coord in enumerate(panels):
            x = coord[0] - x_min_manual
            y = coord[1] - y_min_manual
            final_image[y][x]  = '#'

        f = open('image.txt', 'w')
        for i, columns in enumerate(final_image) :
            for j, rows in enumerate(columns) :
                f.write(final_image[i][j])
            f.write("\n")
        f.close()
        ##
        break
    else:
        print("invalid opcode!!!", opcode)
        break