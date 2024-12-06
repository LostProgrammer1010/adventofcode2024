def main(file):
  safe_total = 0

  with open(file, 'r') as file:
    lines = file.read().split("\n")

    
    for line in lines:
      numbers = line.split(" ")
      safe = True
      increasing = True
      if int(numbers[0]) - int(numbers[1]) > 0:
          increasing = False
      for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1]:
          safe = False
          break
        elif abs(int(numbers[i]) - int(numbers[i+1])) > 3:
          safe = False
          break
        elif int(numbers[i]) < int(numbers[i+1]) and not increasing:
          safe = False
          break
        elif int(numbers[i]) > int(numbers[i+1]) and increasing:

          safe = False
          break

      if safe:
        safe_total += 1 
        
        


  return safe_total




print(main("./Day2/small_input.txt"))
print(main("./Day2/input.txt"))