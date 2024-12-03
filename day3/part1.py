def parse_instructions(instructions: str):
    total = 0
    i = 0
    char_buffer = []
    num1 = ""
    num2 = ""

    def reset():
        nonlocal char_buffer
        nonlocal num1
        nonlocal num2
        nonlocal i
        char_buffer = []
        num1 = ""
        num2 = ""
        i = i + 1

    while i <= len(instructions) - 1:
        char = instructions[i]
        if char == "m" and len(char_buffer) == 0:
            char_buffer.append(char)
            i = i + 1
        elif char == "u" and len(char_buffer) != 0 and char_buffer[-1] == "m":
            char_buffer.append(char)
            i = i + 1
        elif char == "l" and len(char_buffer) != 0 and char_buffer[-1] == "u":
            char_buffer.append(char)
            i = i + 1
        elif char == "(" and len(char_buffer) != 0 and char_buffer[-1] == "l":
            char_buffer.append(char)
            i = i + 1
        elif len(char_buffer) != 0 and char_buffer[-1] == "(":
            while char.isnumeric():
                num1 = num1 + char
                i = i + 1
                char = instructions[i]
            if char == ",":
                i = i + 1
                char = instructions[i]
                while char.isnumeric():
                    num2 = num2 + char
                    i = i + 1
                    char = instructions[i]
                if char == ")":
                    total = total + (int(num1) * int(num2))
                    reset()
                else:
                    reset()
            else:
                # got to "mult(123" but there wasn't a ","
                reset()
        else:
            reset()

    return total


# testing:
test_value = parse_instructions(
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
)
assert test_value == 161


if __name__ == "__main__":
    with open("./day3/input.txt", "r") as f:
        instructions = f.read()
        print(parse_instructions(instructions))
