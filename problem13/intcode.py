###
import collections
###

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
    if mode1 == 0:
        location = int(program[pc+1])
    elif mode1 == 1:
        location = pc + 1
        return (pc + 2, program[pc+1])
    elif mode1 == 2:
        location = int(program[pc+1]) + offset
    return (pc + 2, program[location])

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

def runProgram(program, pc, inputs):
    output = []
    newInputs = inputs.copy()
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
            ###
            if len(inputs) == 0:
                parseOutput(output)
            val = 0
            if len(inputs) > 0:
                val = inputs.pop(0)
            else:
                val = input("Enter your value: ")
                while val != '0' and val != '-1' and val != '1':
                    val = input("Enter your value: ")
                newInputs.append(val)
            ###
            program[location] = val
            pc += 2
        elif opcode == 4:
            res = read(program, pc, mode1)
            pc = res[0]
            output.append(int(res[1]))
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
            print(program[386])
            f = open('inputs_used.txt', 'w')
            f.write(','.join(newInputs))
            f.close()
            break
        else:
            print("invalid opcode!!!", opcode)
            break
    return (pc, output)


def main():
    global offset
    offset = 0

    global memory
    memory = [0 for _ in range(100000)]

    pc = 0
    f = open('program.txt', 'r')
    line = f.readline().rstrip()
    program = line.split(',')
    program.extend(memory)

    ### Problem 13
    f = open('input.txt', 'r')
    line = f.readline().rstrip()
    inputs = line.split(',')
    f.close()

    # insert quarters
    program[0] = '2'

    ###

    runProgram(program, pc, inputs)

    #c = collections.Counter(tileIds)
    #print("tiles with ID 2:", c)
    ###
def parseOutput(output):
    xCoords = []
    yCoords = []
    tileIds = []
    i = 0
    while i < len(output):
        xCoords.append(output[i])
        yCoords.append(output[i+1])
        tileIds.append(output[i+2])
        i += 3
    screen = [[0 for _ in range(max(xCoords) + 1)] for _ in range(max(yCoords) + 1)]

    score = 0
    i = 0
    while i < len(xCoords):
        if xCoords[i] == -1:
            score = tileIds[i]
            next
        screen[yCoords[i]][xCoords[i]] = tileIds[i]
        i += 1

    printScreen(screen, score)

def printScreen(screen, score):
    # print screen
    for _, row in enumerate(screen):
        for _, pixel in enumerate(row):
            if pixel == 0:
                print(' ', end='')
            elif pixel == 1:
                print('W', end='')
            elif pixel == 2:
                print('B', end='')
            elif pixel == 3:
                print('_', end='')
            elif pixel == 4:
                print('o', end='')
            else:
                print(pixel)
        print()
    print("Score:", score)

main()