def main():
    left = []
    right = []
    distance = 0
    with open("./Day1/input1.txt") as file:
        lines = file.read().split("\n")
        for line in lines:
            left.append(line.split("   ")[0])
            right.append(line.split("   ")[1])
        left = sorted(left)
        right = sorted(right)
        print(left)
        for i in range(len(left)):
            distance += abs(int(left[i]) - int(right[i]))

    return distance
            

print(main())