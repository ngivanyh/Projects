# UVa: The Blocks Problem

def find_block(blocks, block):
    for i, stack in enumerate(blocks):
        try:
            stack_idx = stack.index(block)
            return (i, stack_idx)
        except ValueError:
            continue
    return None


def move(blocks, preposition, target, destination):
    target_idx = find_block(blocks, target)

    if target_idx is None:
        print(f"Error: Cannot find target block of number {target}")
        return

    _ = [blocks[block].append(block) for block in blocks[target_idx[0]][target_idx[1] + 1:]]
    blocks[target_idx[0]] = blocks[target_idx[0]][target_idx[1]:]

    if preposition == "onto":
        pass # move everything above b to their original positions


def pile(blocks, preposition, target, destination):
    pass


def main():
    blocks = [[n] for n in range(int(input()))]

    while (command := input()) and command != "quit":
        try:
            command = command.split(" ")
        except Exception:
            print("Error: Invalid Command")
            break

        action = command[0]
        preposition = command[2]
        target, destination = int(command[1]), int(command[3])

        if target == destination:
            continue

        print(target, destination)

        match action:
            case "move":
                move(blocks, preposition, target, destination)
            case "pile":
                pile(blocks, preposition, target, destination)
            case _:
                print("Error: Invalid action")
                break

    for i, stack in enumerate(blocks):
        print(f"{i}: {" ".join(map(str, stack))}")


if __name__ == "__main__":
    main()
