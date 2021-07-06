
pc = 0
f = open('input.txt', 'r')
#f = open('test_1.txt', 'r')
line = f.readline()
program = line.split(',')
while(1):
    opcode = int(program[pc])
    # add
    if opcode == 1:
        lhs = int(program[pc+1])
        rhs = int(program[pc+2])
        res = int(program[pc+3])
        lhs_val = int(program[lhs])
        rhs_val = int(program[rhs])
        res_val = lhs_val + rhs_val
        program[res] = str(res_val)
        pc += 4
    elif opcode == 2:
        lhs = int(program[pc+1])
        rhs = int(program[pc+2])
        res = int(program[pc+3])
        lhs_val = int(program[lhs])
        rhs_val = int(program[rhs])
        res_val = lhs_val * rhs_val
        program[res] = str(res_val)
        pc += 4
    elif opcode == 99:
        print ('done!')
        break

print ('Program output at position 0:', program[0])