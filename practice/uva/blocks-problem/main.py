# UVa: The Blocks Problem

blocks = []

def find_block(block):
    global blocks

    for i, stack in enumerate(blocks):
        try:
            stack_idx = stack.index(block)
            return (i, stack_idx)
        except ValueError:
            continue
    return None

def return_blocks(block):
    global blocks

    block_idx = find_block(block)

    if block_idx is None:
        return

    stack_length = len(blocks[block_idx[0]]) # initial stack length
    for i in range(stack_length - 1, block_idx[1], -1):
        move_block = blocks[block_idx[0]].pop(i) # pop returns the value of the list element removed
        blocks[move_block].append(move_block)

def move(preposition, target, destination):
    global blocks

    return_blocks(target)

    if preposition == "onto":
        return_blocks(destination)

    target_idx, destination_idx = find_block(target), find_block(destination)

    blocks[target_idx[0]].remove(target)
    blocks[destination_idx[0]].append(target)

def pile(preposition, target, destination):
    global blocks

    if preposition == "onto":
        return_blocks(destination)

    target_idx, destination_idx = find_block(target), find_block(destination)

    move_stack = blocks[target_idx[0]][target_idx[1]:].copy() # .copy() present because the need of a copy of the list, not a pointer to it
    blocks[target_idx[0]] = blocks[target_idx[0]][:target_idx[1]]
    blocks[destination_idx[0]] += move_stack

def main():
    global blocks

    blocks = [[n] for n in range(int(input()))]

    while (command := input()) and command != "quit":
        command = command.split(" ")

        action, preposition = command[0], command[2]
        target, destination = int(command[1]), int(command[3])

        # invalid commands
        if (
            target == destination
            or find_block(target)[0] == find_block(destination)[0]
        ): continue

        # action delegation
        if action == "move":
            move(preposition, target, destination)
        elif action == "pile":
            pile(preposition, target, destination)
        else:
            break

    for i, stack in enumerate(blocks):
        print(f"{i}: {' '.join(map(str, stack))}")

if __name__ == "__main__":
    main()
