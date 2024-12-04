def main():
    left = []
    right = []

    total = 0

    with open("./Day1/input1.txt") as file:
        lines = file.read().split("\n")

        for line in lines:
            left.append(line.split("   ")[0])
            right.append(line.split("   ")[1])

        for i in left:
            count = 0
            for x in right:
                if i == x:
                    count += 1
            total += count * int(i)
    return total

print(main())