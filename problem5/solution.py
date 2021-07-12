
def add(program, pc, mode1, mode2):
    if mode1 == 0:
        lhs_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        lhs_val = int(program[pc+1])

    if mode2 == 0:
        rhs_val = int(program[int(program[pc+2])])
    if mode2 == 1:
        rhs_val = int(program[pc+2])

    result = lhs_val + rhs_val
    #print("{} + {} = {}".format(lhs_val, rhs_val, result))
    program[int(program[pc+3])] = str(result)
    return pc + 4

def multiply(program, pc, mode1, mode2):
    if mode1 == 0:
        lhs_val = int(program[int(program[pc+1])])
    if mode1 == 1:
        lhs_val = int(program[pc+1])

    if mode2 == 0:
        rhs_val = int(program[int(program[pc+2])])
    if mode2 == 1:
        rhs_val = int(program[pc+2])

    result = lhs_val * rhs_val
    program[int(program[pc+3])] = str(result)
    return pc + 4

def read(program, pc, mode1):
    if mode1 == 0:
        location = int(program[pc+1])
    elif mode1 == 1:
        location = pc + 1

    #print("PC: {} Reading Location: {}".format(pc, location))
    print("  Value: {}".format(program[location]))
    return pc + 2

def jit(program, pc, mode1, mode2):
    if mode1 == 0:
        test_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        test_val = int(program[pc + 1])

    if mode2 == 0:
        jump_val = int(program[int(program[pc+2])])
    if mode2 == 1:
        jump_val = int(program[pc+2])

    if test_val != 0:
        return jump_val
    return pc + 3

def jnt(program, pc, mode1, mode2):
    if mode1 == 0:
        test_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        test_val = int(program[pc + 1])

    if mode2 == 0:
        jump_val = int(program[int(program[pc+2])])
    if mode2 == 1:
        jump_val = int(program[pc+2])

    if test_val == 0:
        return jump_val
    return pc + 3

def lt(program, pc, mode1, mode2):
    if mode1 == 0:
        lhs_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        lhs_val = int(program[pc+1])

    if mode2 == 0:
        rhs_val = int(program[int(program[pc+2])])
    elif mode2 == 1:
        rhs_val = int(program[pc+2])

    result = int(lhs_val < rhs_val)
    program[int(program[pc+3])] = str(result)
    return pc + 4

def eq(program, pc, mode1, mode2):
    if mode1 == 0:
        lhs_val = int(program[int(program[pc+1])])
    elif mode1 == 1:
        lhs_val = int(program[pc+1])

    if mode2 == 0:
        rhs_val = int(program[int(program[pc+2])])
    elif mode2 == 1:
        rhs_val = int(program[pc+2])

    result = int(lhs_val == rhs_val)
    program[int(program[pc+3])] = str(result)
    return pc + 4

pc = 0
f = open('input.txt', 'r')
#f = open('test_input.txt', 'r')
line = f.readline().rstrip()
program = line.split(',')
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
        pc = add(program, pc, mode1, mode2)
    elif opcode == 2:
        pc = multiply(program, pc, mode1, mode2)
    elif opcode == 3:
        location = int(program[pc+1])
        val = input("Enter your value: ")
        program[location] = val
        #print("  Saved to location: {} Value: {}".format(location, val))
        pc += 2
    elif opcode == 4:
        pc = read(program, pc, mode1)
    elif opcode == 5:
        pc = jit(program, pc, mode1, mode2)
    elif opcode == 6:
        pc = jnt(program, pc, mode1, mode2)
    elif opcode == 7:
        pc = lt(program, pc, mode1, mode2)
    elif opcode == 8:
        pc = eq(program, pc, mode1, mode2)
    elif opcode == 99:
        print ('done!')
        break
    else:
        print("invalid opcode!!!", opcode)
        break