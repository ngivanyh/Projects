inputs = open("inputs.txt").read().split("\n")

pass_zero = 0
cur_index = 50 # the current index = the current value at that index
DIAL = range(0, 99 + 1) # excluding 100

def mod_cur_index(mode, cur_index, displacement):
    return cur_index - displacement if mode == "L" else cur_index + displacement

def calc_dist(mode, cur_index):
    return cur_index if mode == "L" else 99 - cur_index

def passed_zero(mode, a, b):
    if mode == "L":
        range_range = (b, a + 1)
    else:
        range_range = (a, b + 1)
    return True if 0 in range(range_range[0], range_range[1]) else False

for input in inputs:
    turn_direction, turn_amount = input[0], int(input[1:])
    dist = calc_dist(turn_direction, cur_index)

    print(f"dir: {turn_direction} amnt: {turn_amount} dist: {dist}")

    if not turn_amount > dist:
        temp = cur_index
        cur_index = mod_cur_index(turn_direction, cur_index, turn_amount)
        
        pass_zero += 1 if passed_zero(turn_direction, temp, cur_index) else 0
        
        print(f"NON wrapped cur index {cur_index}")
    else:
        temp = cur_index
        cur_index = mod_cur_index(turn_direction, cur_index, dist)
        pass_zero += 1 if passed_zero(turn_direction, temp, cur_index) else 0
                
        turn_amount -= dist
        
        print(f"aaah {cur_index} {turn_amount} {dist}")

        while turn_amount != 0:
            cur_index = 99 if turn_direction == "L" else 0
            range_incl_0 = False
            # if cur_index == 0: pass_zero += 1
            turn_amount -= 1
            dist = calc_dist(turn_direction, cur_index)
            
            temp = cur_index
            if not turn_amount > dist:
                cur_index = mod_cur_index(turn_direction, cur_index, turn_amount)
                turn_amount -= turn_amount
            else:
                cur_index = mod_cur_index(turn_direction, cur_index, dist)
                turn_amount -= dist
            pass_zero += 1 if passed_zero(turn_direction, temp, cur_index) else 0
        print(f"wrapped cur index {cur_index}")
        
    print(f"PASS ZERO {pass_zero}")
    
    # if cur_index == 0:
    #     pass_zero += 1
print(pass_zero)

# print(inputs)