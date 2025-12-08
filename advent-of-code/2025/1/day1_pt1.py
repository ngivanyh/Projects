inputs = open("inputs.txt").read().split("\n")

land_on_zero = 0
cur_index = 50 # the current index = the current value at that index
DIAL = range(0, 99 + 1) # excluding 100

def mod_cur_index(mode, cur_index, displacement):
    return cur_index - displacement if mode == "L" else cur_index + displacement

def calc_dist(mode, cur_index):
    return cur_index if mode == "L" else 99 - cur_index

for input in inputs:
    turn_direction, turn_amount = input[0], int(input[1:])
    dist = calc_dist(turn_direction, cur_index)

    print(f"dir: {turn_direction} amnt: {turn_amount} dist: {dist}")

    if not turn_amount > dist:
        cur_index = mod_cur_index(turn_direction, cur_index, turn_amount)
        
        print(f"NON wrapped cur index {cur_index}")
    else:
        cur_index = mod_cur_index(turn_direction, cur_index, dist)
        turn_amount -= dist
        
        print(f"aaah {cur_index} {turn_amount} {dist}")

        while turn_amount != 0:
            cur_index = 99 if turn_direction == "L" else 0
            turn_amount -= 1
            dist = calc_dist(turn_direction, cur_index)
            if not turn_amount > dist:
                cur_index = mod_cur_index(turn_direction, cur_index, turn_amount)
                turn_amount -= turn_amount
            else:
                cur_index = mod_cur_index(turn_direction, cur_index, dist)
                turn_amount -= dist
        print(f"wrapped cur index {cur_index}")

    
    if cur_index == 0:
        land_on_zero += 1
print(land_on_zero)

# print(inputs)