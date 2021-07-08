


def meets_criteria(number):
    num_str = str(number)

    # check to see if two number are the same next to each other
    i = 1
    previous = num_str[0]
    while i < 6 :
        if previous == num_str[i]:
            break
        previous = num_str[i]
        i+=1
    if i == 6:
        return 0

    # no more than 2 of the same number in a group
    i = 1
    found_double = 0
    same = 0
    previous = num_str[0]
    while i < 6:
        if previous == num_str[i]:
            if same == 0:
                same = 2
            else:
                same += 1
        else:
            if same == 2:
                found_double = 1
            same = 0
        previous = num_str[i]
        i += 1
    #print ("Most same: {} Same: {}".format(found_double, same))

    if same == 2:
        found_double = 1

    if not found_double:
        return 0


    i = 1
    previous = num_str[0]
    while i < 6 :
        if previous > num_str[i]:
            return 0
        previous = num_str[i]
        i+=1
    return 1

min = 245318
max = 765747


valid = 0
for n in range(min, max):
    if meets_criteria(n):
        valid += 1

print('possible valid passwords: {}'.format(valid))