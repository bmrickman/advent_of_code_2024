i = 0
do = True
total = 0


def expect_mult():
    global i
    global instructions
    global total
    if instructions[i : i + 4] == "mul(":
        i = i + 4
        num1 = ""
        num2 = ""
        char = instructions[i]
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


def expect_do():
    global i
    global instructions
    global do
    if instructions[i : i + 4] == "do()":
        do = True
        i = i + 4
        return True
    return False


def expect_dont():
    global i
    global instructions
    global do
    if instructions[i : i + 7] == "don't()":
        do = False
        i = i + 7
        return True
    return False


with open("./day3/input.txt", "r") as f:
    instructions = f.read()


while i <= len(instructions) - 1:
    if expect_do():
        pass
    elif expect_dont():
        pass
    elif do and expect_mult():
        pass
    else:
        i = i + 1

print(total)
