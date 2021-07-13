import itertools

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

def run_program(program, program_input, program_counter, phase_tmp):
    input_index = 0
    output = None
    pc = program_counter
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
            # val = input("Enter your value: ")
            # Read input given and automatically enter it
            val = program_input[input_index]
            input_index += 1
            program[location] = val
            if phase_tmp == 4:
                print("inputting", val)
            pc += 2
        elif opcode == 4:
            if mode1 == 0:
                location = int(program[pc+1])
            elif mode1 == 1:
                location = pc + 1
            #print("  Value: {}".format(program[location]))
            output = int(program[location])
            pc += 2
            return [output, pc, program] # Halt the program here. Resume after

        elif opcode == 5:
            pc = jit(program, pc, mode1, mode2)
        elif opcode == 6:
            pc = jnt(program, pc, mode1, mode2)
        elif opcode == 7:
            pc = lt(program, pc, mode1, mode2)
        elif opcode == 8:
            pc = eq(program, pc, mode1, mode2)
        elif opcode == 99:
            break
        else:
            print("invalid opcode!!!", opcode)
            break
    return [output, -1, -1]

## MAIN
f = open('program.txt', 'r')
#f = open('test_program.txt', 'r')
og_program = f.readline().rstrip().split(',')
f.close()

max_output = -1
max_sequence = [0,0,0,0,0]
sequences = itertools.permutations(range(5,10))
#sequences = itertools.permutations(range(5))
# for each sequence
for sequence in sequences:
    current_output = 0  # current output accumulated
    programs       = [og_program.copy(), og_program.copy(), og_program.copy(), og_program.copy(), og_program.copy()] # for tracking programs mid execution
    pcs            = [0,0,0,0,0] # for tracking program counters mid execution
    while pcs[len(sequence)-1] > -1:
        phase_count = 0
        for phase in sequence:
            program_input = [phase, current_output]
            if pcs[phase_count] != 0:
                program_input = [current_output]
            [output, program_counter, program_state] = run_program(programs[phase_count], program_input, pcs[phase_count], phase)
            # save the state of the program back
            programs[phase_count] = program_state
            pcs[phase_count]      = program_counter
            if output:
                current_output = output # save module output
            phase_count += 1
    print ("Sequence: {} Output: {}".format(sequence, current_output))

    if current_output > max_output :
        max_output = current_output
        max_sequence = sequence

print("max output: {} Max Sequence: {}".format(max_output, max_sequence))

program = og_program.copy()


